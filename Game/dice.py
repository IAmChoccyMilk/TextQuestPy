import random

class Die():
    
    def d20(result):
        sides = 20
        
        def roll():
            result = random.randint(1, sides)
            return result
        
        result = roll()
        return result

    def d12(sides):
        sides = 12
        
        def roll():
            result = random.randint(1, sides)
            return result
        
        result = roll()
        return result
        
    def d10(sides):
        sides = 12
        
        def roll():
            result = random.randint(1, sides)
            return result
        
        result = roll()
        return result
        
    def d8(sides):
        sides = 8
        
        def roll():
            result = random.randint(1, sides)
            return result
        
        result = roll()
        return result
        
    def d6(sides):
        sides = 6
        
        def roll():
            result = random.randint(1, sides)
            return result

        result = roll()
        return result
        
    def d4(sides):
        sides = 4
        
        def roll():
            result = random.randint(1, sides)
            return result

        result = roll()
        return result
        
die_dict = {
    
    'd20': {
        Die().d20()
    },
    'd12': {
        Die().d12()
    },
    'd10': {
        Die().d10()
    },
    'd8': {
        Die().d8()
    },
    'd6': {
        Die().d6()
    },
    'd4': {
        Die().d4()
    }
    
    
}

rolled_die = int(next(iter(die_dict['d20'])))

print(2 * rolled_die)
