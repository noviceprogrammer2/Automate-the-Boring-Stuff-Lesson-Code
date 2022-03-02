# Creating a blank Tic Tac Toe board using dictionaries

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
printBoard(theBoard)

#Code below allows player to enter moves

turn = 'X'
for i in range(9): #Repeats loop 9 times since there are 9 spaces on tic tac toe
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    theBoard[move] = turn #at the location of the move on the board, enter either x or o
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
printBoard(theBoard)
