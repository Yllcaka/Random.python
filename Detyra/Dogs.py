class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
kevin = Dog("Kevin",5)
arex = Dog("Arex",8)
gjina = Dog("Gjina",7)
list = [kevin,arex,gjina]
get_biggest_number = (lambda *x:max(x))
print(f"The oldest dog is {get_biggest_number(kevin.age, arex.age , gjina.age)} years old")
for i in list:
    a = input(f"You wanna know the name or age of {i.name} ")
    a = a.upper()
    if a.startswith("A"):
        print(i.age)
    elif a.startswith("N"):
        print(i.name)
    else:
        print(f"Whatever here are both {i.name} and {i.age}")