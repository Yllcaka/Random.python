def addToInventory(inventory, addedItems):
    # your code goes here
    for i in addedItems:

        if i in inventory.keys():
            inventory[i]  = inventory[i] +1
        else:
            inventory.setdefault(i,1)
    return inventory

def displayInventory(qado):
    count = 0
    for k,v in qado.items():
        print(v,"\t",k)
        count += v
    print("The total of items in the inventory is",count)

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
print(type(inv))
displayInventory(inv)
