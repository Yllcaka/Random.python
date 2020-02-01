from collections import namedtuple

Colors = namedtuple("Colors",['red','green','blue'])
white = Colors(255,222,243)
print(white.green)
print(white[0])