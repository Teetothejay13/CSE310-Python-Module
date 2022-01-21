# Overview

In creating this program, I am refreshing my knowledge of Python. At the time of creating this, I have not had a chance to use Python in about 6 months, so much of my knowledge is rusty. By creating a program such as this, I can refresh my knowledge, as well as have a good program for learning other languages. As everyone knows, one of the best ways to learn a new programming language is to recreate an old program you already have, but in the new language. I feel like the amount of concepts covered by this program will be a good learning aide for future languages.

In this program, I created a user input loop so that the user did not have to restart the program every time they wanted to select a different option. Among these options, the user can choose to read a file, edit a file, or create a new file. These files will be baking or cooking recipes, stored as JSON files that can be manipulated however the user wants.

I am an avid baker, so I came up with this idea of a digital recipe box while I was baking some banana bread (see the recipe included). It will come in handy when I am away from my physical copy of my recipes.


[Recipe Book Program Demonstration](https://youtu.be/UsklABfjv9E)

# Development Environment

I used the VS Code editor to develop this program.

I used python for this program, and I included the json library. I wanted a way to store recipes, but not as one big block of text. Editing
a big text file would be annoying, so making each recipe a JSON file I can interact with was much easier and more efficient.

# Useful Websites

* [Stack Overflow JSON Forum](https://stackoverflow.com/questions/32991069/python-checking-for-json-files-and-creating-one-if-needed)
* [Grepper JSON Dump to File](https://www.codegrepper.com/code-examples/javascript/json+dump+to+file)
* [Stack Overflow Git Version Control](https://stackoverflow.com/questions/9335486/git-how-to-roll-back-to-last-push-commit)

# Future Work

* Implement editRecipe() function
* Add input checking methods, ensuring only valid inputs are accepted
* Add a description functionality to the program and json files