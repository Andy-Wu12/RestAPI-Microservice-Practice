# Flask Rest API Practice <br/>
**This repository will show my work during my time learning to write REST APIs.**

To run this project, you either need to have MongoDB (and preferably Compass) installed and setup 
on your device or a MongoDB Atlas account. <br/>
Atlas provides free tiers, which are more than enough
for this project.

[Download MongoDB Community Server](https://www.mongodb.com/try/download/community) <br/>
[Use MongoDB Atlas](https://www.mongodb.com/atlas/database)

For this project, you will simply need two python modules, both of which we can install with pip.
I use a virtual environment for this project, but you don't need to.
If you would like to set one up or just learn more about it, refer to [this documentation](https://docs.python.org/3/library/venv.html)

#### You can install the necessary packages with by running the following commands:
1. pip3 install flask
2. pip3 install pymongo

#### Once you have the project downloaded, follow these steps to get started

1. cd into the project folder
2. Run the command _python3 server.py_ in your terminal. 
   1. Add an optional -d if you want to run the server in _detached state_, although it may be easier to just manage two terminal tabs
3. Open a browser and navigate to [http://localhost:5000/users](http://localhost:5000/users)
4. In another terminal tab (or the same one if you detached the server process), run the command 
_chmod +X curlTest.sh_
5. Afterward, run the shell script (which varies depending on your operating system) to test the functionality.
   1. For me on Mac OS X, I can run the script successfully with 
      1. _./curlTest.sh_
      2. _bash curlTest.sh_

Building this project with Docker is something I plan to implement soon.

