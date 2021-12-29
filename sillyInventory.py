# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 11:40:14 2021

@author: gmahenr
"""

from random import random, randrange

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        item_total = item_total + v
    for k, v in inventory.items():
        print(str(v) + ' ' + k )
    print("Total number of items: " + str(item_total))
    print()

def addToInventory(inventory, addedItems):
    for k in addedItems:
        if k in inventory: 
            inventory[k] = inventory[k] + 1
        else:
            inventory.setdefault(k,  1)
    return inventory
      
def addInvToInv(inv1, inv2):
    for k, v in inv2.items():
        if k in inv1 and inv2[k] > 0:
            inv1[k] = inv1[k] + inv2[k]
        else:
            inv1.setdefault(k, v)
    return inv

def dictify(listOfStuff):
    blankDict = {}
    for k in listOfStuff:
        if k in blankDict: 
            blankDict[k] = blankDict[k] + 1
        else:
            blankDict.setdefault(k,  1)
    return blankDict

def generateMouseLoot():
    return {
            'gold coin': randrange(0,10,1),
            'dagger': round(random() * .65),
            'rat meat': round(random() * 10)
            }

def sortInventoryAlpha(inv):
    newList = []
    sortedDict = {}
    for k in inv:
        newList.append(k)
    newList.sort() 
    for i in range (0,len(newList)):
        sortedDict.setdefault(newList[i], inv[newList[i]])
    return sortedDict

def sortInventoryNumeric(inv):
    sortedDict = {}
    list1 = sorted(inv, key=inv.get)
    list2 = sorted(inv.values())
    for i in range(0,len(list1)):
        sortedDict.setdefault(list1[i], list2[i])
    return sortedDict

# Initial inventory
inv = {'gold coin': 42, 'rope': 1}

# Things found in a room
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}    

# Loot from a dragon
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

someRandomLoot = ['gunsaw', 'gold coin', 'gold coin', 'arrow', 'arrow', 'arrow', 'potion']
someRandomLoot = dictify(someRandomLoot)
displayInventory(someRandomLoot)

displayInventory(inv)

# Randomly generated loot from a mouse
mouse = generateMouseLoot()
displayInventory(mouse)
# Add items from a list to a dictionary.
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)

# Add dictionary items to dictionary items
inv = addInvToInv(inv, stuff)
displayInventory(inv)

# Add the dictified list to the inventory!
inv = addInvToInv(inv, someRandomLoot)
displayInventory(inv)

# Add a 'randomly' generated dictionary to a dictionary.
inv = addInvToInv(inv, mouse)
displayInventory(inv)

# Sort dictionary alplhabetically
inv = sortInventoryAlpha(inv)
displayInventory(inv)

# sort dictionary numerically.
inv = sortInventoryNumeric(inv)
displayInventory(inv)