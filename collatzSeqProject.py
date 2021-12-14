""""
Author: OzRam21
Date authored: 11/14/2021
Chapter 3 Practice Project 1
Purpose: Create a program that asks the user for a number 
        and continuously puts it through a collatz function until
        the value evaluates to 1.
"""

def collatz(number):
    isEven = number % 2 # Check if the users number is odd
    if isEven == 0:
        endResult = number // 2
        print(endResult)
        return endResult
        # Prints and returns the evaluated number
    else:
        endResult = 3 * number + 1
        print(endResult)
        return endResult
        # Prints and returns the evaluated number

try:
    print('Enter a number: ')
    userNum = int(input())
    # Ask user for number and convert to integer

    while userNum != 1:
        userNum = collatz(userNum)
    # Keep calling the collatz sequence number until the number is 1

except ValueError:
    print('You did not enter a valid number!')
    # This is a except statement that is raised when the user input is not a integer number