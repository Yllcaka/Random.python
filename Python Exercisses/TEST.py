import json
with open("scientist_birthdays.json","r") as f:
    info = json.load(f)
print("We know these Birthdays:")
print(info.keys())
a = input('Which one do you wanna choose')
if a in info:
    print(f"The birthday of {a} was on: {info.get(a)}")
else:
    print("That birthday isn't on the list")
b = input("Do you wanna add any other birthday???  ")
b = b.lower()
if b.startswith("y"):
    name = input("Enter the name of the person ")
    day = input("Enter the birthday ")
    info.update({name:day})

    with open("scientist_birthdays.json","w") as d:
        json.dump(info,d)
else:
    print("alright have a nice day then")