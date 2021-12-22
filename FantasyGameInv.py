""""
Author: OzRam21
Date authored: 12/21/2021
Chapter 5 Practice Project 2
Purpose: 
- Dictionary will represent a player's item inventory
- Dictionary key will be the item name, values will be the number of said item in inventory 
- Write a function that will display the invetory in the following format: [# of item] [item name]
"""

def inventoryDispl(invtDict):
    print('Inventory: ')
    itemTotal = 0
    for name, itmNum in invtDict.items():
        print(str(itmNum) + ' ' + name) # Print out the number of item followed by the name
        itemTotal = itemTotal + itmNum # Variable will sum up the total amount items in the player inventory
    print('Total number of items: ' + str(itemTotal)) # Display the total number of items

# This is an example of a player inventory
myBag = {'potions': 2, 'elixir': 4, 'arrows': 15, 'royal quiver': 1, 'light chestplate': 1}

inventoryDispl(myBag)