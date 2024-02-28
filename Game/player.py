import json
import cmd
import textwrap
import sys
import os
import time
import random

##### Player stuff ######
class Player:
    def __init__(self):
        self.name = ''
        self.hp = 0
        self.mp = 0
        self.xp = 0
        self.strength = 0
        self.level = 0
        self.player_class = ''
        self.status_effects = []
        self.player_location = 'a1'
        self.game_over = False
        self.backpack = []
        self.equipped_items = []
        self.gold = 0

        
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