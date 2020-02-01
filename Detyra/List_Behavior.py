import copy

spam = [[1,2,3],[4,5,6],[7,8,9]]
maps = copy.copy(spam)
cheese = copy.deepcopy(spam)
other = spam

spam.append("nothing")
maps.append("Something")
spam[1][1] = "bla bla"
maps[2][1] = "PLEASE LOOOOOOK"
cheese[2][2] = "NICE"
print(spam , "This is spam")
print(maps ,"This is maps Shallow copy")
print(cheese, "This is Cheese Deep copy")
print(other,"This is other Normal assigned list to a variable")
print()

print("this is the id of spam",id(spam))
print("this is the id of maps",id(maps))
print("this is the id of cheese",id(cheese))
print("this is the id of other",id(other))

print()

print("this is the id of spam element",id(spam[2][1]))
print("this is the id of maps element",id(maps[2][1]))
print("this is the id of cheese element",id(cheese[2][1]))
print("this is the id of other element",id(other[2][1]))

print()

print("this is the id of spam element",id(spam[2][2]))
print("this is the id of maps element",id(maps[2][2]))
print("this is the id of cheese element",id(cheese[2][2]))
print("this is the id of other element",id(other[2][2]))
