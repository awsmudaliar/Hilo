# Hilo (updated)
H**ow did you apply abstraction in your program's design?**
We took the complex coding solution of developing the Hi-Low game and applied abtraction to our design by creating classes that simplied the process.

Title: Project Team 1: HI/LOW
**Description: **
Hilo is a game in which the player guesses if the next card drawn by the dealer will be higher or lower than the previous one. Points are won or lost based on whether or not the player guessed correctly.

**Required software: **
  - python v3.10.4 
  - import random
  
**Project structure: **  
Design Plan
Object 1: director
Class: Director
This class will have 5 modules
Init: this will used to give some variable default values

Start_Game: This has 3 sections 
  1) Welcome new players
  2) A loop that will keep running the game until the player quits or loses
  3) Thank's the player for playing and display's their final scores

Get_inputs: This will get all the inputs needed to run the game
  1) The inital number, player guess, and evaluate inputs and varaibles for a result
  2) The player guesses High or Low
  3) The number that will be compared to the inital number

do_updates: This is used to evaluate the players guess. Additionally, assigns points based on if they guess correct or incorrect

do_outputs: This does 3 things
  1) Prints out their card that was drawn and shows current score
  2) Determines if the player can play based on the current score (must have more than zero points)
  3) Asks the user if they would like to carry on playing

Object 2: die
Class: Die
This class has one purpose to generate a random number from 1 to 13. It will need the random library imported to work. This class will be used by the Director class. In this application it will be used to generate all numbers needed. 
  
Team member names and email addresses
- Alex M awsmudaliar@byui.edu
- Peter Babcock peterb@saefl.com
- Rachel Knight kni21003@byui.edu
