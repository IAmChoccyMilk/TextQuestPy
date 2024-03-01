import random
from dice import *
from player import *
class Items():
    def __init__(self, name, description, value, rarity):
        self.item_name = name
        self.item_description = description
        self.item_value = value
        self.item_can_equip = False
        self.item_armor = 0
        self.item_damage = 0
        self.item_rarity = rarity
        self.item_effect = []
        
    def __str__(self):
        return "{}\n============\n{}\nValue: {}\nRarity: {}\n".format(self.item_name, self.item_rarity, self.item_description, self.item_value)
        
    
class Weapon(Items):
    def __init__(self, name, description, damage, value, rarity):
        self.damage = damage
        super().__init__(name, description, value, rarity)
        
    def __str__(self):
        return "{}\n============\n{}\nValue: {}\nDamage {}".format(self.item_name, self.item_description, self.item_value, self.item_damage)
    
    
class Short_Sword(Weapon):
    def __init__(self):
        super().__init__(name="Short Sword",
                         rarity='common',
                         description="'Arguably the most reliable weapon in any soldiers armory. A sturdy and sharp blade paired with a comfortable grip and an almost perfect weight balance to match.'",
                         value=random.randint(6, 14),
                         damage=6)
        
        
class Gold(Items):
    def __init__(self, amount):
        self.amount = amount
        super().__init__(name="Gold Coins", 
                         description="'A gold coin so shiny you can make out the pimple on your nose.'".format(str(self.amount)),
                         value=self.amount,
                         rarity=None)
    
print(Short_Sword())