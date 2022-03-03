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
    #total counters
    numberofPawns=0
    totalpieces=0
    #white counters
    wking = 0
    wpawn = 0
    totalWhitePieces = 0
    #Black counters
    bking = 0
    bpawn = 0
    totalBlackPieces = 0

    validspaces = {'1a':'', '1b': '','1c':'', '1d':'', '1e':'', '1f':'', '1g':'', '1h':'', '2a':'', '2b':'', '2c':'', '2d':'', '2e':'', '2f':'', '2g':'', '2h':'','3a':'', '3b':'', '3c':'', '3d':'', '3e':'', '3f':'', '3g':'', '3h':'','4a':'', '4b':'', '4c':'', '4d':'', '4e':'', '4f':'', '4g':'', '4h':'','5a':'', '5b':'', '5c':'', '5d':'', '5e':'', '5f':'', '5g':'', '5h':'','6a':'', '6b':'', '6c':'', '6d':'', '6e':'', '6f':'', '6g':'', '6h':'','7a':'', '7b':'', '7c':'', '7d':'', '7e':'', '7f':'', '7g':'', '7h':'','8a':'', '8b':'', '8c':'', '8d':'', '8e':'', '8f':'', '8g':'', '8h':''}

 #Pre for loop initial board test (before bothering with for loop, these three conditions are checked for a valid board)
    #checks if there's at least a king or queen in board
    if 'bking'  not in board.values():
        return print('Error! No black king on the chessboard')
    if 'wking' not in board.values():
        return print('Error! No white king on the chessboard')
    # if board key is not in valid spaces, returns false
    for key in board.keys():
        if key not in validspaces.keys():
            print('Value: %s not in validspace on chess board'%(key))
            return False

    for v in board.values(): #checks each chess value and makes assignments
        #white piece checker

        #counts white kings
        if 'wking' in board.values():
            wking = wking + 1
            totalWhitePieces = totalWhitePieces + 1
        #counts white pawns
        elif 'wpawn' in board.values():
            wpawn = wpawn + 1
            totalWhitePieces = totalWhitePieces + 1
        #any white piece not king or pawn added to total white pieces
        elif 'wrook' or 'wbishop' or 'wknight'in board.values():
            totalWhitePieces = totalWhitePieces + 1

        #black piece checker

        #counts black kings
        elif 'bking' in board.values():
            bking = bking + 1
            totalBlackPieces = totalBlackPieces + 1
        #counts black pawns
        elif 'bpawn' in board.values():
            bpawn = bpawn + 1
            totalBlackPieces = totalBlackPieces + 1
        #counts other black pieces that aren't kings or pawns
        elif 'brook' or 'bbishop' or 'bknight' in board.values():
            totalBlackPieces = totalBlackPieces + 1

    #Tallying totals
    totalpieces = totalWhitePieces + totalBlackPieces
    #Conditional Print structure that prints total pieces for each team with how many pawns they have left
    if totalWhitePieces <= 16 and totalBlackPieces <= 16 and wpawn <= 8 and bpawn<= 8 and bking== 1 and wking == 1:
        print('There are a total of %d pieces on the chessboard.\n'
              'For the Black Team: there are %d pawns and %d total pieces.\n'
              'For the White Team: there are %d pawns and %d total pieces.'
              %(totalpieces,bpawn,totalBlackPieces,wpawn,totalWhitePieces))


testboard = { '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking', '3z':'bking'}
isValidChessBoard(testboard)

