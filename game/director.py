from game.die import Die
import random

class Director:

    def __init__(self):

        self.dice = []
        self.is_playing = True
        #Player starts with 300 points
        self.score = 0
        self.total_score = 300
        self.hilorequest = ""
        self.previous_value = 0
        die = Die()
        self.dice.append(die)

    def start_game(self):
        self.previous_value = random.randint(1,13)

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

        die = self.dice[0]
        die.roll()
        self.score += die.points 
        self.total_score += self.score

    def do_outputs(self):

        if not self.is_playing:
            return
        
        values = ""
        self.score = 0
        self.value = self.previous_value

        print(f"You rolled: {self.value}")
        print(f"Your score is: {self.total_score}\n")
        self.is_playing == (self.score > 0)