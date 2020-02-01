with open("database.txt","w") as f:
        name = input("What is your first name: ")
        surname =input("What is your last name: ")
        dogs = input("Do you like dogs? ")
        cat = input("Do you like cats? ")
        vs = input("Do you think dogs are better than cats? ")

        list = [name,surname,dogs,cat,vs]
        for i in list:
            f.write(i +", ")