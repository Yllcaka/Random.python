import random
Hanglist = ["tarabuka","anija","plastelin","vushtrri","qanta","babaruka"]
The_hanged_word = random.choice(Hanglist)

print("Guess what word I'm thinking of")
print("It starts with",The_hanged_word[0])
print("It ends with",The_hanged_word[-1])
print("And it has",len(The_hanged_word),"letters")
print(
    '''The rules go so:
You can guess up to 5 times, let's call it the guess counter
If you guess a letter it won't count as a guess, for the guess counter''')
n = str(input('Now try to guess the word'))
i = 0
while i in range(4):
    if n == "":
        print('Please put in a letter')
        n = str(input('Guess it '))
    elif n == The_hanged_word:
        print("You guessed right, it's",The_hanged_word)
        break
    elif len(n)>1 and n != The_hanged_word:
        print('That is not the word')
        n = str(input('Try again '))
        i += 1
    elif n in The_hanged_word:
        times = The_hanged_word.count(n)
        if times == 1:
            print('Yes that letter is',times,'time in the word')
        else:
            print('Yes that letter is',times,'times in the word')
        n = str(input('You are close try it again '))
    elif n != The_hanged_word:
        print("That letter isn't part of the word")
        n = str(input('Try again '))
        i += 1
if i >=4:
    print('You have failed')
else:
    print('YOU WON')