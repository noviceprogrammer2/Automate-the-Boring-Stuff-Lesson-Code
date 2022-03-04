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

displayInventory(stuff)
