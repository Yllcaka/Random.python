class A:
    def feature1(self):
        print('This is feature 1')
    def feature2(self):
        print('This is feature 2')
class B:
    def feature3(self):
        print('This is feature 3')
    def feature4(self):
        print('This is feature 4')
class C(A,B):
    def feature5(self):
        print('This is feature 5')
s1 = A()
s2 = B()
s3 = C()
s1.feature2()
s2.feature3()
s3.feature4()