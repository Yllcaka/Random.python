class Student:
    def __init__(self, Name, nr):
        self.Name = Name
        self.nr = nr
        self.lap = self.Laptop()

    def show(self):
        print(self.Name, self.nr)
        self.lap.show()

    class Laptop:
        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = 16
        def show(self):
            print(self.brand, self.cpu, self.ram)
s1 = Student('Ylli',30,)
s2 = Student('Toti',17)
s1.show()
s1.lap.show()