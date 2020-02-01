import pprint as p
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    # if character not in count:
    #     count[character] = 0
    count[character] = count[character] + 1
    print(count[character])

print(count)

# stuff = ['spam', 'eggs', 'lumberjack', 'knights', 'ni']
# stuff.insert(0,stuff[:])
# pp = p.PrettyPrinter(indent=4)
# p.pprint(stuff)

# spam = {1:"First",2:"Second",3:"Third"}
# for i,v in spam.items():
#     print(i,v)