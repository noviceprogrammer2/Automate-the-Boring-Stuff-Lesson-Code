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
    #counters
    numberofKings = 0
    numberofPawns=0
    totalpieces=0
    validspaces = {'1a':'', '1b': '','1c':'', '1d':'', '1e':'', '1f':'', '1g':'', '1h':'', '2a':'', '2b':'', '2c':'', '2d':'', '2e':'', '2f':'', '2g':'', '2h':'','3a':'', '3b':'', '3c':'', '3d':'', '3e':'', '3f':'', '3g':'', '3h':'','4a':'', '4b':'', '4c':'', '4d':'', '4e':'', '4f':'', '4g':'', '4h':'','5a':'', '5b':'', '5c':'', '5d':'', '5e':'', '5f':'', '5g':'', '5h':'','6a':'', '6b':'', '6c':'', '6d':'', '6e':'', '6f':'', '6g':'', '6h':'','7a':'', '7b':'', '7c':'', '7d':'', '7e':'', '7f':'', '7g':'', '7h':'','8a':'', '8b':'', '8c':'', '8d':'', '8e':'', '8f':'', '8g':'', '8h':''}
    #checks if there's at least a king or queen in board
    if 'bking' in board.values() == False:
        return False
    if 'wking' in board.values() == False:
        return False
    # if board key is not in valid spaces, returns false
    for key in board.keys():
        if key not in validspaces.keys():
            print('Value: %s not in validspace on chess board'%(key))
            return False

    for v in board.values(): #checks each value and makes assignments
        #king checker
        if 'bking' or 'wking' in board.values():
            numberofKings = numberofKings + 1
            totalpieces = totalpieces + 1
        #pawn checker
        elif 'wrook' or 'brook' or 'wbishop' or 'bbishop' or 'wknight' or 'bknight' in board.values:
            totalpieces = totalpieces + 1
        elif 'wPawn' or 'bPawn' in board.values():
            numberofPawns = numberofPawns + 1
            totalpieces = totalpieces + 1
    print(totalpieces)


testboard = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
isValidChessBoard(testboard)

