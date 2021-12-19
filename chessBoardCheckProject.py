""""
Author: OzRam21
Date authored: 12/18/2021
Chapter 5 Practice Project 1
Purpose: 
- Create a function named isValidChessBoard
- Take in a dictionary arguement, return true or false 
- Output depends if chess board is valid
- Each player has 16 total pieces
- Each player has 8 pawns, 1 king, 1 queen, 2 bishops, 2 knights and 2 rooks
- Each piece must begin with 'b' or a 'w'
- All pieces must be on a valid space on the board, 'a' to 'h' and 1 to 8
"""

def isValidChessBoard(currBoard):
    refPieces = {'bking':1, 'wking':1, 'bqueen':1, 'wqueen':1, 'brook':2, 'wrook':2,
                'bbishop':2, 'wbishop':2, 'bknight':2, 'wknight':2, 'bpawns':8, 'wpawns':8}
    # This is the reference dictionary for a valid complete chess set

    movesExtract = list(currBoard.keys()) # All the board spaces are extracted and placed into a list

    piecesExtract = list(currBoard.values()) # All the pieces on each board space will be extracted into a list

    for mvIndx, move in enumerate(movesExtract): # loop through each move string in the moves list, remember that strings can be enumerated like lists
        if int(move[0]) > 8 or int(move[0]) < 0 : # convert the number literal into an integer and compare
            return False # Returns False because the moves space is greater than 8 or negative
        if move[1] > 'h' or move[1] < 'a': # Compare the letter part of the move
            return False # Returns False if the the letter is uppercase or past 'h' 
    
    try:
        inputPieces = {} # Empty dictionary with piece names as the keys, and number of pieces as the values
        try:
            for pcIndx, piece in enumerate(piecesExtract) : # enumerate through all the pieces from the input dictionary
                inputPieces.setdefault(piece, 0) # Verify if the piece from the list exists in the dictionary already. If not, add it as a key and add 0 to the value
                inputPieces[piece] = inputPieces[piece] + 1 # Increase the value for that particular piece by 1 
                if inputPieces[piece] > refPieces[piece]: # Compare if the input chess piece count exceeds any of the complete chess board count values
                    return False # Return False because the input pieces exceeds the max number for any piece
        except TypeError:
            return False # Returns False because a dictionary key is not valid
    except KeyError:
        return False # One of the input pieces is not valid because it was not found in the complete chess board dictionary
    
    return True


# This dictionary will return false because of invalid space
badMove1 = {'9a': 'wking', '3h':'wqueen', '2g':'bbishop', '6b':'bking', '3e':'bqueen'}

# This dictionary will return false because of 2 white kings
badMove2 = {'1a': 'wking', '3h':'wqueen', '2g':'bbishop', '6b':'bking', '3e':'bqueen', '2b':'wking'}

# This dictionary will return false because of 'pking' being an invalid piece
badMove3 = {'9a': 'wking', '3h':'wqueen', '2g':'bbishop', '6b':'pking', '3e':'bqueen'}

# This dictionary will return false because of there is a list in a key
badMove4 = {'1a': [1,'boo'], '3h':'wqueen', '2g':'bbishop', '6b':'pking', '3e':'bqueen'}

# This dictionary will return True
goodMove = {'1a': 'wking', '3h':'wqueen', '2g':'bbishop', '6b':'bking', '3h':'bqueen'}

# All these should print False
print(isValidChessBoard(badMove1))
print(isValidChessBoard(badMove1))
print(isValidChessBoard(badMove3))
print(isValidChessBoard(badMove4))

# This should print True
print(isValidChessBoard(goodMove))