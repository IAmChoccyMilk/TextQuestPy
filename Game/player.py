import json
import cmd
import textwrap
import sys
import os
import time
import random

##### Player stuff ######
class Player:
    def ___init___(self):
        self.name = ''
        self.hp = 0
        self.mp = 0
        self.level = 0
        self.player_class = ''
        self.status_effects = []
        
    # Attributes of the player
    # playerName = None
    # playerLevel = None
    # playerHP = None
    # playerClass = None
    # armorClass = None

    '''
    # Sets the JSON structure for the character files
    playerData = {
    "Player Name": playerName,
    "Class": playerClass,
    "Level": playerLevel,
    "Armor Class": armorClass,
    "Health Points": playerHP,
    }
   

    with open('player.json,' 'w') as f:
    json.dump(playerData, f)'''