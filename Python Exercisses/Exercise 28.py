a = input('Enter a list of number and seperate them with spaces and I will tell you which one is the largest of the bunch')
a = a.split(',')
def maximum(a):
    Large = 1
    for i in a:
        i = int(i)
        if i > Large:
            Large = i
    print(str(Large) + ' is the largest number in the bunch')
maximum(a)