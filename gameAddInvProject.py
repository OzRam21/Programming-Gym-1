""""
Author: OzRam21
Date authored: 12/22/2021
Chapter 5 Practice Project 3
Purpose: 
- Write a function that has 2 parameters, a dictionary parameter and a list parameter
- The dictionary parameter will represent a player's current inventory 
- The list parameter will represent the loot that can be gained after vanquishing a particular foe
- Function should return a dictionary with the player's updated inventory  
"""

def addToInventory(inventory, addedItems): # Take in the inventory dictionary parameter and the addedItems list
    for index, item in enumerate(addedItems): # Loop through the list 
        inventory.setdefault(item, 0) # Check if the item from the list already exists in the dictionary. If not, add it as a key and with a value of 0
        inventory[item] = inventory[item] + 1 # Increase the value of the item key by 1 for each occurence in the list
    return inventory # Return the updated dictionary with the added items

# This code was already explained in 'Chapter 5 Practice Project 2'
def inventoryDispl(invtDict):
    print('Inventory: ')
    itemTotal = 0
    for name, itmNum in invtDict.items():
        print(str(itmNum) + ' ' + name)
        itemTotal = itemTotal + itmNum 
    print('Total number of items: ' + str(itemTotal)) 
   
# This is an example of a player inventory
myBag = {'potions': 2, 'elixir': 4, 'arrows': 15, 'royal quiver': 1, 'light chestplate': 1}

# This is the loot gained after vanquising a dragon
dragonLoot = ['gold coin','dagger','gold coin','gold coin','ruby']


inventoryDispl(myBag) # Display the player inventory before added items
updatedInv = addToInventory(myBag, dragonLoot) # Update the inventory
inventoryDispl(updatedInv) # Display the player inventory after the looted items were added