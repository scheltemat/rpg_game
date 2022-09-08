
from random import randint

class Character:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power
        self.alive = True
        self.armor = 0 
        self.evade = 0 
        self.inventory = {}
        
    def attack(self, enemy):
        
        if enemy.evade == 0:
            enemy.health -= max(0, self.power - enemy.armor)
            print(f"{self.name} does {self.power} damage to the {enemy.name}. \n")
            
        elif enemy.evade == 2:
            r = randint(1,10)
            if r == 1:
                print(f"The {self.name}'s attack missed the {enemy.name}!")
            else:
                enemy.health -= max(0, self.power - enemy.armor)
                print(f"{self.name} does {self.power} damage to the {enemy.name}. \n")
        elif enemy.evade == 4:
            r = randint(1, 20)
            if r < 4:
                print(f"The {self.name}'s attack missed the {enemy.name}!")
            else:
                enemy.health -= max(0, self.power - enemy.armor)
                print(f"{self.name} does {self.power} damage to the {enemy.name}. \n")
        elif enemy.evade == 6: 
            r = randint(1,5)
            if r == 1:
                print(f"The {self.name}'s attack missed the {enemy.name}!")
            else:
                enemy.health -= max(0, self.power - enemy.armor)
                print(f"{self.name} does {self.power} damage to the {enemy.name}. \n")
        elif enemy.evade == 8:
            r = randint(1,4)
            if r == 1:
                print(f"The {self.name}'s attack missed the {enemy.name}!")
            else:
                enemy.health -= max(0, self.power - enemy.armor)
                print(f"{self.name} does {self.power} damage to the {enemy.name}. \n")
            
    
        
        
    # def alive(self):
    #     if self.health > 0:
    #         return True
    #     else:
    #         return False
    
    def print_status(self):
        if self.alive:
            print(f"{self.name} has {self.health} health, {self.power} power, and {self.armor} armor.")
        else:
            print(f"{self.name} has died.")
            

class Hero(Character):
    def __init__(self, name, health, power):
        super(Hero,self).__init__(name, health, power)
        self.currency = 100
        self.inventory = {}
        
    def attack(self, enemy):
        
        if not isinstance(enemy, Shadow):
            crit = randint(1,5)
            if crit == 1:
                enemy.health -= (self.power * 2)
                print("You've landed a critical hit!")
                print(f"{self.name} does {self.power * 2} damage to the {enemy.name}. \n")
                self.power = 5
            else:
                enemy.health -= max(0, self.power - enemy.armor)
                print(f"{self.name} does {self.power} damage to the {enemy.name}. \n")
        else:
            enemy.noDamage(self)
        


class Shadow(Character):
    def __init__(self, name, health, power):
        super(Shadow,self).__init__(name, health, power)
        self.bounty = 7
        
    def noDamage(self, enemy):
        chance = randint(1,10)
        if chance == 1:
            self.health -= enemy.power
            print(f"{enemy.name} does {enemy.power} damage to the {self.name}")
        else:
            print(f"{enemy.name} does no damage to the {self.name}!")
        
                 
class Goblin(Character):
    def __init__(self, name, health, power):
        super(Goblin,self).__init__(name, health, power)
        self.bounty = 5


class Medic(Character):
    def __init__(self, name, health, power):
        super(Medic,self).__init__(name, health, power)
        self.bounty = 4
        
    def regenerate(self):
        r = randint(1,5)
        if r == 1:
            self.health += 2
            print(f"The {self.name} has regenerated 2 health!")
                    

class Zombie(Character):
    def __init__(self, name, health, power):
        super(Zombie,self).__init__(name, health, power)
        self.bounty = 10
        self.inventory = {}
    
    def alive(self):
        if self.inventory.get('Zombicide', 0) > 0:
            return False
        else:
            return True

    
class Theif(Character):
    def __init__(self, name, health, power):
        super(Theif,self).__init__(name, health, power)
        self.bounty = 5
        
    def attack(self, enemy):
        chance = randint(1,5)
        if chance == 1:
            enemy.currency -= 1
            self.bounty += 1
            print(f"The {self.name} has stolen a coin from {enemy.name}!")
        else:
            enemy.health -= max(0, self.power - enemy.armor)
            print(f"{self.name} does {self.power} damage to the {enemy.name}. \n")
            
class FinalBoss(Character):
    def __init__(self, name, health, power):
        super(FinalBoss,self).__init__(name, health, power)
        self.bounty = 100
        
    def attack(self, enemy):
        enemy.health -= 0
        print(f"The {self.name} just wants a burger.")
        
        
def mainMenu():
    print(f"""
        \n
        -----------------------
        What do you want to do?
        1. Go to store
        2. Look for an enemy
        3. Fight Final Boss
        4. End game
        -----------------------
        """)

def shopMenu(hero):
    print(f"""
        \n
        -----------------------
        What would you like to purchase?
        1. Super Tonic - 15 coins
        2. Armor - 20 coins
        3. Evade - 25 coins
        4. Zombicide - 50 coins
        5. Burger - 1 coin
        6. Leave
        
        You currently have {hero.currency} coins.
        -----------------------
        """)

def fight_menu(enemy):
    print(f"""
        \n
        -----------------------
        What do you want to do?
        1. fight {enemy.name}
        2. use SuperTonic
        3. use Zombicide
        4. do nothing
        5. flee
        -----------------------
        """)

def finalBossMenu(enemy):
    print(f"""
        \n
        -----------------------
        What do you want to do?
        1. fight {enemy.name}
        2. do nothing
        3. flee
        4. use Burger
        -----------------------
        """)


def goToStore(hero):
            
    print(f"Welcome to H-E-B.")
    
    while True: 
        shopMenu(hero)
        
        selection = input()
        if selection == '1': # SuperTonic
            if hero.currency >= 15:
                print("Nice!")
                hero.currency -= 15
                hero.inventory["SuperTonic"] = hero.inventory.get("SuperTonic", 0) + 1
            else:
                print(f"You do not have enough coins!")
        elif selection == '2': # Armor
            if hero.currency >= 20:
                hero.currency -= 20
                hero.armor += 2
                print(f"Good for you! Your armor is now {hero.armor}")
            else:
                print(f"You do not have enough coins!")
                
        elif selection == '3': # Evade
            if hero.currency >= 25:
                if hero.evade == 8:
                    print("You cannot purchase any more Evade!")
                else:
                    hero.currency -= 25
                    hero.evade += 2
                    print(f"Neato! Your Evade is now {hero.evade}")
            else:
                print(f"You do not have enough coins!")
                
        elif selection == '4': # Zombicide
            if hero.currency >= 50:
                hero.currency -= 50
                hero.inventory["Zombicide"] = hero.inventory.get("Zombicide", 0) + 1
            else:
                print(f"You do not have enough coins!")
                
        elif selection == '5': # Burger
            if hero.currency >= 1:
                hero.currency -= 1
                hero.inventory["Burger"] = hero.inventory.get("Burger", 0) + 1
                print(f"Hero has purchased a burger... for some reason")
            else:
                print(f"You do not have enough coins!")
        elif selection == '6':
            break
        else:
            print(f"Invalid input {selection}")
            
        keepShopping = input("Do you want to keep shopping? y/n ")
        if keepShopping == 'n':
            break
        elif keepShopping == 'y':
            pass
        else:
            print(f"Invalid input {keepShopping}")

def combat(enemy, hero):
            
    print(f"You've encountered a {enemy.name}.")
    
    while enemy.alive and hero.alive:
        fight_menu(enemy)
        raw_input = input()
        if raw_input == '1': # hero attacks and then the enemy attacks back
            hero.attack(enemy)
            if not isinstance(enemy, Zombie) and enemy.health <= 0:
                enemy.alive = False
            if isinstance(enemy, Medic):
                enemy.regenerate()
            hero.print_status()
            enemy.print_status()
            print("")
            
            if enemy.alive:
                enemy.attack(hero)
                if hero.health <= 0:
                    hero.alive = False
                enemy.print_status()
                hero.print_status()
            else:
                hero.currency += enemy.bounty
                print(f"You found {enemy.bounty} coins!")
                print(f"You now have {hero.currency} coins.")
        
        elif raw_input == '2': # hero uses a super tonic item
            
            if hero.inventory.get('SuperTonic', 0) > 0:
                hero.health += 10
                hero.inventory["SuperTonic"] -= 1
                print(f"Hero used SuperTonic! You now have {hero.health} health!")
                
                # if enemy.alive():
                enemy.attack(hero) 
                if hero.health <= 0:
                    hero.alive = False
                enemy.print_status()
                hero.print_status()
            else:
                print("You do not have a SuperTonic!")
        
        elif raw_input == '3': # hero uses zombicide item
            if hero.inventory.get('Zombicide', 0) > 0:
                if isinstance(enemy, Zombie):
                    enemy.inventory["Zombicide"] = enemy.inventory.get("Zombicide", 0) + 1
                    hero.inventory.get("Zombicide", 0) - 1
                    hero.currency += enemy.bounty
                    enemy.alive = False
                    print(f"Hero used Zombicide to kill the Zombie!")
                    print(f"You found {enemy.bounty} coins!")
                    print(f"You now have {hero.currency} coins.")
                    
                else:
                    print("You cannot use Zombicide on this enemy!")        
                
            else:
                print("You do not have a Zombicide!")
        
        elif raw_input == '4': # hero does nothing but enemy attacks anyways
            # if enemy.alive():
            enemy.attack(hero)
            if hero.health <= 0:
                hero.alive = False
            enemy.print_status()
            hero.print_status()
                
        elif raw_input == '5': # hero attempts to escape
            q = randint(1,5)
            if q == 1:   
                print(f"{hero.name} escaped, but barely!")
                break
            else:
                print(f"{hero.name} failed to escape!")
                if hero.health <= 0:
                    hero.alive = False
                enemy.attack(hero)
                enemy.print_status()
                hero.print_status()
                
        else:
            print(f"Invalid input {raw_input}")  
    
def finalBoss(enemy, hero):
    
    print(f"You've encountered the {enemy.name}!")
    
    while enemy.alive and hero.alive:
        finalBossMenu(enemy)
        raw_input = input()
        if raw_input == '1': # hero attacks and then the enemy attacks back
            hero.attack(enemy)
            if not isinstance(enemy, Zombie) and enemy.health <= 0:
                enemy.alive = False
            if isinstance(enemy, Medic):
                enemy.regenerate()
            hero.print_status()
            enemy.print_status()
            print("")
            
            if enemy.alive:
                enemy.attack(hero)
                if hero.health <= 0:
                    hero.alive = False
                enemy.print_status()
                hero.print_status()
            else:
                hero.currency += enemy.bounty
                print(f"You found {enemy.bounty} coins!")
                print(f"You now have {hero.currency} coins.")
                
        elif raw_input == '2':
            enemy.attack(hero)
            if hero.health <= 0:
                hero.alive = False
            enemy.print_status()
            hero.print_status()
            
        elif raw_input == '3':
            q = randint(1,5)
            if q == 1:   
                print(f"{hero.name} escaped, but barely!")
                break
            else:
                print(f"{hero.name} failed to escape!")
                enemy.attack(hero)
                enemy.print_status()
                hero.print_status()
                
        elif raw_input == '4':
            if hero.inventory.get('Burger', 0) > 0:
                enemy.inventory["Burger"] = enemy.inventory.get("Burger", 0) + 1
                hero.inventory.get("Burger", 0) - 1
                print(f"Hero has given the final boss a Burger! He is no longer hangry and the players are free from this never ending hellscape!!!")
                print("""
                        ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
                        ███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀
                        ██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼
                        ██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀
                        ██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼
                        ███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄
                        ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
                        ███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼
                        ██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼
                        ██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼
                        ██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼
                        ███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄
                        ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼""")
                quit()
            else:
                print("You do not have a burger!")
                
        else:
            print(f"Invalid input {raw_input}")
        

def generateEnemy():
    randEnemy = randint(1,5)
    if randEnemy == 1:
        opponent = Goblin("Goblin", 6, 2)
    elif randEnemy == 2:
        opponent = Shadow("Shadow", 1, 1)
    elif randEnemy == 3:
        opponent = Zombie("Zombie", 3, 1)
    elif randEnemy == 4:
        opponent = Medic("Medic", 6, 1)
    else:
        opponent = Theif("Theif", 10, 1)
    return opponent

def main():
    
    hero = Hero("Hero", 10, 5)
    
    while hero.alive:
    
        mainMenu()
        choice = input()
        if choice == '1':
            goToStore(hero)
            
        elif choice == '2':
            opponent = generateEnemy()
            combat(opponent, hero)
        
        elif choice == '3':
            enemy = FinalBoss("Final Boss", float('inf'), 69)
            finalBoss(enemy, hero)
           
        elif choice == '4':
            break 
        
        else:
            print(f"Invalid input {choice}")
            mainMenu()


    print("""
                    ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
                    ███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀
                    ██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼
                    ██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀
                    ██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼
                    ███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄
                    ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
                    ███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼
                    ██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼
                    ██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼
                    ██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼
                    ███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄
                    ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼""")

main()
