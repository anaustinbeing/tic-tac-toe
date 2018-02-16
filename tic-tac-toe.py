'''
********************************
       Tic-Tac-Toe GAME
    Developer: Austin Joyal
********************************
'''


import sys
import time
import random

 
global position
position = -1
board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
wins = ((0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6))

# printing the initial board showing positions 
def initial_board():
    print('This is the view of the board. Note each position.\nFIRST ROW    1->3\nSECOND ROW   4->6\nTHIRD ROW    7->9')
    print(' _'*3)
    for x in(0,3,6):
        print('|' + board[x] + '|' + board[x+1] + '|' + board[x+2] + '|')
        print(' =+=+=')
        
 # printing board  
def print_board():
    dummy = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    for x, i in enumerate(board):
        if i == 'X' or i == 'O':
            dummy[x] = i
    print(' _'*3)
    for x in(0,3,6):
        print('|' + dummy[x] + '|' + dummy[x+1] + '|' + dummy[x+2] + '|')
        print(' =+=+=')
 
def score(board):
    for w in wins:
        b = board[w[0]]
        if b in 'XO' and all (board[i] == b for i in w):
            return b, [i+1 for i in w]
    return None
 
def over():
    return all (b in 'XO' for b in board)
 
def available(board):
    return [ b for b in board if b not in 'XO']
 
def computer_turn(symbol, board):
    o = 'O' if symbol =='X' else 'X'
    print("\nComputer thinking...")
    time.sleep(5)
    block = None
    options  = [int(s)-1 for s in available(board)]
    for choice in options:
        brd = board[:]
        brd[choice] = symbol
        if score(brd):
            break
        if block is None:
            brd[choice] = o
            if score(brd):
                block = choice
    else:
        choice = block if block is not None else random.choice(options)
    board[choice] = symbol
    return choice+1

def player_turn(symbol, board):
    options = available(board)
    while True:
        timeout = 10
        print("\nYOUR TURN\nPlace {0}. Positions remaining {1}  ".format(symbol, ' '.join(options)))
        position = input() 
        if str(position) in options:
            break
        print( "Wrong input." )
    board[int(position)-1] = symbol
    return position
 
def computer(symbol):
    print_board()
    print('\nComputer selects {}'.format(computer_turn(symbol, board)))
    return score(board)
 
def player(symbol):
    print_board()
    print('\nYou selected {}'.format(player_turn(symbol, board)))
    return score(board)

def first_player(symbol):
    print_board()
    print('Player1 selects {}'.format(player_turn(symbol, board)))
    return score(board)

def second_player(symbol):
    print_board()
    print('Player2 selects {}'.format(player_turn(symbol, board)))
    return score(board)
 
print(__doc__)
initial_board()
option = input('\nSelect one among the following:\n1. Single player\n2. Multi player  ')
if option == 1:
    choice = raw_input("\n'X' or 'O' ?  (Use capitals) ")
    while not over():
        if choice is 'X':
            s = computer('O')
        else:
            s = computer('X')
        if s:
            print_board()
            print("\nYOU LOSE :(\nComputer wins along positions: {} \n  Better Luck next time".format(s[1]))
            break
        if not over():
            s = player(choice)
            if s:
                print_board()
                print("\n*********Congratulations!!********\n  YOU win along positions: {}".format(s[1]))
                break
    else:
        print('\nReally close. The game ended in a draw. :(')

elif option == 2:
    while not over():
        s = first_player('X')
        if s:
            print_board()
            print("\n*********Congratulations!!********\n  Player {0} wins along positions: {1}".format(s[0], s[1]))
            break
        if not over():
            s = second_player('O')
            if s:
                print_board()
                print("\n*********Congratulations!!********\n  Player {0} wins along positions: {1}".format(s[0], s[1]))
                break
    else:
        print('\nReally close. The game ended in a draw. :(')
    
    
