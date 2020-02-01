def div (a,b):
    print(a/b)

def smart_div(func):

    def inner(a,b):
        if a<b:
            a,b = b,a
        return func (a,b)
    return inner

bla=smart_div(div)
x=int(input('The first number'))
y=int(input('The second number'))
bla(x,y)