#!/usr/bin/node
req = require('request');
req('https://swapi-api.alx-tools.com/api/films/', function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    let count = 0;
    for (const film of JSON.parse(body).results) {
      for (const character of film.characters) {
        if (character.includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
