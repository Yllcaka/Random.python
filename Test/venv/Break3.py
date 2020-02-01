def fun():
    r=100
    i=3
    a=1
    b=1
    f=[0,1,1]
    c=2
    while c<r:

        c=a+b
        if c>=100:
              break
        f.append(c)
        a=b
        b=c
    print(f )
    return f
fun()