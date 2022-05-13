import random

class Die:
    def __init__(self):
        self.value = 0
        self.points = 0
        self.hilorequest = ""
        self.previous_value = 0


    def roll(self):
        #Card values range from 1 - 13
        self.value = random.randint(1,13)
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