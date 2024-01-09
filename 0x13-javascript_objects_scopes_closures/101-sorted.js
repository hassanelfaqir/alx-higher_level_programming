#!/usr/bin/node
const dict = require('./101-data').dict;

const total = Object.entries(dict);
const val = Object.values(dict);
const valsU = [...new Set(vals)];
const newDict = {};
for (const j in valsU) {
  const list = [];
  for (const k in total) {
    if (total[k][1] === valsU[j]) {
      list.unshift(total[k][0]);
    }
  }
  newDict[valsU[j]] = list;
}
console.log(newDict);
