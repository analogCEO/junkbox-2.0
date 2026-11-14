"""Write design-system/project/tokens.css from tokens.json (layout of the Design System type's compiled tokens.css)."""
import json, sys, os
root = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), '..', 'design-system', 'project')
t = json.load(open(os.path.join(root, 'tokens.json')))
themes = [th['id'] for th in t['color']['themes']]
first = themes[0]
def val(tok, th):
    v = tok['value']
    return v if isinstance(v, str) else v.get(th, v[first])
out = ['/* Junkbox 2.0 — generated from tokens.json */']
lines = [f'  --{c["name"]}: {val(c, first)};' for c in t['color']['tokens']]
lines += [f'  --{s["name"]}: {val(s, first)};' for s in t.get('shadow', {}).get('tokens', [])]
out.append(f':root, [data-theme="{first}"] {{\n' + '\n'.join(lines) + '\n}')
for th in themes[1:]:
    lines = [f'  --{c["name"]}: {val(c, th)};' for c in t['color']['tokens'] if val(c, th) != val(c, first)]
    lines += [f'  --{s["name"]}: {val(s, th)};' for s in t.get('shadow', {}).get('tokens', []) if val(s, th) != val(s, first)]
    out.append(f'[data-theme="{th}"] {{\n' + '\n'.join(lines) + '\n}')
lines = [f'  --{s["name"]}: {s["value"]};' for fam in ('spacing', 'radius') for s in t[fam]['tokens']]
lines += [f'  --font-{k}: {v};' for k, v in t['type']['families'].items()]
out.append(':root {\n' + '\n'.join(lines) + '\n}')
for g in t['type']['groups']:
    for s in g['styles']:
        fam = s.get('family', g['family'])
        decl = [f'font-family: var(--font-{fam})', f'font-size: {s["fontSize"]}', f'line-height: {s["lineHeight"]}', f'font-weight: {s["fontWeight"]}']
        if 'letterSpacing' in s: decl.append(f'letter-spacing: {s["letterSpacing"]}')
        out.append(f'.{s["name"]} {{ ' + '; '.join(decl) + '; }')
open(os.path.join(root, 'tokens.css'), 'w').write('\n'.join(out) + '\n')
print('tokens.css written')
