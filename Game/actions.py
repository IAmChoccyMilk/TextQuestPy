from player import Player

class Action():
    """Base for all actions"""
    def __init__(self, method, name, hotkey, **kwargs):
        """Creates a new action
        
        :method: = the function object to execute
        :name: = the name of the action
        :ends_turn: = True if the player is expected to move after this action else False
        :hotkey: = The keyboard key the playe should use to initiate the action
        """
        
        self.method = method
        self.name = name
        self.hotkey = hotkey
        self.kwargs = kwargs
        def __str__(self):
            return "{}: {}".format(self.hotkey, self.name)
        
class MoveNorth(Action):
    def __init__(self):
        super().__init__(method=Player.move_north,
                         name='Move North', hotkey='n')
        
class MoveSouth(Action):
    def __init__(self):
        super().__init__(method=Player.move_south,
                         name='Move South', hotkey='s')
        
class MoveEast(Action):
    def __init__(self):
        super().__init__(method=Player.move_east,
                         name='Move East',
                         hotkey='e')

class MoveWest(Action):
    def __init__(self):
        super().__init__(method=Player.move_west,
                         name='Move West',
                         hotkey='w')
        
class ViewBackpack(Action):
    """Prints all items in the players backpack"""
    def __init__(self):
        super().__init__(method=Player.print_backpack,
                         name='View Backpack',
                         hotkey='tab')
        
class Attack(Action):
    def __init__(self, enemy):
        super().__init__(method=Player.attack,
                         name='Attack',
                         hotkey='a')
        
class Flee(Action):
    def __init__(self, room):
        super().__init__(method=Player.flee,
                         name='Flee',
                         hotkey='f',
                         room=room)
        
class SaveAndExit(Action):
    def __init__(self):
        super().__init__(method=Player.save_and_exit,
                         name='Save and Exit',
                         hotkey='esc')