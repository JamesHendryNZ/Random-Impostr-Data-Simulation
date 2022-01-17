"""
James Hendry
Version 0.1 Alpha
The Game that the simluations runs
many of.
some imposters and some boatdudes
imposters win if boatdudes die
boatdudes win if imposters get yeeted
"""

from typing import Iterable
from Imposter import Imposter
from Player import Player
from collections import Counter
from DataPoint import DataPoint
import random
import time

class Game:

    players = []
    random.seed(time.localtime())

    def __init__(self , playerAmount) -> None:
        
        counter = 1
        imposterAmount = int(playerAmount / 5)
        
        self.players = []

        while counter <= playerAmount:
            self.players.append(Player())
            counter += 1

        
        #choose some players to be imposters
        # choose random number
        # if number is the same choose random number again
        # until new number
        
        
        
        while imposterAmount > 0:            
            chosenImposter = random.randint(0,playerAmount-1)
            
            if self.checkImposter(self.players[chosenImposter] ) is False:
                self.players[chosenImposter] = Imposter()
                imposterAmount -= 1
        #----------------------------------------------------------
        pass

        #333333333333333333333333333333333333333333333333333333333333333333

    def checkImposter(  self , daPlayer ):
        if type(daPlayer) is Imposter:
            return True
        else:
            return False
        
    """
        Simulate game
        imposter kills one dude
        assume report before 2nd dead.
        do vote methhod 
        do yeet method for unfortunate player

        if imposters are equal to or grater than the players then
        the game is over and the imposters win
        """
    def simulateGame( self ):
        
        chosen2Die = 0
        chosen2Yeet = 0

        print("Game Simulation Started")
        
        

        random.seed( int(round(time.time() ) ) )
        
        while (self.checkImposterBalance( self.players )) == 0:
            
            print("started game round")
            print(self.checkImposterBalance( self.players ))

            chosen2Die = random.randint(0 , len(self.players) - 1)

            while self.checkImposter(self.players[chosen2Die]) is True:
                    chosen2Die = random.randint(0 , len(self.players) - 1)

            self.players.pop(chosen2Die)


            #vote simulation here
            chosen2Yeet = random.randint(0 , len(self.players) )

            currentPlayer = 0
            votes = []
            for player in self.players:
                votes.append(player.vote(currentPlayer,chosen2Yeet))
                currentPlayer += 1

            self.yeetPlayer( self.getMostCommonItem(votes) , self.players)
        #================================

        if self.checkImposterBalance(self.players) == 2:
            return self.createDataPoint(True)
        else:
            return self.createDataPoint(False)

    def getMostCommonItem( self, countableList ):
        itemData = Counter(countableList)
        return itemData.most_common(1)[0][0]

        #create game
        #return datapoint variable made by value game(Data made by game)

    def yeetPlayer( self , playerNumber , players):
        if self.checkImposter(players[playerNumber - 1]) is True:
            print( "Player " + str(playerNumber) + " was a Sussy Baka imposter")
        else:
            print( "Player " + str(playerNumber) + " was Sus But not an imposter")

        players.pop(playerNumber -1)

    #333333333333333333333333333333333333333333333333333333333333333333
    
    def checkImposterBalance( self , players ):
        
        #[ plyaerAmount , ImposterAmount ]
        composistion    = self.checkPlayerCompistion(players)
        
        playerAmount    = composistion[0]
        imposterAmount  = composistion[1]

        if imposterAmount == 0:
            return 1
        elif imposterAmount >= playerAmount:
            return 2
        else:
            return 0

    #3333333333333333333333333333333333333333333333333333333333333333333

    def checkPlayerCompistion( self , players):

        playerAmount = 0
        imposterAmount = 0
        compostition = [0,0]

        for player in players:
            if type(player) is Player:
                playerAmount += 1
            else:
                imposterAmount += 1
        
        compostition[0]= playerAmount
        compostition[1]= imposterAmount
        return compostition

    #createDataPoint creates a datapoint object for data analysis
    def createDataPoint( self , imposterVictory):
        
        newDataPoint = DataPoint(imposterVictory , len(self.players) , self.checkPlayerCompistion(self.players))
        
        return newDataPoint


        