#!/bin/bash
# This script makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with a message "You got me!", in the body of the response
curl -s -X PUT -d "user_id=98" 0.0.0.0:5000/catch_me
