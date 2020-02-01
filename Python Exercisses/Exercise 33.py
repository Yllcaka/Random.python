Birthday = {
    "Ylli":"03.02.2001",
    "Adi":"10.09.1993",
    "Dimi":"02.05.1998"
}
print('''
        We know the birthdays of:
        Ylli
        Adi
        Dimi
''')
a = input('Which one do you wanna choose')
if a in Birthday:
    print(f"The birthday of {a} is on: {Birthday.get(a)}")
else:
    print("That birthday isn't on the list")
