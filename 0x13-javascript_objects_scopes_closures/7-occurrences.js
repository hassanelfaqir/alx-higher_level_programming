#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let nOccurrences = 0;
  for (let j = 0; j < list.length; j++) {
    if (searchElement === list[j]) {
      nOccurrences++;
    }
  }
  return nOccurrences;
};
