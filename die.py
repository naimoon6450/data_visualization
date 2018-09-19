from random import randint

class Die():
    #class for a single die

    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        #return random value between 1 and number of num_sides
        return randint(1,self.num_sides)
