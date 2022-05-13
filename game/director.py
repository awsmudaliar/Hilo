from game.die import Die
import random

class Director:

    def __init__(self):
        self.dice = 0
        self.is_playing = True
        self.value = 0
        #Player starts with 300 points
        self.score = 0
        self.total_score = 300
        self.hilorequest = ""
        self.previous_value = 0

    def start_game(self):
        #self.previous_value = random.randint(1,13)
        self.previous_value = Die.roll()

        print ("Welcome to Hi/Lo")
        print()
        input("Press Enter to Start...") 

        while self.is_playing:
            print()
            self.get_inputs()
            self.do_updates()
            self.do_outputs()
        
        print()
        print("Thanks for Playing")
        print(f"Score: {self.total_score}\n")

    def get_inputs(self):
        # Get input for hi/lo
        print(f"Current Value is: {self.previous_value}")
        self.hilorequest = input("Higher or Lower (H/L): ")

       
    def do_updates(self):

        if not self.is_playing:
            return 

        self.value = Die.roll()

        # Evaluate the card
        if self.hilorequest == "h" or "H":
            if self.value > self.previous_value:
                self.points = 100
            else:
                self.points = -75
        elif self.hilorequest == "l" or "L":
            if self.value < self.previous_value:
                self.points = 100
            else:
                self.points = -75


    def do_outputs(self):

        if not self.is_playing:
            return
        
        values = ""
        self.score = 0
        self.value = self.previous_value

        print(f"You rolled: {self.value}")
        print(f"Your score is: {self.total_score}\n")
        self.is_playing == (self.score > 0)