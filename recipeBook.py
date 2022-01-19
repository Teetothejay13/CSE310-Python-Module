# 1. Name:
#      TJ Putnam
# 2. Program Name:
#      Recipe Book
# 3. Program Description:
#      This program will take an input in the form of a file name, and look for a json file with that name. If it exists,
#      then it will open the file and read it. If it doesn't, then the program will ask if the user wants to create the
#      file, and comply if they do. If the file exists/once it is created, the user can select an input to read the recipe,
#      edit the recipe, or open a new recipe.
# 4. What was the hardest part?
#      
# 5. How long did it take for me to complete the assignment?
#      

# we'll need these
import json
import os
import io


# main will run the show
def main():
    # first, we need an input loop the user can quit from
    userInput = ""
    print("Welcome to your personal recipe book!/n")
    while userInput != "q":
        print("Please select what you would like to do:/n")

# this function will open the file and read it after checking if it's there, prompting to create the file if it isn't
def openFile(fileName):
    pass

# this function will allow the user to edit the recipe and save the changes
def editRecipe(fileName):
    pass

# this function will display the information that the user needs displayed
def display():
    pass