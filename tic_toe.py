import random


def display_board(board):
    print('\n'*10)
    print(' | | ')
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(' | | ')
    print('-----')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-----')
    print(' | | ')
    print(board[1]+'|'+board[2]+'|'+board[3])
    print(' | | ')

    print('\n'*3)


# test_board = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
# display_board(test_board)


def player_input():
    marker = ''
    # Keep Asking player 1 to choose X or O

    while(marker != 'X' and marker != 'O'):
        marker = input('Player 1, choose X or O: ')

    # Assign player 2, the opposite marker
    player1 = marker

    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'

    return(player1, player2)


# player1_marker, player2_marker = player_input()

# print('Player 1 Marker : '+player1_marker)
# print('Player 2 Marker : '+player2_marker)


def place_marker(board, marker, position):
    board[position] = marker


# place_marker(test_board, '$', 8)
# display_board(test_board)

def win_check(board, mark):
    # Win tic toe game?

    # All rows, and check to see if they all share the same marker?
   # All columns, check to see if marker matches
    # 2 diagonalss , check to see match
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[7] == mark and board[8] == mark and board[9] == mark) or
            (board[7] == mark and board[4] == mark and board[1] == mark) or
            (board[8] == mark and board[5] == mark and board[2] == mark) or
            (board[9] == mark and board[6] == mark and board[3] == mark) or
            (board[7] == mark and board[5] == mark and board[3] == mark) or
            (board[9] == mark and board[5] == mark and board[1] == mark))


# print(win_check(test_board, 'X'))
def choose_first():

    flip = random.randint(0, 1)

    if(flip == 0):
        return 'Player 1'
    else:
        return 'Player 2'


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    # Board is full if we return true

    return True


def player_choice(board):
    position = 0

    while position not in range(1, 10) or not space_check(board, position):
        position = int(input('Choose a position : (1-9) '))

    return position


def replay():
    while True:
        choice = input('Play again? Enter Yes or No: ')
        if (choice == 'Yes' or choice == 'No'):
            break
        else:
            continue
    return choice == 'Yes'


# While loop to keep running the game
print('Welcome to Tic TAC TOE')

while True:
    # Play the Game

    # Set Everything up (board, whos first , choose makers X,O)
    the_board = [' ']*10
    player1_marker, player2_marker = player_input()

    turn = choose_first()
    print(turn+' will go first ')

    play_game = input('Ready to play? y or n ?  ')

    if play_game == 'y':
        game_on = True
    else:
        game_on = False

    # Game Play
    while game_on:
        if turn == 'Player 1':
            display_board(the_board)
            # Choose a position
            position = player_choice(the_board)

            # Place the marker on the position
            place_marker(the_board, player1_marker, position)
            # check if they won
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('Player 1 has WON !!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Tie GAME !!')
                    game_on = False
                else:
                    turn = 'Player 2'
            # or check if there is a tie

            # no tie and no won? then next players turn

            #  PLayer one turn

        else:

            display_board(the_board)
            # Choose a position
            position = player_choice(the_board)

            # Place the marker on the position
            place_marker(the_board, player2_marker, position)
            # check if they won
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('Player  2 has WON !!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Tie GAME !!')
                    game_on = False
                else:
                    turn = 'Player 1'
            # player two turn

            #  Player one turn

            # Player two turn

    if(not replay()):
        break

# Break out of the while loop on replay()
