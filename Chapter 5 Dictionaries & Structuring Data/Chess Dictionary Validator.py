#Takes a dictionary argument and returns true or false depending on if the board is valid

#restrictions
#Each player can have at most 16 piees
# 8 pawns at most
# spaces can be from 1a to 8h
# each player can only have one king or queen
# pieces can begin with either w or b to represent white or black

#need to generate valid spaces
#need to generate valid pieces
#then create argument to check

def isValidChessBoard(board):
    # creating keys to map valid spaces
    validspaces = {'1a':'', '1b': '','1c':'', '1d':'', '1e':'', '1f':'', '1g':'', '1h':'',
                    '2a':'', '2b':'', '2c':'', '2d':'', '2e':'', '2f':'', '2g':'', '2h':'',
                    '3a':'', '3b':'', '3c':'', '3d':'', '3e':'', '3f':'', '3g':'', '3h':'',
                    '4a':'', '4b':'', '4c':'', '4d':'', '4e':'', '4f':'', '4g':'', '4h':'',
                    '5a':'', '5b':'', '5c':'', '5d':'', '5e':'', '5f':'', '5g':'', '5h':'',
                    '6a':'', '6b':'', '6c':'', '6d':'', '6e':'', '6f':'', '6g':'', '6h':'',
                    '7a':'', '7b':'', '7c':'', '7d':'', '7e':'', '7f':'', '7g':'', '7h':'',
                    '8a':'', '8b':'', '8c':'', '8d':'', '8e':'', '8f':'', '8g':'', '8h':''}
    numberofbKings = 0
    numberofbQueens = 0
    numberofbPawns = 0
    numberofwKings = 0
    numberofwQueens = 0
    numberofwPawns = 0
    totalwpieces = 0
    totalbpieces = 0

    #checks if there's at least a king or queen in board
    if 'bking' not in board.values:
        return False
    if 'bqueen' not in board.values:
        return False
    if 'wking' not in board.values:
        return False
    if 'wqueen' not in board.values:
        return False
    # if board key is not in valid spaces, returns false
    if board.keys not in validspaces
        return False

    for board.keys in validspaces: #for board.keys in validspaces (if the board key happens to be a valid space)
        #Black piece checker
        if 'bking' in board.values:
            numberofbKings = numberofbKings + 1
            if numberofbKings > 1:
                return False
        if'bqueen' in board.values:
            numberofbQueens = numberofbQueens + 1
            if numberofbQueens > 1:
                return False
        if 'bpawn' in board.values:
            numberofbPawns = numberofbPawns + 1
            if numberofbPawns > 16
                return False
        #white piece checker
            if 'wking' in board.values:
                numberofwKings = numberofwKings +1
                if numberofwKings > 1:
                    return False
            if 'wqueen' in board.values:
                numberofwQueens = numberofwQueens + 1
                if numberofwQueens > 1:
                    return False



    return False



board = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}

