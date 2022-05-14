from game.die import Die

class Director:

    def __init__(self):
        # Initiates all the variables
        self.is_playing = True
        #Player starts with 300 points
        self.total_score = 300

    def start_game(self):
        print(chr(27) + "[2J")
        print ("Welcome to Hi/Lo")
        print()
        input("Press Enter to Start...") 
        print(chr(27) + "[2J")


        # Game play loop
        while self.is_playing:
            print()
            self.get_inputs()
            self.do_updates()
            self.do_outputs()
        
        # Ending Printout
        print()
        print(chr(27) + "[2J")
        print("Thanks for Playing")
        print(f"Score: {self.total_score}\n")

    # Creates random card for user
    def get_inputs(self):
        # chooses card
        self.previous_value = Die.roll()

        # Get input for hi/lo
        print(f"Current Value is: {self.previous_value}")
        self.hilorequest = input("Higher or Lower (H/L): ")
        self.value = Die.roll()
       
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

    def do_outputs(self):
    # Prints the score and card rolled
        print(f"Your card is: {self.value}")
        print(f"Your score is: {self.total_score}\n")

        values = ""
        self.score = 0

    # Determines if player has enough points or if player wants to play
        if self.total_score < 1:
            self.is_playing = False
        else:
            player_continue = input("Do you want to keep playing (Y/N): ")
            print(chr(27) + "[2J")
            if player_continue == "N":
                self.is_playing = False
