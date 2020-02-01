def update(x):
    print('Value of x ',x)
    print('Memory Address of x before update',id(x))
    x=8
    print('Value of x after update',x)
    print('Memory Address of x after update',id(x))

a=10
update(a)
