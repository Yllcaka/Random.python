f = open("/home/ylli/Pictures/Toti.png" , "rb")
f1 = open('LALA.png','wb')
for i in f:
    f1.write(i)