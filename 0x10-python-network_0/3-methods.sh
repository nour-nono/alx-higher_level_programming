#!/bin/bash
# Display all HTTP methods the server of a given URL will accept.
# curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
curl -sIX OPTIONS 0.0.0.0:5000/route_4 | grep Allow | sed "s/Allow: //"
