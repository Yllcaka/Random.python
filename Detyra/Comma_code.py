def actual(word):
    the_string = ""
    for i in range(len(word)-1):
        the_string+= "{}, "
    the_string += f"and {word[-1]}."
    return the_string.format(*word)






spam = ['apples' , 'bananas' , 'tofu' , 'cats',"bla bla"]
print(actual(spam))