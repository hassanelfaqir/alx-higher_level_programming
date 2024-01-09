#!/usr/bin/node
let na = 0;

exports.logMe = function (item) {
  console.log(na + ': ' + item);
  na++;
};
