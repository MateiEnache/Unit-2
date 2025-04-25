import random

class Die():
    """Creates a Dice"""

    def __init__(self,sides):
        """initializes the die"""
        self.sides = 6
        self.sides = sides
        
        
    def roll_die(self):
        """rolls a die"""

        return random.randint(1,self.sides)


def lotto():
    list = [0,1,2,3,4,5,6,7,8,9,"M","A","T","E","I"]
    for i in range(4):
        digit = random.randint(0,14)


def main():
    D6 = Die(6)
    D10 = Die(10)
    D20 = Die(20)
    for i in range(10):
        D6.roll_die()
        D10.roll_die()
        D20.roll_die()

main()