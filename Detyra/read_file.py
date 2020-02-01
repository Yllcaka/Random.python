with open("database.txt","r") as f:
    line = f.readline()
    x = line.split(",")
    x.pop()
    for i in x[2:]:
        print(str(x[0])+str(x[1]) + " said: " + i)
