import json

class Player:
    
    # Attributes of the player
    playerName = None
    playerLevel = None
    playerHP = None
    playerClass = None
    armorClass = None

    # Sets the JSON structure for the character files
    playerData = {
    "Player Name": playerName,
    "Class": playerClass,
    "Level": playerLevel,
    "Armor Class": armorClass,
    "Health Points": playerHP,
    }
    
    def CreateCharacter(self):
        playerName = input().title()
        

playerClasses = {
    
}


    
'''with open('player.json,' 'w') as f:
    json.dump(playerData, f)'''
