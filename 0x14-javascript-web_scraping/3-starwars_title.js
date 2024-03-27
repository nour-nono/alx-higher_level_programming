#!/usr/bin/node
req = require('request');
req('https://swapi-api.alx-tools.com/api/films/:id' + process.argv[2], function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
