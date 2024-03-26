let's start JS :)
in node js process.argv
The first element will be process.execPath (the path to the Node.js executable, which is probably /usr/bin/node or /usr/bin/nodejs)
The second element will be the path to the JavaScript file you are running (example: /path/to/my/example.js)
the remaining elements will be any additional command line arguments.
If there is no additional command line arguments, process.argv will be an array with just two elements: ['path/to/node', 'path/to/js']
############################################################################################################
in node js if we want something to be visible from outside the file we need to export it:

exporting a global function
foo = function () {
  console.log("foo!");
}
we don't need to export it, it's global

exporting anonymous functions
module.exports = function (args) {
  return args.reduce((a, b) => a + b);
};

exporting named functions
module.exports.add_func = function (a, b) {
  return a + b;
};
