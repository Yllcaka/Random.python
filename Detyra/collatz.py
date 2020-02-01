def collatz():
    a = int(input("Please enter a number"))
    try:
        while a != 1:
            if a %2 == 0:
                a = a //2
                print(a)
            elif a%2 != 0:
                a = 3 * a + 1
                print(a)

    except:
        print("Please try again.")


# while i != 1:
#     print(collatz(i))

collatz()
