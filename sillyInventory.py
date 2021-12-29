# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 11:40:14 2021

@author: gmahenr
"""

from random import random, randrange

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        item_total = item_total + v
    for k, v in inventory.items():
        print(str(v) + ' ' + k )
    print("Total number of items: " + str(item_total))

def addToInventory(inventory, addedItems):
    for k in addedItems:
        if k in inventory: 
            inventory[k] = inventory[k] + 1
        else:
            inventory.setdefault(k,  1)
    return inventory
      
def addInvToInv(inv1, inv2):
    for k, v in inv2.items():
        if k in inv1:
            inv1[k] = inv1[k] + inv2[k]
        else:
            inv1.setdefault(k, v)
    return inv

def generateMouseLoot():
    dagger = round(random() * .65)
    goldCoins = randrange(0,50)
    ratMeat = round(random() * 10)
    if dagger == 0 and goldCoins == 0:
        return {'rat meat': ratMeat}
    elif dagger == 0 and goldCoins > 0:
        return {'gold coin': goldCoins, 'rat meat': ratMeat}
    else:
        return {'gold coin':goldCoins,'dagger':dagger, 'rat meat': ratMeat}
    
inv = {'gold coin': 42, 'rope': 1}

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

inv = addToInventory(inv, dragonLoot)

inv = addInvToInv(inv, stuff)
mouse = generateMouseLoot()
inv = addInvToInv(inv, mouse)
displayInventory(inv)