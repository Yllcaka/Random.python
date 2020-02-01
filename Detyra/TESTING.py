class Car:
    coolness = "Really cool"

    def __init__(self , emri , ngjyra , viti):
        self.name = emri
        self.color = ngjyra
        self.year = viti

    def __repr__(self):
        return f"\"This is a {self.name}, made in {self.year}, with a fine color of {self.color}\""

    start = (lambda self: print("The engine has actually started..."))

    specs = (lambda self: print())

    cool = (lambda self: print(f"This car like all the other is really {self.coolness}"))
    # def cool(self):
    #     print(f"This car like all the other is really {self.coolness}")


cars = []


def MORE():
    for i in cars:
        i.start()
        i.specs()
        i.cool()
    Again = input("Do you wanna add more cars")
    Again = Again.upper()
    if Again.startswith("Y"):
        number()
    else:
        print("It was nice meeting you")


def number():
    Number_of_Cars = int(input("How many cars do you want"))
    for i in range(Number_of_Cars):
        a = input("Car name ")
        b = input("Car color ")
        c = input("Car Year ")
        cars.append(Car(a , b , c))
    MORE()


# a = Car("Audi","White",2019)
# print(a.name)
# a.start()
# a.specs()
# # print(type(a))
# number()
# for i in cars:
#     print(i.name)
# print(cars)