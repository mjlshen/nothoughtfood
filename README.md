time2eat
========

MHacks III Project - time2eat

Instructions
==============================================================
Enter the time in minutes you want to finish preparing a meal, followed by "b", "l", or "d" and then press <Enter> to submit the request. For example, "35d" would return a recipe for a 35 minute dinner and "15b" would return a recipe for a 15 minute breakfast. If you want to make the recipe, you can click on "Directions" at the bottom of the list of ingredients to view the full instructions necessary to create the meal.

Code
==============================================================
This app was created using Flask, a microframework based on Python. If you ever want to create a web application, I highly recommend it! Of course, since it is a web app, it also uses HTML, JavaScript, and CSS.

Tidbits
==============================================================

Originally, the idea was to create a web app where the user could type in specific ingredients and the app would display possible recipes the user could make. Unfortunately, I am was not familiar enough with creating and using a database and perhaps even the search functionality necessary to bring the idea into fruition. Thankfully, I was told another, related idea by an anonymous individual (who will remain as such unless he or she requests otherwise): the user will input the time they want to spend making a specific meal and the app will return possible recipes. Here is my group's attempt!

This app was created at MHacks III, inside The Qube, a Quicken Loans office space in Detroit, MI.

Future Improvement
==============================================================

1. Create a more user-friendly interface. Currently, it may as well be glorified  command-line interface. I am able to do this with my current skill set.

2. Improve database to include more than one recipe per time/meal option. This would involve creating a new database, or altering the search function to allow more than one result per input. I would need to learn either method as I do not know how to do this at the moment.

3. Realize my initial goal to allow ingredient-to-recipe functionality. This would build upon the database and would probably require a separate search function. This currently seems out of my reach, but if I achieve the second step, this may be reasonable.
