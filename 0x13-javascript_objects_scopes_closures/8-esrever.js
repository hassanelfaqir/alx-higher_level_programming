#!/usr/bin/node
exports.esrever = function (list) {
  let len = list.length - 1;
  let j = 0;
  while ((len - j) > 0) {
    const aux = list[len];
    list[len] = list[j];
    list[j] = aux;
    j++;
	  len--;
  }
  return list;
};
