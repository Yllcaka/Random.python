from adda3 import *
s1 = Student(53,22)
s2 = Student(15,7)
s3 = s1+s2

print(s3.m1)
if s1 > s2:
    print('s1 is the winner')
else:
    print('s2 is the winner')
s3 = s1-s2
print(s3.m1) #Nje pyetje per mendimin
print(s1.__str__())
s3 = s1 / s2
print(s3.m1)
print(s3.m2)