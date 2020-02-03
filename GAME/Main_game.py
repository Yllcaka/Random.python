from Fight import *
from Enemy import *
import os

def instructions():
    print(bold , ''' The instructions to the game are simple when
when there's something to choose from just enter the first letter
of the word.''' , end)
    answer = (input("Do you understand,if so enter 'Yes' ").lower())
    if not answer.startswith("y"):
        print("Alright than here you go again")
        instructions()


def start():
    magic_set = [spell("Ember" , 20 , "Fire") , spell("Poison Spit" , 10 , "Poison"), spell("Healing Touch",10,"Healing")]
    stuff = {"Mana potion": 5,"Health potion":5}
    name = input("What's your name? ")

    protagonist = choose(name , stuff , magic_set)
    return protagonist

def The_actual_fighting(hero):
    while hero.health > 0:
        os.system("cls" if os.name == 'nt' else "clear")
        hero.leveling_system()
        enemy = monsters(hero)
        if monsters(hero).name == "The Dark King":
            KING = monsters(hero)
            fight(hero , KING)
            if KING.health <= 0:
                print("YATAAAA YOU WON YOU SLAYED THE EVIL LORD")
            break
        fight(hero , enemy)
        print("You earned 50XP")
        hero.exp += 50


instructions()
protagonist = start()
The_actual_fighting(protagonist)
