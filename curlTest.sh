#!/bin/bash

USER_FNAME_KEY="firstName"
USER_LNAME_KEY="lastName"

while : ;
do
  echo "1 - Add new user entry"
  echo "2 - Get all user entries"
  echo "3 - Exit program"

  read -p "Please choose one of the options above by entering it's corresponding number: " userIn

  if [ -z "${userIn}" ]; then
    userIn='-1'
  fi

  if [ $userIn == 1 ]; then
    echo "Enter a first name then a last name, in that order."
    read firstName lastName
    if [ -z "$firstName" ] || [ -z "$lastName" ]; then
      echo "Both a first name and last name must be provided, separated by a space. Try again!"
      continue
    else
      echo "Adding $firstName $lastName to the database!"
      echo "Run the corresponding 'Get All' command to see the updated collection"
      curl -X POST -H "Content-Type: application/json" -d \
      "{\"${USER_FNAME_KEY}\" : \"${firstName}\", \"${USER_LNAME_KEY}\": \"${lastName}\"}"  http://localhost:5000/users
    fi
  elif [ $userIn == 2 ]; then
    echo "Getting all user entries..."
    echo "$(curl http://localhost:5000/users)"
  elif [ $userIn == 3 ]; then
    echo "Exiting..."
    exit 0
  else
    echo "Invalid input!";
  fi

done
