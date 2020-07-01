# My-first-project
I have done this project as a close to a course on python that i have been doing as an absolute beginner

Collection of geodata and visualization of landscaping companies registered on the yelp API
in every county in England, Scotland, Wales and Northern Ireland

The point of this is to give me a rough guide of the geographical spread of a type of business. And this could easily be adapted to handle user input to determine other types of businesses for the search.



yelp3.py I wrote from scratch which gathers and starts to clean the data and stores it in a database (fname.sqlite)

yelptowhere.py was from my course but has been heavily edited up to 50%, cleans and writes data to where.js

The part i am not so good at... although the course is primaraly python based so my main concern was getting the above scripts to work with the... 
Visualization 

where.js is a simple JavaScript file that yelptowhere.py updates with the name of the business in the search and coordinates for that business. An example of this was available under a creative commons licence from py4e.com

where.html is very lightly edited and available under a creative commons licence from py4e.com

The run order is 
yelp3.py
yelptowhere.py
Then open where.html to visualise

The database browser and SQL used is SQLite
