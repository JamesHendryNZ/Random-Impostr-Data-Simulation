"""
James Hendry
Version 0.2 Beta
The simluation class which 
simulates many games, collects the results
and exports it has an excel (.xlsx)file
"""
from math import fabs
from random import randint
import random
import pandas
import datetime

from pandas.core.frame import DataFrame
from Game import Game
import openpyxl



class Simulation:
    
    #amountOfTimes= 0
    simulationData= []
    
    #dataCollected = DataPoint[]
    
    def __init__(self , simulations , playerAmount , fileName) -> None:
        self.simulationData = []
        self.simulateGames( simulations , playerAmount , fileName)
        pass

    def simulateGames( self , amountOfGames , playerAmount , fileName):
        counter = 0
        random.seed(int(datetime.datetime.now().second))

        while counter < amountOfGames:
            game = Game( playerAmount )
            self.simulationData.append(game.simulateGame())
            counter += 1
        
        self.exportDataToExcel( self.simulationData , fileName)
        
        print(" Simulations done")
    
    """
    this exports the Data to an excel file
    it will make an excell file
    put all the data from in simulation data and put it in
    If possible, make it make graphs
    do any disconnect IO stuff to end connection.
    """
    def exportDataToExcel( self,  data , fileName ):

        imposterVictories = []
        survingPlayers    = []
        survingImposters  = []

        #fileName = 'randomChoiceImposter.xlsx'

        print(fileName)
        if str(fileName).endswith(".xlsx") is False:
            fileName = fileName + ".xlsx"

        for dataPoint in data:
            imposterVictories.append(dataPoint.imposterVictory)
            survingPlayers.append(dataPoint.survingPlayers)
            survingImposters.append(dataPoint.survingImposters)
        
        dataFrame = pandas.DataFrame(zip(imposterVictories,survingPlayers,survingImposters), columns=["Imposters Win?","Players remaining","Imposters Remaining"])
        
        print(dataFrame)

        with pandas.ExcelWriter( fileName ) as writer:
            dataFrame.to_excel( writer , sheet_name="Yeeted Through Random Choices")

        #----------------------------------------------------------------
    #simulateGames(2)