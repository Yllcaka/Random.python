def detyra():
    a = input("A je mashkull apo femer??? ")
    a = a.upper()
    if a.startswith("M"):
        print("Jom tuj fol me Eronin")

    elif a.startswith("F"):
        print("Jom tuj fol me Buk Nören")
    else:
        print("Te lutem shkruj diqka qysh duhet...")
        detyra()
detyra()