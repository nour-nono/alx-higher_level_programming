#!/usr/bin/node
function factorial(a) {
    if (a<1) {
        return 1;
    }
    if (a === 1) {
        return a;
    }
    return a*factorial(a-1);
}
console.log(factorial(process.argv[2]));
