
import cmd
import textwrap
import sys
import os
import time
import random
from Game.player import Player
screen_width = 100

gameStarted = False

# Prints menu options
def MakeMenuOptions():
    os.system('clear')
    print("#################################################################################")
    print("Welcome to")
    print("_________ _______          _________ _______           _______  _______ _________")
    print("\__   __/(  ____ \|\     /|\__   __/(  ___  )|\     /|(  ____ \(  ____ \\__   __/")
    print("   ) (   | (    \/( \   / )   ) (   | (   ) || )   ( || (    \/| (    \/   ) (   ")
    print("   | |   | (__     \ (_) /    | |   | |   | || |   | || (__    | (_____    | |   ")
    print("   | |   |  __)     ) _ (     | |   | |   | || |   | ||  __)   (_____  )   | |   ")
    print("   | |   | (       / ( ) \    | |   | | /\| || |   | || (            ) |   | |   ")
    print("   | |   | (____/\( /   \ )   | |   | (_\ \ || (___) || (____/\/\____) |   | |   ")
    print("   )_(   (_______/|/     \|   )_(   (____\/_)(_______)(_______/\_______)   )_(   ")
    print("                                                                                 ") 
    print("#################################################################################")           
    print("                                (S)tart new game                                 ")
    print("                                (L)oad game                                      ")
    print("                                (C)reate new character                           \n")
    print("                   Copyright 2024 - @IAmChoccyMilk. All rights reserved.        ")
    
# Makes the menu
def MakeMenu():
    
    MakeMenuOptions()
    
    inputValid = False
    
    menuInput = input("> ")
        
    match menuInput.title():
        case "S":
            StartGame()
            print("YOU DID IT!")
            inputValid = True
        case "L":
            print("Sorry, this feature is still a work in progress!")
            inputValid = False
        case "C":
            print("Sorry, this feature is still a work in progress.")
            inputValid = False
        case "H":
            HelpMenu()
        case "Q":
            sys.exit()
        case _:
            print("Invalid command, please try again.")
            inputValid = False

# Starts game.
def StartGame():
    myPlayer = Player()

def HelpMenu():
    print("                          Help:                                                               ")
    print("                               - Use up, down, left, right to move                                 ")
    print("                               - Type your commands to execute actions                                     ")
    print("                               - Use 'look' to inspect something                           \n")
# Opens menu of existing characters and allows user to select one of them to continue
def LoadGame():
    pass

# Allows the user to create a character without starting a new game afterward
def CreateCharacter():
    pass
    
while True:
    
    # Makes menu screen
    MakeMenu()
    
                