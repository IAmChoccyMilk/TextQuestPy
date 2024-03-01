import json
import cmd
import textwrap
import sys
import os
import time
import random
import items, realm
from items import *
import pickle

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
        self.location_x, self.location_y = realm.starting_position
        self.game_over = False
        self.backpack = [items.Gold(10), items.Short_Sword()]
        self.equipped_items = []
    
    def is_alive(self):
        return self.hp > 0

        
    def do_action(self, action, **kwargs):
        action_method = getattr(self, action.method.__name__)
        if action_method:
            action_method(**kwargs)
            
    def print_backpack(self):
        for item in self.backpack:
            print(items, '\n')
            
    def move(self, dx, dy):
        self.location_x += dx
        self.location_y += dy
        print(realm.room_exists(self.location_x, self.location_y).intro_txt)

    def move_north(self):
        self.move(dx=0, dy=-1)
        
    def move_south(self):
        self.move(dx=0, dy=1)
        
    def move_east(self):
        self.move(dx=1, dy=0)
    
    def move_west(self):
        self.move(dx=-1, dy=0)
        
    def attack(self, enemy):
        best_weapon = None
        max_damage = 0
        for i in self.backpack:
            if isinstance(i, items.Weapon):
                if i.damage > max_damage:
                    max_damage = i.damage
                    best_weapon = i
                    
        print("You use {} again {}!".format(best_weapon.item_name, enemy.name))
        enemy.hp -= best_weapon.item_damage
        if not enemy.is_alive():
            print("You killed {}!".format(enemy.name))
        else:
            print("{} HP is {}.".format(enemy.name, enemy.hp))
            
    def flee(self, room):
        """Moves the player randomly to an adjacent room"""
        available_moves = room.adjacent_moves()
        r = random.randint(0, len(available_moves) - 1)
        self.do_action(available_moves[r])
        
    def save_and_exit(self):
        pickle.dump(self, open( "saved_player.p", "wb" ))
        pickle.dump(realm._world, open( "saved_realm.p", "wb" ))
        print("Game saved!")
        exit()
        
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