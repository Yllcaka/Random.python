a1 = 1
r = 2
n = 4

def geometricRecursion(a1,n,r):
    if n <= 1:
        return a1
    return geometricRecursion(a1,n-1,r)*r

print("Numri i kthyer eshte: " + str(geometricRecursion(a1,n,r)))