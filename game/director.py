from game.die import Die


class Director:

    def __init__(self):

        self.dice = []
        self.is_playing = True
        self.score = 0
        self.total_score = 0

        # Replace the following code bellow
        for i in range(5):
            die = Die()
            self.dice.append(die)

    def start_game(self):

        print ("Welcome to Dice")
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
        while True:
            roll_dice = input("Roll dice? [y/n] ")
            if roll_dice == "y":
                break
            elif roll_dice == "n":
                break
            else:
                print("Invalid Input")
                print("")

        self.is_playing = (roll_dice == "y")

       
    def do_updates(self):

        if not self.is_playing:
            return 

        for i in range(len(self.dice)):
            die = self.dice[i]
            die.roll()
            self.score += die.points 
        self.total_score += self.score

    def do_outputs(self):

        if not self.is_playing:
            return
        
        values = ""
        for i in range(len(self.dice)):
            die = self.dice[i]
            values += f"{die.value} "

        print(f"You rolled: {values}")
        print(f"Your score is: {self.total_score}\n")
        self.is_playing == (self.score > 0)