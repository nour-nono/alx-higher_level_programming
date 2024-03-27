#!/usr/bin/node
req = require('request');
req(process.argv[2], function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    req = require('fs');
    req.writeFile(process.argv[3], body, 'utf8', function (err) {
      if (err) {
        console.log(err);
      }
    });
  }
});
