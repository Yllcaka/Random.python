def fun():
    r=99
    i=3
    a=1
    b=1
    c=a+b
    f=[0,1,1]
    while c<r:
        c=a+b
        f.append(c)
        a=b
        b=c
        i=i+1
    print(f)
    return f
fun()