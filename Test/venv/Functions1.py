def count(lst):
    long = 0
    short = 0

    for i in range(len(lst)):
        if len(lst[i]) > 4:
            long += 1
        else:
            short += 1
    return long,short

list=['Ylli', 'Kastro', 'Alba', 'Qendrim', 'Leonora', 'Tini', 'Fjolla']

long,short = count(list)
print("Long names: {} and Short names: {}".format(long,short))
