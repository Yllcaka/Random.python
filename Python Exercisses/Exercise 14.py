def set_list(x):
    a = input("Enter anything to add to the list when done just type 'end'")
    while a != 'end':
        x.append(a)
        a = input ('Enter another item')
    print(set(x))
def list_without_set(x):
    a = input("Enter anything to add to the list when done just type 'end'")
    while a != 'end':
        if a in x:
            a = input('Enter another item')
        else:
            x.append(a)
            a = input('Enter another item')
    print(x)
def list_type():
    enter = input("Do you wanna have an ordered or unordered list? ")
    enter = enter.lower()
    if enter.startswith("or"):
        a = []
        set_list(a)
    elif enter.startswith("un"):
        x = ['Everything']
        list_without_set(x)
    else:
        print("Please enter a valid answer ")
        list_type()
list_type()