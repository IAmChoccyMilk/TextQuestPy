import random

gameStarted = False

def StartGame():
    print("Are you ready to plunge into the world of Slavaria?\n If so type 'Start' into the console.")
    started = input().title()
    
    if started == "Start":
        print("Enjoy your journey adventurer!")
        gameStarted = True
    elif started != "Start":
        print("Sorry, that isnt right. Please try again.")
        gameStarted = False
        
def GameLoop():
    player = None
    playerHP = 10
    playerLevel = 1
    
    
while True:
    StartGame()