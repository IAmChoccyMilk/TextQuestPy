import random

gameStarted = False

def MakeMenuOptions():
    print("(S)tart new game\n")
    print("(L)oad game\n")
    print("(C)reate new character\n\n\n")
    

def MakeMenu():
    
    MakeMenuOptions()
    
    inputValid = False
    
    menuInput = input()
        
    match menuInput.title():
        case "S":
            StartGame()
            inputValid = True
        case "L":
            print("Sorry, this feature is still a work in progress!")
            inputValid = False
        case "C":
            print("Sorry, this feature is still a work in progress.")
            inputValid = False
        case _:
            print("invalid input, please try again.")
            inputValid = False

# Starts game.
def StartGame():
    pass
    
# Opens menu of existing characters and allows user to select one of them to continue
def LoadGame():
    pass

# Allows the user to create a character without starting a new game afterward
def CreateCharacter():
    pass
    
while True:
    
    # Makes menu screen
    MakeMenu()
    
                