def Mana_potion(object,inv):
    inv["Mana potion"] -= 1
    object.mana += 35
def HP_potion(object,inv):
    inv["Health potion"] -= 1
    object.health += 300