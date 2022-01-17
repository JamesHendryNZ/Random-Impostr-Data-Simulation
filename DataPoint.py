"""
James Hendry
Version 0.1 Alpha
DataPoint Class
A class to hold data
"""

class DataPoint:
    imposterVictory = False
    survingPlayers = 0
    survingImposters = 0

    def __init__(self , imposterVictory, survingPlayers , playerComposition):
        self.imposterVictory = imposterVictory
        self.survingPlayers = survingPlayers
        self.survingImposters = playerComposition[1]

    
