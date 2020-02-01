class Computer:

    def __init__(sef):
        sef.name='Ylli'
        sef.age=18


    def compare(sef,other):
        if sef.age == other.age:
            return True
        else:
            return False
Computer
c1=Computer()
c1.age = 18
c2=Computer()
if c1.compare(c2):
    print('They are the same')
else:
    print('They are different')
