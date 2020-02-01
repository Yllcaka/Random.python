happynumbers = []
primenumbers = []
with open('happynumbers.txt', 'r') as open_file:
    line = open_file.readline()
    while line:
        happynumbers.append(int(line))
        line = open_file.readline()
with open('primenumbers.txt', 'r') as open_file:
    line = open_file.readline()
    while line:
        primenumbers.append(int(line))
        line = open_file.readline()
SAME = []
for elem in happynumbers:
    if elem in primenumbers:
        SAME.append(elem)
print(SAME)