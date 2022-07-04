#!/bin/bash

USER_FNAME_KEY="firstName"
USER_LNAME_KEY="lastName"
COLOR_KEY="favoriteColor"

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
    echo "Enter a first name, a last name, then a color in that order."
    read firstName lastName favColor
    if [ -z "$firstName" ] || [ -z "$lastName" ] || [ -z "$favColor" ]; then
      echo "A first name, last name, and color must be provided, separated by spaces. Try again!"
      continue
    else
      curl -X POST -H "Content-Type: application/json" -d \
      "{\"${USER_FNAME_KEY}\": \"${firstName}\", \"${USER_LNAME_KEY}\": \"${lastName}\", "\
"\"${COLOR_KEY}\": \"${favColor}\"}" http://localhost:5000/users
      echo "Run the corresponding 'Get All' command to see if the collection updated!"
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
