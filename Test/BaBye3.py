class Student:
    school = 'Universum'

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return int((self.m1 + self.m2 + self.m3) / 3)

    @classmethod
    def info(cls):
        return cls.school

    @staticmethod
    def info2():
        print('This is a program')


s1 = Student(2, 3, 4)
s2 = Student(3, 4, 5)

print(s1.avg())
print(Student.info())


Student.info2()
