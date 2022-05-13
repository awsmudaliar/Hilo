import random

class Die:
    def __init__(self):
        # Initiates all the variables
        self.value = 0
        self.points = 0


    def roll():
        #Chooses a card value range from 1 - 13
        value = random.randint(1,13)
        return value