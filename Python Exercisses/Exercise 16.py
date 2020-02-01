import random
import string
def Password_generator():
    a = int(input('How long do you want your password to be?'))
    strength = input('''Do you want your password to be weak or STRONG:
    A Strong password is more secure and should be used for bigger projects
    Or if you don't want your data to be leaked
    But you can get a weak one to if you don't need it to be that secure
    And you want it to be easy to remember.
    ''')
    Pass = string.ascii_letters + string.digits
    def strong():
        return ''.join(random.choice(Pass) for i in range(a))
    def weak():
        return ''.join(random.choice(string.digits) for i in range(a))
    if strength == 'STRONG':
        return strong()
    elif strength == 'weak':
        return weak()
    else:
        print('Please enter a valid number')
        return Password_generator()


print("Here's you password: " + Password_generator())
b = input('You want another password?')
while b == 'yes':
    print("Here's you password: " + Password_generator())
    b = input('You want another password?')
else:
    print('Goodbye')