#!/usr/bin/node
const fs = require('fs');

const fArgs = fs.readFileSync(process.argv[2]).toString();
const sArgs = fs.readFileSync(process.argv[3]).toString();
fs.writeFileSync(process.argv[4], fArgs + sArgs);
