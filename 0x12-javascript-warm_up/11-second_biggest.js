#!/usr/bin/node
if (process.argv.length < 4) {
  console.log("0");
} else {
  const arr = process.argv.slice(2);
  for (let index = 0; index < arr.length; index++) {
    arr[index] = +arr[index];
  }
  arr.sort().reverse();
  console.log(arr[1]);
}
