# library
import random


# class
class Dice:
    # initialisation
    def __init__(self, sides):
        self.sides = sides

    # method
    def roll(self):
        return random.randint(1, self.sides)


# objects
d6 = Dice(6)
d20 = Dice(20)

print(d6.roll())
print(d20.roll())
