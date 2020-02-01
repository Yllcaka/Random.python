import random as r


class enemy:
    status = "Normal"
    def __init__(self , name , health_points , strength , type , speed):
        self.name = name
        self.health = health_points
        self.strength = strength
        self.type = type
        self.speed = speed

    def att_back(self , protagonist):
        protagonist.health -= self.strength + r.randint(1 , 5)


def monsters(The_Hero):
    antagonist = [enemy("Slime" , 100 , 2 , 'Normal' , 3) , enemy("Goblin" , 70,  3 , "Poison", 4)]
    if The_Hero.level == 2:
        for i in antagonist:
            i.health += 100
            i.name = f"Forest {i.name}"
        antagonist.append(enemy("Dragon" , 200 , 10 ,"Fire", 5))
    elif The_Hero.level == 3:
        for i in antagonist:
            i.health += 150
            i.name = f"Heavenly {i.name}"
    elif The_Hero.level >= 4:
        antagonist = enemy("The Dark King" , 1500 , 100  , "Gold", 30)
        return antagonist
    return r.choice(antagonist)
