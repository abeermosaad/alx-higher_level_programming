#!/usr/bin/node
let len = process.argv.length - 2; const arr = [];
if (len === 0 || len === 1) {
  console.log(0);
  process.exit();
}
for (let i = 2; i < len; i++) {
  arr.push(process.argv[i]);
}
len = arr.length;
arr.sort();
console.log(arr[len - 2]);
