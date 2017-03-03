from random import randint



class Dice(object):
    listOfTypes = [3,4,6,8,10,12,20,100]
    def __init__(self, dice_type):
        if dice_type in self.listOfTypes:
            self.dice_type = dice_type
        else:
            raise ValueError('nie ma takiej kostki')

    def roll(self):
        number = randint(1, self.dice_type+1)
        return number

    def roll_generator(self):
        for throw in range(0, 10)
            yield self.roll()