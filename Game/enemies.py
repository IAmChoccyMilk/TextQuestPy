class Enemy:
    def __init__(self, name, hp, damage):
        """Creates new enemy
        
        :name: the name of the enemy
        :hp: the health points of the enemy
        :damage: the damage the enemy will deal
        """
        
        self.name = name
        self.hp = hp
        self.damage = damage
        
    def is_alive(self):
        return self.hp > 0
    
class GiantSpider(Enemy):
    def __init__(self):
        super().__init__(name="Giant Spider",
                         hp=10,
                         damage=3)
        
class Goblin(Enemy):
    def __init__(self):
        super().__init__(name="Goblin",
                         hp=16,
                         damage=15)
        
class Ogre(Enemy):
    def __init__(self):
        super().__init__(name="Ogre",
                         hp=40,
                         damage=25)