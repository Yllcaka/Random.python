import random_word

string = '''The French lettering company Letraset manufactured a set of dry-transfer
                        sheets which included the lorem ipsum filler text in a variety of fonts, sizes, and layouts.
                        These sheets of lettering could be rubbed on anywhere and were quickly adopted by graphic
                        artists, printers, architects, and advertisers for their professional look and ease of use.'''
lst = string.split()
# print(lst)
r_stuff = []
for i in range(len(lst)):
    r_stuff.append(random.choice(lst))
a = " ".join(r_stuff)
print(len(a))
print(len(string))


def reverseWords(input):
    # split words of string separated by space
    inputWords = input.split(" ")

    # reverse list of words
    # suppose we have list of elements list = [1,2,3,4],
    # list[0]=1, list[1]=2 and index -1 represents
    # the last element list[-1]=4 ( equivalent to list[3]=4 )
    # So, inputWords[-1::-1] here we have three arguments
    # first is -1 that means start from last element
    # second argument is empty that means move to end of list
    # third arguments is difference of steps
    inputWords = inputWords[-1::-1]

    # now join words with space
    output = ' '.join(inputWords)

    return output
print(reverseWords(string))