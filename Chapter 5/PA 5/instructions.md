For the chapter 5 PA, we are going to read some data about movies from an online JSON file, and do some basic statistics on the data therein.

First, take a look at the movies.json file, by clicking on this URL: http://programminginprocessing.com/movies.json

The 'movies' key is associated with a JSON array of 18,095 JSON objects, each of which represents a single movie. These movies are a small subset of the movies from the popular IMDB site. Each movie object has entries for the movie's id, title, year, and running time. Note that all of these entries are strings.

Create a Google Colab Jupyter notebook that does the following:

Read the JSON file from the URL above, and convert it into a Python dictionary object, and then get a list of the movie objects 
Use list comprehension to create a list of the movie objects with valid running times. Movies where the runtime is unknown have the value 'n/a' for the 'time' key. Hint: take advantage of the string [isnumeric()](https://www.tutorialspoint.com/python/string_isnumeric.htm). method

Write a function named shortestMovie(), which takes the list you created in step two as a parameter, and returns the movie object with the shortest running time, and another function named longestMovie(), which is similar, but returns the movie object with the longest running time

Finally, create a function named averageLength(), which takes the list created in step two as a parameter and returns the mean running time for all of the movies that have valid run time values
For step 3, it is important that you return the entire movie object for each function, not merely the time. For example, if the 1910 movie "Arms and the Woman" had either the shortest or longest running time, printing the return from one of the functions would produce this output:

`{'id': 'tt0006371', 'time': '50', 'title': 'Arms and the Woman', 'year': '1916'}`

Once your code is complete, download your notebook as a .ipynb file, and submit it via this assignment posting.
