const potrace = require('potrace'); const fs = require('fs');
const opts = { threshold: 128, turdSize: 4, optTolerance: 0.3, alphaMax: 1.0 };
for (const n of ['word','illo','tag']) potrace.trace(`part-${n}.png`, opts, (e, svg) => { if (e) throw e; fs.writeFileSync(`d-${n}.txt`, svg.match(/ d="([^"]+)"/)[1]); console.log(n, 'done'); });
