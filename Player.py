"""
James Hendry
Version 0.1 Alpha
the player class.
"""
import random

class Player:

    isAlive = True

    """
    for the current simulation
    """
    def vote( self , selfNumber , pickedNumber):
        if selfNumber is pickedNumber:
            random.seed(selfNumber)
            return random.randint(0,pickedNumber)
        
        else:
            return(pickedNumber)
###################################

"""
    for a later date
    def vote( amountOfPlayers, selfNumber ):
        random.seed(selfNumber)
        return  random.randint(0,pickedNumber)
"""