#!/usr/bin/node
req = require('request');
req(process.argv[2], function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    const tasks = JSON.parse(body);
    const completedTasks = tasks.filter(task => task.completed === true);
    console.log(completedTasks.length);
  }
});
