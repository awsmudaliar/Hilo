import random

class Die:
    def roll():
        #Chooses a card value range from 1 - 13
        value = random.randint(1,13)
        return value