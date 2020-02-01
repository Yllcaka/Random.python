def counts(lst):



    more = 0

    less = 0



    for i in range(len(lst)):

        if len(lst[i]) > 5:

            more = more + 1

        else:

            less = less + 1



    return more, less





list = []

x = int(input("How many names you want to enter:"))



for k in range(x):

    list.append((input()))



more, less = counts(list)

print('Names more than 5 characters : {} and Names less than 5 characters : {}'.format(more, less))

