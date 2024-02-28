from player import *
import random
from engine import *

class Events():
    
    
    
    def found_gold():
        # list of possible outcomes
        eat_list = ['You bite into the coin and break a tooth. You lose 3HP', 'You eat the coin and swallow it whole. Thats gonna hurt later.']
        
        interaction1 = "You see a coin purse on the ground! What would you like to do?"
        for character in interaction1:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.04)
        interaction1Added = "actions: take, ignore, "
        for character in interaction1Added:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.02)
        choice = input('> ')
        valid_choices = ['take', 'pick up', 'eat', 'consume', 'ignore']
        if choice not in valid_choices:
            print("You cant do that! Do something else.")
        elif choice == 'take' or 'pick up':
            Player().gold += random.randint(1, 6)
        elif choice == 'eat' or 'consume':
            result1 = random.choice(eat_list)
            if result1 == eat_list[0]:
                Player().hp -= 3
        elif choice == 'ignore':
            result2 = "You leave the coin purse on the ground and continue walking."
            for character in result2:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.04)
    
    def Odd_Trader():
        interaction1 = "A shady figure wearing a black cloak approaches you. You can see a dim glow from pieces of jewelry that hang on a string from his neck."
        for character in interaction1:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.04)
        trader_speech1 = "You look like you could use some goods, and I could use some gold. So why dont you browse my wares?"
        for character in trader_speech1:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.04)
        trader_speech1Added = "actions: 'wares', 'ignore'"
        for character in trader_speech1Added:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.04)
        choice = input('> ')
        valid_choice = ['wares', 'ignore']
        if choice not in valid_choice:
            print("You cant do that! Do something else.")
        elif choice == 'wares':
            # Put shop function here
            pass
        elif choice == 'ignore':
            trader_speech2 = "I see. I am sure you will browse next time."
            for character in trader_speech2:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.04)
                prompt()
        