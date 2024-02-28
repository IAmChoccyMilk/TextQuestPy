import cmd
import textwrap
import sys
import os
import time
import random
from map import *
from player import *


myPlayer = Player()

screen_width = 100

gameStarted = False

# Prints menu options
def MakeMenuOptions():
    os.system('cls')
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
    print("                                (C)reate new character                           ")
    print("                                (H)elp menu                                      ")
    print("                                (Q)uit                                         \n")
    print("                   Copyright 2024 - @IAmChoccyMilk. All rights reserved.         ")
    
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
            inputValid = True
        case "Q":
            sys.exit()
        case _:
            print("Invalid command, please try again.")
            inputValid = False

# Starts game.
def StartGame():
    setup_game()

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
 

##### Game Interactivity #####
def print_location():
    print('\n' + ('#' * (4 + len(myPlayer.player_location))))
    print('#' + myPlayer.player_location.upper() + '#')
    print('#' + zoneMap[myPlayer.player_location] [DESCRIPTION] + '#')
    print('\n' + ('#' * (4 + len(myPlayer.player_location))))
    
    # Handles all actions and commands
def prompt():
    print("===================================")
    print("What would you like to do?")
    action = input("> ")
    acceptable_actions = ['move', 'go', 'travel', 'walk', 'quit', 'inspect', 'interact', 'look']
    while action.lower() not in acceptable_actions:
        print("You, dont know how to do that, please try again.\n")
        action = input("> ")
    if action.lower() == 'quit':
        sys.exit()
    elif action.lower() in ['move', 'go', 'travel', 'walk']:
        player_move(action.lower())
    elif action.lower() in ['examine', 'inspect', 'interact', 'look']:
        player_examine(action.lower())
        
    # Defines the move action
def player_move(myAction):
    ask = "Where would you like to go?"
    destination = input(ask)
    if destination in ['north', 'up', 'n']:
        destination = zoneMap[myPlayer.player_location] [UP]
        movement_handler(destination)
    elif destination in ['east', 'right', 'e']:
        destination = zoneMap[myPlayer.player_location] [RIGHT]
        movement_handler(destination)
    elif destination in ['south', 'down', 's']:
        destination = zoneMap[myPlayer.player_location] [DOWN]
        movement_handler(destination)
    elif destination in ['west', 'left', 'w']:
        destination = zoneMap[myPlayer.player_location] [LEFT]
        movement_handler(destination)
    
    # Actually moves the player
def movement_handler(destination):
    if myPlayer.player_location == '':
        myPlayer.player_location = 'a1'
    else:
        print("\n" + "You have arrived at " + destination)
        myPlayer.player_location = destination
        print_location()

    
    # Defines the examine action
def player_examine(action):
    if zoneMap[myPlayer.player_location] [SOLVED] == True:
        print("You have already explored this zone.")
    else:
        print("Thing here")
        


##### DEFINE MAIN GAMELOOP #####
def main_game_loop():
    while myPlayer.game_over == False:
        prompt()
    # Here handle if puzzles have been solved/Bosses defeated/explored everything/etc.
    

def setup_game():
    os.system("cls")
    
    ### Name collection
    question1 = "What is your characters name?\n"
    for character in question1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player_name = input('> ')
    myPlayer.name = player_name
    ### Class collection
    question2 = "What is your characters class?\n"
    for character in question2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.02)
    question2continued = "(The current choices are: barbarian, wizard, and rogue)\n"
    for character in question2continued:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    playerClass = input('> ')
    valid_player_classes = ['barbarian', 'wizard', 'rogue']
    if playerClass in valid_player_classes:
        myPlayer.player_class = playerClass
        print(f"Ah, a {playerClass}. A wise choice indeed!\n")
    while playerClass.lower() not in valid_player_classes:
        playerClass = input('> ')
        if playerClass in valid_player_classes:
            myPlayer.player_class = playerClass
            print(f"Ah, a {playerClass}. A wise choice indeed!\n")
            
    if myPlayer.player_class is 'barbarian':
        myPlayer.hp = 120
        myPlayer.mp = 20
        myPlayer.strength = 14
    elif myPlayer.player_class is 'wizard':
        myPlayer.hp = 40
        myPlayer.mp = 120
        myPlayer.strength = 8
    elif myPlayer.player_class is 'rogue':
        myPlayer.hp = 60
        myPlayer.mp = 50
        myPlayer.strength = 10
        
    ### Introduction
    question3 = "Welcome " + player_name + " the " + playerClass + "!\n"
    for character in question3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
        
    speech1 = "Welcome to the world of Slavaria!\n"
    speech2 = f"More specifically, the city of Alavaria! We have been waiting for you. The Anomaly seems to think highly of you {player_name}. Better get going!\n"
    for character in speech1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.06)
    for character in speech2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.04)
    
    os.system('cls')
    print("#############################")
    print("     Welcome to Alavaria!    ")
    print("#############################")
    main_game_loop()
          
        
MakeMenu()