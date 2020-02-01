def arithmeticRecursion(n,d):
    if n <= 1:
        # print('Numri eshte 1')
        return 1

    print('Numri eshte ' + str(n))
    arithmeticRecursion(n - 1,d)
arithmeticRecursion(10,3)