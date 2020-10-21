#! python3
# Tic Tac Toe game in python

import pyinputplus as pyip
import random

#board = [' ' for x in range(10)]

def insertLetter(letter, pos):
    board[pos] = letter

def spaceIsFree(pos):
    return board[pos] == ' '

def printBoard(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

def isWinner(bo, le):
    return (bo[7] == le and bo[8] == le and bo[9] == le) or \
           (bo[4] == le and bo[5] == le and bo[6] == le) or \
           (bo[1] == le and bo[2] == le and bo[3] == le) or \
           (bo[1] == le and bo[4] == le and bo[7] == le) or \
           (bo[2] == le and bo[5] == le and bo[8] == le) or \
           (bo[3] == le and bo[6] == le and bo[9] == le) or \
           (bo[1] == le and bo[5] == le and bo[9] == le) or \
           (bo[3] == le and bo[5] == le and bo[7] == le) 

def playerMove():
    run = True
    while run:
        move = pyip.inputNum('Please select a position to place an \'X\'' \
       ' (1-9): ',min = 1, max = 9)

        if spaceIsFree(move):
            run = False
            insertLetter('X', move)
        else:
            print('Sorry, this space is occupied!')

def compMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter ==' ' \
                     and x != 0]

    move = 0

    '''checks to see if there are any winning spaces for 'O'
        or a way to block 'X' from winning'''
    for let in ['O', 'X']:               
        for i in possibleMoves:          # put all spaces left in a copy of.. 
            boardCopy = board[:]         # ..board
            boardCopy[i] = let           # put letter in the free space
            if isWinner(boardCopy, let): # check to see if the space filled up..
                move = i                 # ..is a winning move, then return that
                return move

    '''if no winning spaces are available then we want to place 'O'
        in the one of the corners, then centre, then edge if there is no space
        respectively'''
    cornersOpen = []
    for i in possibleMoves:              
        if i in [1,3,7,9]:               # checks to see any spaces free in..
            cornersOpen.append(i)        # .. corners.
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen) # if there is a space randomly select..
        return move                      # a corner to place 'O'

    if 5 in possibleMoves:               # check if centre is empty and place..
        move = 5                         #.. 'O' if it is
        return move

    edgesOpen = []
    for i in possibleMoves:              
        if i in [2,4,6,8]:               # checks to see any spaces free in..
            edgesOpen.append(i)          # .. edges.
    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)   # if there is a space randomly select..
        return move                      #..a edge to place 'O'
    return move                      
    

def selectRandom(li):
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]


def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def main():
    print('Welcome to Tic Tac Toe!')
    printBoard(board)

    while not (isBoardFull(board)):
        if not(isWinner(board, 'O')):
            playerMove()
            printBoard(board)
        else:
            print('Sorry, you lose!')
            break

        if not(isWinner(board, 'X')):
            move = compMove()
            if move != 0:
                insertLetter('O', move)
                print('Computer placed an \'O\' in position', move)
                printBoard(board)
        else:
            print('Congratulations, you win!')
            break

    if isBoardFull(board):
        print('Tie Game!')


while True:
    prompt = 'Would you like to play (y/n): '
    retry  = pyip.inputYesNo(prompt)

    if retry == 'yes' or retry == 'y':
        board = [' ' for x in range(10)]
        main()

    elif retry == 'no' or retry == 'n':
        break

print('Game has ended')
