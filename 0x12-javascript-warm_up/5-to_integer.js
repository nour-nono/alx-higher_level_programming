#!/usr/bin/node
const x = +process.argv[2] ? `My number: ${+process.argv[2]}` : 'Not a number';
console.log(x);
