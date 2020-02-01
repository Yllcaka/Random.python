def backwards():
    a = input('Type a sentence here  ')
    b = a.split()
    b = b[::-1]
    b = ' '.join(b)
    print(b)
backwards()