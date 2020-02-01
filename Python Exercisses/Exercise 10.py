import random
a = random.sample(range(1,100),20)
b = random.sample(range(1,100),20)
g = [x for x in a if x in b]
print(g)