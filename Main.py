"""
James Hendry
Version 0.2 Beta
The main class used as the interface between the user
and the program
"""
from mimetypes import init
from select import select
from tkinter import Menu
from turtle import right
from Simulation import Simulation

class Main:
    isRunning = False
    #weewoo = Simulation(2)
    
    def __init__(self) -> None:
        self.menu( )
        pass

    

    def menu( self ):
        isRunning = True
        selectedOption = 0
        gottenValues = []

        while isRunning == True:
            selectedOption = int(self.displayMenuItems())
            if selectedOption == 1:
                gottenValues = self.getSimulationVariables()
                self.__runSimulation(gottenValues[0], gottenValues[1] , str(gottenValues[2]) )
            else:
                isRunning = False


            
        """
        Put menu interface here
        """
    
    def __runSimulation( self , amountOfTimes , amountOfPlayers , fileName):
        simulations = Simulation( amountOfTimes , amountOfPlayers , fileName)

    def displayMenuItems( self ):
        
        print("This is a data collection simulation about randomly yeeting people in Amongus")
        print("Press" + "\n1 for Simulation"+"\n2 or any other key to quit")
        
        return input()
    
    def getSimulationVariables( self ):
        variables = []
        rightInputType = False

        print("O.k Random Yeet Amongus Simulation in Progress")
        if int(input("do you want to Start" + "\nPress 1 to start" + "\nOr Any other key to quit\n")) == 1:
            while rightInputType is False:
                variables.append( int(input( "How many games do you want to Simulate\n" ) ) )
            
                variables.append( int(input( "How many players do you want to Simulate\n") ) )
            
                variables.append( input( "What do you want the Excel file to be called?\n"))

                if type(variables[0]) == int and type(variables[1]) == int:
                    return variables
                else:
                    print(" Incorrect Input"+"\nThe \"How many\" question need an answer that is an interger")
                    variables.clear()
    
    #----------------
start = Main()


    





    