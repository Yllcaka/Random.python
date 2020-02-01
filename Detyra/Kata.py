def digital_root(n):
    l = 0
    for i in str(n):
        l += int(i)
    b = l
    while b>=10 or b==0:
        b = 0
        for i in str(l):
            b += int(i)
    return b
print(digital_root(1866888))