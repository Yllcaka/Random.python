# PLEEEEEEEEEEEEEEEEEASE!!!!!!!!!!!!!!!!!!!!!!!
list = [i for i in range(10) if i%2 == 0]
print(list)
list1 = [1,2,3,4,5]
list2 = [5,4,3,2,1]
for i,v in zip(list1,list2):
    print(f"This is the first one {i}, but this, this is the second {v}")
cop = []
for i in "4ll th3 numb3r5 1 n33d 4r3 g01ng t0 b3 th3r3":
    try:
        cop.append(int(i))
    except:
        pass
print('The numbers of the above string are {} {} {} {} {}'.format(*cop))
lista_e_pesdhet = [int(i) for i in "12345"]
print(lista_e_pesdhet)
