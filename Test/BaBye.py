
class computer:
    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = int(ram)
    def config(self):
        print('config is', self.cpu, self.ram)

com1 = computer('i7',12.4)
com2 = computer('i5',10)
com1.config()
com2.config()
a=5
a.bit_length()
print(a)