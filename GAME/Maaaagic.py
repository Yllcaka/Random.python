import random as r


class spell:
    def __init__(self , spell_name , spell_power , spell_type):
        self.spell_name = spell_name
        self.spell_power = spell_power
        self.spell_type = spell_type


def statistical_damage(magic_receiver , sickness):
    stat = magic_receiver.status
    print("The enemies is:" , stat)
    if stat != "Normal" and stat in sickness:
        magic_receiver.health -= sickness[stat]


def magic_type(magic_attack , magic_attacker , magic_receiver):
    if magic_attack.spell_type == "Fire":
        magic_receiver.health -= (magic_attacker.magical * r.randint(1 , 3) + 5)
        if r.random() < 0.1:
            magic_receiver.status = "Burning"
    elif magic_attack.spell_type == "Poison":
        magic_receiver.health -= (magic_attacker.magical * r.randint(1 , 3))
        if r.random() < 0.5:
            magic_receiver.status = "Poisoned"
    elif magic_attack.spell_type == 'Healing':
        magic_attacker.health += magic_attacker.magical * 10


statistical_hindering = {"Burning": 8 , "Poisoned": 15}
