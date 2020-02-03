from termcolor import colored
from Maaaagic import *
from inventory import *
# def space(text,cut):

space = (lambda text , cut: (cut - len(text)) * ' ')
bold = '\033[1m'
end = '\033[0m'

class hero:
    level = 1
    exp = 0
    # status = "Normal"

    def __init__(self , name , health , strength , pow , spd , wpn , mana , inv , magic_set):
        self.name = name
        self.health = health
        self.strength = strength
        self.magical = pow
        self.speed = spd
        self.weapon = wpn
        self.mana = mana
        self.inv = inv
        self.magic_set = magic_set

    def leveling_system(self):
        if self.exp >= 300:
            self.level = 4
        elif self.exp >= 150:
            self.level = 3
        elif self.exp >= 20:
            self.level = 2

        print(self.exp)
        print(self.level)

    def attack(self , enemy):
        if self.level == '2':
            enemy.health -= self.strength + r.randint(3 , 15)
        elif self.level == '3':
            enemy.health -= self.strength + r.randint(5 , 20)
        elif self.level == '4':
            enemy.health -= self.strength + r.randint(7,25)
        else:
            enemy.health -= self.strength + r.randint(0 , 10)

    def magic(self , enemy , sets):
        # enemy.health -= self.magical * r.randint(1 , 3) - 5
        print(f"MANA:{self.mana}\n")
        for i in sets:
            print(i.spell_name)
        print(colored("\nEXIT","red"))
        select = input("Choose: ").title()
        for i in sets:
            if (i.spell_name).startswith(select):
                magic_type(i , self , enemy)
                self.mana -= 10
                break
            elif select.startswith('E'):
                print()
        else:
            print("You don't know that spell")
            self.magic(enemy , sets)

    def inventory(self , inv):

        for k , v in inv.items():
            print(bold + colored(k , "green") , space(k , 15) , colored(v , "red") , end)
        print(colored("\nEXIT","red"))
        choice = input("What do you wanna do? ").lower()
        if choice.startswith("e"):
            print()
        elif choice.startswith("m") and "Mana potion" in inv.keys():
            Mana_potion(self , inv)
            if inv["Mana potion"] <= 0:
                inv.pop("Mana potion")
        elif choice.startswith("h") and "Health potion" in inv.keys():
            HP_potion(self , inv)
            if inv["Health potion"] <= 0:
                inv.pop("Health potion")
        elif choice.startswith("h") and "Health potion" in inv.keys():
            inv["Health potion"] -= 1
            self.health += 100
        elif choice.startswith("w"):
            self.weapon = inv["weapon"]
        else:
            print("You selected nothing \n")
            self.inventory(inv)

    def hero_stuff(self , anti):
        print(f'{bold}{colored("ATTACK" , "red")}{end}'
              f'{space("ATTACK" , 20)}{bold}'
              f'{colored("MAGIC" , "magenta")}{end}'
              f'\n{bold}'
              f'{colored("INVENTORY" , "yellow")}{end}'
              f'{space("INVENTORY" , 20)}{bold}'
              f'{colored("FLEE" , "cyan")}'
              f'{end}')
        a = input("What do you wanna do? ").lower()

        if a.startswith("a"):
            self.attack(anti)

        elif a.startswith("i"):
            self.inventory(self.inv)

        elif a.startswith("m"):
            if self.mana >= 5:
                self.magic(anti , self.magic_set)
            else:
                print("MANA is empty")
                self.hero_stuff(anti)
        else:
            print("Please type a valid answer")
            self.hero_stuff(anti)

def fight(me , evil):
    if evil.name == "The Dark King":
        print("The Unholy Dark King accepts you offer... ")
    else:
        print(f"You stumbled upon a {evil.name}")
    while evil.health > 0 and me.health > 0:
        statistical_damage(evil , statistical_hindering)
        print(f"{me.name}{space(me.name , 20)}HP: {me.health}\n"f"{evil.name}{space(evil.name , 20)}HP: {evil.health}")

        me.hero_stuff(evil)

        evil.att_back(me)
    if me.health <= 0:
        print('''
          ________    _____      _____  ___________   
         /  _____/   /  _  \    /     \ \_   _____/   
        /   \  ___  /  /_\  \  /  \ /  \ |    __)_    
        \    \_\  \/    |    \/    Y    \|        \   
         \______  /\____|__  /\____|__  /_______  /   
                \/         \/         \/        \/    
        ____________   _________________________      
        \_____  \   \ /   /\_   _____/\______   \     
         /   |   \   Y   /  |    __)_  |       _/     
        /    |    \     /   |        \ |    |   \     
        \_______  /\___/   /_______  / |____|_  /     
                \/                 \/         \/      

        ''')


def choose(name , stuff , set):
    print("The classes are Warrior, Mage, Assassin")
    hero_class = input("What Class You wanna choose? ").upper()
    if hero_class.startswith("W"):
        protagonist = hero(name , 1000 , 150 , 10 , 50 , 'axe' , 50 , stuff , set)
    elif hero_class.startswith("M"):
        protagonist = hero(name , 500 , 50 , 150 , 300 , 'staff' , 250 , stuff , set)
    elif hero_class.startswith("A"):
        protagonist = hero(name , 700 , 100 , 75 , 175 , 'knife' , 100 , stuff , set)
    else:
        print("Please enter a valid answer")
        protagonist = choose(name , stuff , set)
    return protagonist