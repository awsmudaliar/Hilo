from game.die import Die
import random

class Director:

    def __init__(self):
        # Initiates all the variables
        self.dice = 0
        self.is_playing = True
        self.value = 0
        self.score = 0
        #Player starts with 300 points
        self.total_score = 300
        self.hilorequest = ""
        self.previous_value = 0

    def start_game(self):
        #self.previous_value = random.randint(1,13)
        self.previous_value = Die.roll()

        print ("Welcome to Hi/Lo")
        print()
        input("Press Enter to Start...") 

        # Game play loop
        while self.is_playing:
            print()
            self.get_inputs()
            self.do_updates()
            self.do_outputs()
        
        # Ending Printout
        print()
        print("Thanks for Playing")
        print(f"Score: {self.total_score}\n")

    # Creates random card for user
    def get_inputs(self):
        # chooses card
        self.value = Die.roll()

        # Get input for hi/lo
        print(f"Current Value is: {self.previous_value}")
        self.hilorequest = input("Higher or Lower (H/L): ")

       
    def do_updates(self):

        # Evaluates the card and the user input for points
        if self.hilorequest == "H":
            if self.value > self.previous_value:
                self.points = 100
            else:
                self.points = -75
        elif self.hilorequest == "L":
            if self.value < self.previous_value:
                self.points = 100
            else:
                self.points = -75
        # adds points to score
        self.total_score += self.points

    # Determines if player is eligible to play
    def do_outputs(self):
        if not self.is_playing:
            return
        
        values = ""
        self.score = 0

    # Prints the score and card rolled
        print(f"Your card is: {self.value}")
        print(f"Your score is: {self.total_score}\n")

    # Determines if player has enough points or if player wants to play
        if self.total_score < 1:
            self.is_playing = False
        else:
            player_continue = input("Do you want to keep playing (Y/N): ")

            if player_continue == "N":
                self.is_playing = False
