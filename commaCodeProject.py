""""
Author: OzRam21
Date authored: 11/22/2021
Chapter 4 Practice Project 1
Purpose: Function will take in a list value as an arguement. Then it will return a string 
        that combines the list values together into a string. Items are separated by a 
        comma and a space. The last value in the list will include an 'and' before the last value.  
"""

def commaString(entryList): # defining the function that will convert a list into a string
    strList = [] # This list will store the string version of the input list values
    outString = ''
    # Declaring our empty list and string that  

    if len(entryList) == 0: # First the list is checked if it is empty
        outString = 'Empty list'
        return outString
        # Return a list saying that the input list was empty
        
    else:
        for x in range(len(entryList)):
            strList.append(str(entryList[x]))
            # Here we will cycle through the values in the input list, convert the values to the string version, and store into the strList list
            # This bypasses the need to check if a value is a string or not

        for i in range(len(strList)): # Check to see if the list value is the last one 
            if i > 0 and i + 1 == len(strList):
                outString = outString + 'and ' + strList[-1]
                # If it is the last one, add the 'and' and the string list value to the string that will be returned 
            else:
                outString = outString + strList[i] + ', '
                # Concatonate the list value and seperate with a comma and a space
        return outString

spam = ['beaver',43, 56,28.4, 7878.3, 'bean']
print(commaString(spam))
