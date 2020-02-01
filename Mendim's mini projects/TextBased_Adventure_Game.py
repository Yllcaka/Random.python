import time


def key():
    print('"The key to the Tree",is embedded on it')
    time.sleep(1)
    key_door = str(input('You go to the door,do you wanna open it? '))
    if key_door == 'yes':
        Hallway_door()
    elif key_door == 'no':
        print('You lay there and cry then,idk')

def base():
    direction = str(input('Go left or right? '))
    if direction == 'right':
        door_right()
    elif direction == 'left':
        door_left()
    else:
        print('Those two doors are the only way')
        base()
def Hallway_door():
    print('You open up the door slowly')
    time.sleep(3)
    print('Theres just a sapling planted there,')
    time.sleep(2)
    print('You say:\n"Is this all there is..."')
    time.sleep(2)
    print('"...is this a joke"')
    time.sleep(5)
    print(name,'starts looking around trying to find answers')
    time.sleep(2)
    print("Theres a big sign above, there's something written")
    time.sleep(5)
    print('')
    print('')
    print('')
    print('')
    print('                            MUST NOT BE NAMED                            ')
    print('')
    print('')
    print('')
    print('')
    time.sleep(10)
    print('You say to yourself\n"What does it mean"')
    time.sleep(4)




def door_right():
    print('You open the door...')
    print("There's just a dog here")
    pet = input('You want to pet it? ')
    if pet == 'yes':
        time.sleep(.5)
        print('He barks at you, you bark back')
        print('You go out and close the door')

    if pet == 'no':
        print("There isn't anything else to do here")
        print('You go out and close the door')
    base()
def looking():
    print('You look around and you see a corpse')
    examine = str(input('You wanna examine the corpse '))
    if examine == 'yes':
        print("There's a key round the corpses neck you take it")
        print('You got a key')
        key()
    if examine == 'no':
        print("You act like you didn't see anything and keep walking")
        print("Theres a door at the end of the hallway")
        time.sleep(2)
        print("You try to open it\nIt's locked")
        time.sleep(1)
        print('On the door writes something\n"IF YOU WANT TO GO TO THE TREE YOU MUST FIRST GO THROUGH THE KEEPERS RIDDLE"')
        examination = str(
            input('You go back to the corpse,you think to yourself is it worth it to go through the corpse '))
        if examination == 'yes':
            print("There's a key round the corpses neck you take it")
            print('You got a key')
            key()
        elif examination == 'no':
            print('please just go with it ')
            looking()
def door_left():
    dare = str(input('There is a spooky hallway \n You dare to "go" through there or do you go "back" '))
    if dare == 'back':
        print('You close the door and go back to the beginning')
        base()
    elif dare == 'go':
        print('As you go through the hallway you hear a howling sound')
        look = str(input('Do you want to look around '))
        if look == 'yes':
            looking()
        if look == 'no':
            print("You see there's a door at the end of the hallway,you go to it")
            time.sleep(1)
            print("You try to open it,but it's locked")
            sure = str(input("You want to look around ,maybe theres something around here that can help you? "))
            if sure == 'yes':
                looking()
            elif sure == 'no':
                print('I guess, you go back to the beginning than')
                base()
    else:
        print("There isnt't any other way")
        door_left()
#<----------THE----------------------GAME-------------------->
print('You trip')
time.sleep(3)
print('You just fell into a well')
time.sleep(2)
print('You just met an old man')
name = input('"What is your name young boy" - says the old man:')
print('"',name,'"-You tell him')
print('"',name,',if you wanna escape from this so-called dungeon you have to find the tree" -The old man says')
time.sleep(4)
print('He shows you two doors,one to the left and one to the right...\n"One of these doors leads the path to the tree...CONTINUE AT YOU OWN RISK"')
time.sleep(6)
print('The old man Throws a smokebomb on the ground and disappears...')
base()
print('                            ...TO BE CONTINUED...                            ')

