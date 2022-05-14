# Hilo (updated)

Peter Test
Alex Test
Rachel Test

How did you apply abstraction in your program's design?
We took the complex coding solution of developing the Hi-Low game and applied abtraction to our design by creating classes that simplied the process.

Week 4(Additions)
Title: Project HILOW
Description: 
Hilo is a game in which the player guesses if the next card drawn by the dealer will be higher or lower than the previous one. Points are won or lost based on whether or not the player guessed correctly.

Required software: 
  python v3.10.4 
  import random
  
Project structure:   
Design Plan
Object 1: director
Class: Director
This class will have 5 modules
Init: this will used to give some variable default values

Start_Game: This has 3 sections 
  1) Welcome new players
  2) A loop that will keep running the game until ther player quits or loses
  3) Thanking the player for playing and displaying their final scores

Get_inputs: this will get all the inputs needed to run the game
  1) The inital number, which the player will use to guess if the next number will be higher or lower
  2) the players guess High or Low
  3) The number that will be compated to the inital number

do_updates: This is used to evaluate the players guess and to assign points based on if the players guess correct or incorrect

do_outputs: This does 3 things
  1)prints out the card that was draw and shows the user there current scored
  2) determines if the player can keep player based on the current score (must have more than zero points)]]
  3) asks the user if they would like to carry on players

Object 2: die
Class: Die
This class has one purpose and that is to generate a random number from 1 to 13. It will need the random library imported to work.
This class will be used by the Director class. 
In this application it will be used to generate the initial  number and the Hi/Low number. 

  
Team member names and email addresses
Alex M awsmudaliar@byui.edu
Peter Babcock peterb@saefl.com
Rachel Knight kni21003@byui.edu
