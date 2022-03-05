
#Function takes any inventory and displays it in pretty print while tallying total of items

# inventory.py
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items(): #for keys and values in inventory

        print(str(v) + ' ' + str(k)) #converts value and key to strings, prints them in proper formatting
        item_total = item_total + int(v) #converts value to integer and adds it to item total
    print("Total number of items: " + str(item_total))



#Add to inventory function takes new loot and adds it to the original inventory
def addToInventory(inventory, addedItems):
        for loot_item in addedItems: #for dragonloot in existing inventory
            #at inventory[loot_item], if already in inventory add one to it, if not in inventory, set loot_item = 0
            # then add one (tricks program into always adding one of new item if it doesn't exist yet)
            # if item exists in inventory, get statement is ignored and one is added to that item in inventory
            inventory[loot_item] = inventory.get(loot_item,0) + 1 





    #need get default function if item in dragon loot not in inventory

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
