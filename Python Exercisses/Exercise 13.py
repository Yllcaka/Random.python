def fib(n):
    a = 0
    b = 1
    x=[1]
    for c in range(n):
        i = a+b
        a = b
        b = i
        x.append(b)
    print(x)
fib(4)