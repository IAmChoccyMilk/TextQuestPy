import cmd
import textwrap
import sys
import os
import time
import random
from player import *
'''
a1 a2...  #PLAYER STARTS AT a1
######### 
|_|_|_|_| a4...
|_|_|_|_| b4...
|_|_|_|_| c4...
|_|_|_|_| d4...
#########
'''
ZONENAME = ''
DESCRIPTION = 'description'
EXAMINATION = 'examine'
SOLVED = False
UP = 'up', 'north', 'n'
DOWN = 'down', 'south', 's'
LEFT = 'left', 'west', 'w'
RIGHT = 'right', 'east', 'e'

solved_places = {'a1': False, 'a2': False, 'a3': False, 'a4': False,
                 'b1': False, 'b2': False, 'b3': False, 'b4': False,
                 'c1': False, 'c2': False, 'c3': False, 'c4': False,
                 'd1': False, 'd2': False, 'd3': False, 'd4': False}

zoneMap = {
    'a1': {
        ZONENAME: "The Otherworldly Inn",
        DESCRIPTION:  'This is the inn in which you are currently staying at. Your room is small, but cozy. A fireplace resting in the back wall illuminates your room with a comforting glow and the scent of sweet cranberries fill your nose.',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: '',
        DOWN: 'b1',
        LEFT: '',
        RIGHT: 'a2'
    },
    'a2': {
        ZONENAME: "Alvarian Square",
        DESCRIPTION:  'The center of the city of Alavaria. You can see market stalls, shops, eateries, and of course the Anomaly itself taking the center spotlight. crowds of people go about their day and incoherent chatter from many different conversations fill your ears. Quite stimulating isnt it.',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: '',
        DOWN: 'b2',
        LEFT: 'a1',
        RIGHT: 'a3'
    },
    'a3': {
        ZONENAME: "The Slums",
        DESCRIPTION:  'The smell of garbage and dew fill your nose. The building become darker as the soot gradually grabs at the decrepit building around you. You continue to walk until you find yourself surrounded by small beaten houses and large worn tenaments; Thick black smoke slowly rises into the sky from the many chimneys; darkening the sky. You would think this place was cursed by a God.',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: '',
        DOWN: 'b3',
        LEFT: 'a2',
        RIGHT: 'a4'
    },
    'a4': {
        ZONENAME: "Alavarian Eastern Outskirts",
        DESCRIPTION:  'The building get smaller and fewer between until you find yourself at a broken wooden bridge. You look across the bridge to see wilderness. A quiet dark forest. The only way is back where you came from.',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: '',
        DOWN: '', #Will be b4
        LEFT: 'a3',
        RIGHT: ''
    },
    'b1': {
        ZONENAME: "The Forest of Old - North East",
        DESCRIPTION:  'The forest is said to hold treasure of some kind, though, no one has had any luck yet. It is rumored a Goblin ship crashed in this forest decades ago, causing them to infest it. Many adventurers tell stories of the goblins they have slain, and the loot they have brought back from the goblin stockpiles and caves.',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'a1',
        DOWN: '', # will be c1
        LEFT: '',
        RIGHT: 'b2'
    },
    'b2': {
        ZONENAME: "The Forest of Old - North",
        DESCRIPTION:  'The forest is said to hold treasure of some kind, though, no one has had any luck yet. It is rumored a Goblin ship crashed in this forest decades ago, causing them to infest it. Many adventurers tell stories of the goblins they have slain, and the loot they have brought back from the goblin stockpiles and caves.',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'a2',
        DOWN: '', # will be c1
        LEFT: 'b1',
        RIGHT: '' # will be b3
    },
    
}

