lista = [1, 2, 5, 6, 7, 10]

def maxElement(lista):
    output = lista[0]

    for i in range(1, len(lista)):
        if lista[i] > output:
            output = lista[i]

    return output

def minElement(lista):
    output = lista[0]

    for i in range(1, len(lista)):
        if lista[i] < output:
            output = lista[i]

    return output

def findElement(lista, numrin):
    for i in range(0, len(lista)):
        if (lista[i] == numrin):
            return i

    return -1

# print(findElement(lista, 2))

def binarySearch(lista, numrin, add=0):
    end = len(lista)
    middle = int(end / 2)
    print(middle)
    if lista[middle] == numrin:
        print(middle)
    elif middle == 0:
        return -1 - add
    elif numrin > lista[middle]:
        return binarySearch(lista[middle:], numrin, middle + add) + middle
    elif numrin < lista[middle]:
        return binarySearch(lista[:middle], numrin)

# 1, 2, 5, 6, 7, 10
# print(binarySearch(lista, 1))
# print(binarySearch(lista, 2))
# print(binarySearch(lista, 5))
# print(binarySearch(lista, 6))
# print(binarySearch(lista, 7))
# print(binarySearch(lista, 10))
# print(binarySearch(lista, -6))
# print(binarySearch(lista, 194809401))
# print(maxElement([1,5,3,9,-1]))
# print(findElement([1,5,3,9,-1],3))
binarySearch([1,5,3,-1,9],9)