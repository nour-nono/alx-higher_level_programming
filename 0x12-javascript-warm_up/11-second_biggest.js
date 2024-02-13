#!/usr/bin/node
const arr = process.argv.slice(2);
for (let index = 0; index < arr.length; index++) {
  arr[index] = +arr[index];
}
arr.sort((a, b) => b - a);
console.log(arr[1] || 0);
