def Mana_potion(object,inv):
    inv["Mana potion"] -= 1
    object.mana += 35
def HP_potion(object,inv):
    inv["Health potion"] -= 1
    object.health += 300

a = 5
b =10
print(str(a) +" + " + str(b) + " bejne: " + str(a+b) )
print(f"{a} + {b} bejne: {a+b}")
print("{} + {} bejne: {}".format(a,b,a+b))

#
# a = 10
# print(a)
# a = a-3
# a-=3
# print(a)