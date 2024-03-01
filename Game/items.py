import random
import player
class Items():
    def __init__(self, name, description, value, rarity, type_of_item):
        
        self.item_Name = name
        self.item_Desc = description
        self.item_value = value
        self.item_rarity = rarity
        self.item_type = type_of_item
        
    def __str__(self):
        return "{}\n=====================\n{}\nValue: {}\nRarity: {}\nType: {}".format(self.item_Name, self.item_Desc, self.item_value, self.item_rarity, self.item_type)
    
class GoldCoin(Items):
    def __init__(self, amount):
        self.amount = amount
        super().__init__(name='Gold Coins',
                         description='A shiny gold coin! Looks valuable',
                         value=self.amount,
                         rarity='common',
                         type_of_item='Currency')
class Weapon(Items):
    def __init__(self, name, description, value, rarity, damage_dice, type_of_item, hit_dice):
        self.damage_dice = damage_dice
        self.hit_dice = hit_dice
        super().__init__(name, description, value, rarity, type_of_item)
        
    def __str__(self):
        return "{}\n=============\n{}\nValue: {}\nDamage Dice: {}\nDamage Type: {}".format(self.item_Name, self.item_Desc, self.item_value, self.hit_dice, self.item_type)

class Dagger(Weapon):
    def __init__(self):
        super().__init__(name='Dagger', 
                         description='"Like a short sword, but... short...er."',
                         value=random.randint(4,10),
                         rarity='common',
                         damage_dice=random.randint(1, 6),
                         hit_dice='1d6'
                         type_of_item='Piercing'
                        )
        
    def roll_dice():
        damage = Dagger().damage_dice + player.Player().strength / 3
        return int(damage)

class ShortSword(Weapon):
    def __init__(self):
        super().__init__(name='Short Sword',
                         description='Arguably the most reliable weapon in any soldiers armory. A sturdy and sharp blade paired with a comfortable grip and an almost perfect weight balance to match.',
                         value=random.randint(8, 14),
                         rarity='common',
                         damage_dice=random.randint(1, 12),
                         hit_dice='1d12',
                         type_of_item='Slashing/Piercing')
        
    def roll_dice():
        damage = ShortSword().damage_dice + player.Player().strength / 3
        return int(damage)
    
class Armor(Items):
    def __init__(self, name, description, value, rarity, armor_class_bonus, type_of_item):
        self.armor_bonus = armor_class_bonus
        super().__init__(name, description, value, rarity, type_of_item)
        
class LeatherArmor(Armor):
    def __init__(self):
        super().__init__(name='Leather Armor', 
                         description='"A set of light leather armor. It may not protect as much as a set of chainmail or bronze, but at least I can still run."',
                         rarity='common',
                         value=random.randint(5, 11),
                         armor_class_bonus=2,
                         type_of_item='Armor')
        
    
        