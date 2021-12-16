""""
Author: OzRam21
Date authored: 11/23/2021
Chapter 4 Practice Project 2
Purpose: Program will determine how often a streak of 6 heads or 6 tails
        shows up in a randomly generated list of 10,000 simulated coin tosses.
        It should output the percentage of total 6 streaks, 6 head streaks, and 6 tails streaks.  
"""
import random

numFlips = 10000 # Determine how many coin flips will be simulated
resultList = [] # store the outcome of the flips
cntrStreaks = [0,0,0,0] # cntrStreaks[0] = consecutive heads, cntrStreaks[1] = 6 head streaks, 
                    # cntrStreaks[2] = consecutive tails, cntrStreaks[3] = 6 tail streaks
chances = [0,0,0] # stores the total amount of any, heads, and tails streaks
                  # chances[0] = any streak %, chances[1] = heads streak %, chances[2] = tails streak %

# First part of the code
for experimentNum in range(numFlips):
    generatedNum = random.randint(0,1)
    if generatedNum == 0:
        resultList = resultList + ['H']
    else:
        resultList = resultList + ['T']

# Second part of the code
for index, item in enumerate(resultList):
    # This part of the code will check if the item in result list is heads
    if item == 'H':
        cntrStreaks[0] += 1
        if cntrStreaks[2] != 0: # Resets the tails counter to 0 if heads is the item
            cntrStreaks[2] = 0
        if cntrStreaks[0] == 6: # Increases the heads streak counter by 1 if there are 6 heads and resets the heads counter
            cntrStreaks[1] += 1
            cntrStreaks[0] = 0
    # This part of the code will check if the item in result list is tails
    if item == 'T':
        cntrStreaks[2] += 1
        if cntrStreaks[0] != 0: # Resets the heads counter to 0 if tails is the item
            cntrStreaks[0] = 0
        if cntrStreaks[2] == 6: # Increases the tails streak counter by 1 if there are 6 consecutive tails and resets the tails counter
            cntrStreaks[3] += 1
            cntrStreaks[2] = 0

chances[0] = ((cntrStreaks[1]*6 + cntrStreaks[3]*6) / numFlips) * 100 # stores % of overall streaks
chances[1] = ((cntrStreaks[1]*6) / numFlips) * 100 # stores % of heads streaks
chances[2] = ((cntrStreaks[3]*6) / numFlips) * 100 # stores % of tails streaks

# Print all the possibilities: Any streak, heads streak, tails streak
print('Chance of any streak: %s%%, Chance of Heads streak: %s%%, Chance of tails streak: %s%%' % (chances[0],chances[1],chances[2]))