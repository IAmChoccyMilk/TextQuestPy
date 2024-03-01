import items
import enemies
import realm
import actions
import random
from player import Player

class MapRoom:
    """The base of a room within the realm"""
    def __init__(self, x, y):
        """Creates a new room
        
        :x: = The x-coordinate of the room
        :y: = The y-coordinate of the room
        """
        
        self.x = x
        self.y = y
        
    def intro_text(self):
        """Information to be printed when the player enters the room"""
        raise NotImplementedError()
    
    def modify_player(self, the_player):
        """Process actions that change the state of the player"""
        raise NotImplementedError()
    
    def adjacent_moves(self):
        """Returns all adjacent rooms"""
        moves = []
        if realm.room_exists(self.x + 1, self.y):
            moves.append(actions.MoveEast())
        if realm.room_exists(self.x - 1, self.y):
            moves.append(actions.MoveWest())
        if realm.room_exists(self.x, self.y - 1):
            moves.append(actions.MoveNorth())
        if realm.room_exists(self.x, self.y + 1):
            moves.append(actions.MoveSouth())
        return moves
    
    def available_actions(self):
        """Returns all available actions"""
        moves = self.adjacent_moves()
        moves.append(actions.ViewBackpack())
        moves.append(actions.SaveAndExit())
        
        return moves

class StartingRoom(MapRoom):
    def intro_text(self):
        return """
        You find yourself blinded as you open your eyes. You can hear drops of liquid tick off the hard ground as it resonates off the walls. The air is cold and damp and it smells musky. You feel around and reach into your backpack to pull out a torch. As the torch light illuminates your way you can now see there are four ways to go.
        """
        
    def modify_player(self, the_player):
        #Room has no action player
        pass

class EmptyCavePath(MapRoom):
    def intro_text(self):
        return """
        Another unremarkable part of the cave. You must forge onwards.
        """

    def modify_player(self, the_player):
        #Room has no action on player
        pass

class ChestRoom(MapRoom):
    """A room that adds items to the players backpack."""
    def __init__(self, x, y, item):
        self.item = item
        super().__init__(x, y)
        
    def add_loot(self, the_player):
        the_player.backpack.append(self.item)
        
    def modify_player(self, the_player):
        self.add_loot(the_player)
        
class FindSwordRoom(ChestRoom):
    
    def __init__(self, x, y):
        super().__init__(x, y, items.Short_Sword())
        
    def intro_text(self):
        return """
        You notice a nice looking short sword inbedded in a corpse. He wont need it anymore after all.
        You pick up the short sword.
        """
        
class FindGoldRoom(ChestRoom):
    def __init__(self, x ,y):
        super().__init__(x, y, items.Gold(random.randint(1, 8)))
        
    def intro_text(self):
        return """
        Someone must of lost some gold pieces. 
        You pick them up!
        """
        
class EnemyRoom(MapRoom):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)

    def modify_player(self, the_player):
        if self.enemy.is_alive():
            the_player.hp = the_player.hp - self.enemy.damage
            print("Enemy does {} damage. You have {} HP remaining.".format(self.enemy.damage, the_player.hp))

    def available_actions(self):
        if self.enemy.is_alive():
            return [actions.Flee(tile=self), actions.Attack(enemy=self.enemy)]
        else:
            return self.adjacent_moves()
        
class GiantSpiderRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.GiantSpider())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            A giant spider jumps down from its web in front of you!
            """
        else:
            return """
            The corpse of a dead spider rots on the ground.
            """
            
class GoblinRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Goblin())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            A goblin hops out from a dark corner. Its an ambush!
            """
        else:
            return """
            The limp corpse of the dead goblin falls on the ground.
            """
            
            
class OgreRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Ogre())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            ... The ground is shaking... oh this cant be good. 
            A huge ogre squeezes through a large opening!
            """
        else:
            return """
            The body of the dead ogre hits the ground with a booming thud.
            """
            
class SnakePitRoom(MapRoom):
    def intro_text(self):
        return """
        You have fallen into a pit of deadly snakes!

        You have died!
        """

    def modify_player(self, player):
        player.hp = 0
        
class LeaveCaveRoom(MapRoom):
    def intro_text(self):
        return """
        You see a bright light in the distance...
        ... it grows as you get closer! It's sunlight!


        You made it out!
        """

    def modify_player(self, player):
        player.game_over = True