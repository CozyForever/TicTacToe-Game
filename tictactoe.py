# Implementation of a Two Player Tic-Tac-Toe game in Python.

""" The game board is created  using dictionary
   in which keys will be the location (i.e: top-right, bottom-left, etc.)
   and the initial values on the board will be empty and then after each move
    the value will change according to the player's decision.
"""

game_board = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '}

board_choice = []

print("Welcome to the two-player TicTacToe Game!")
print("Choose a space on the board by inputting a value 1-9. ")
print("1 beginning in the bottom-left and 9 ending in the top-right.")

for choice in game_board:
    board_choice.append(choice)

# A updated game board will be printed after every move in the game.
# We will simply define by calling the printBoard function

def print_board(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

# Now define the chess game function which contains the functionality for conducting the game.
def tic_tac_toe():
    turn = 'X'
    count = 0

    for i in range(10):

        print_board(game_board)
        print("It is your turn " + turn + ", " + "What move will you make?")

        move = input()

        if game_board[move] == ' ':
            game_board[move] = turn
            count += 1
        else:
            print("That position is already taken.\nPlease choose a new position.")
            continue
        # Now we will check if player X or O has won for every move after 5 moves.
        if count >= 5:
            if game_board['7'] == game_board['8'] == game_board['9'] != ' ':  # across the top row
                print_board(game_board)
                print("\nGame Over.\n")
                print("**** " + turn + " Congratulations, You won!! ****")
                break
            elif game_board['4'] == game_board['5'] == game_board['6'] != ' ':  # across the middle
                print_board(game_board)
                print("\nGame Over.\n")
                print("**** " + turn + " Congratulations, You won!! ****")
                break
            elif game_board['1'] == game_board['2'] == game_board['3'] != ' ':  # across the bottom
                print_board(game_board)
                print("\nGame Over.\n")
                print("**** " + turn + " Congratulations, You won!! ****")
                break
            elif game_board['1'] == game_board['4'] == game_board['7'] != ' ':  # down the left side
                print_board(game_board)
                print("\nGame Over.\n")
                print("**** " + turn + " Congratulations, You won!! ****")
                break
            elif game_board['2'] == game_board['5'] == game_board['8'] != ' ':  # down the middle
                print_board(game_board)
                print("\nGame Over.\n")
                print("**** " + turn + " Congratulations, You won!! ****")
                break
            elif game_board['3'] == game_board['6'] == game_board['9'] != ' ':  # down the right side
                print_board(game_board)
                print("\nGame Over.\n")
                print("**** " + turn + " Congratulations, You won!! ****")
                break
            elif game_board['7'] == game_board['5'] == game_board['3'] != ' ':  # diagonally
                print_board(game_board)
                print("\nGame Over.\n")
                print("**** " + turn + " Congratulations, You won!! ****")
                break
            elif game_board['1'] == game_board['5'] == game_board['9'] != ' ':  # diagonally
                print_board(game_board)
                print("\nGame Over.\n")
                print("**** " + turn + " Congratulations, You won!! ****")
                break

        # If neither X nor O wins and the board becomes full, the game will result in a 'tie'.
        if count == 9:
            print("\nGame Over.\n")
            print("It's a Tie!!")

        # Change the player after every move.
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

         # Ask if the player's want to restart the game.
    restart = input("Would you like to play Again? (y/n)")
    if restart == "y" or restart == "Y":
        for choice in board_choice:
            game_board[choice] = " "
            print("Thank you for playing!")

        tic_tac_toe()

if __name__ == "__main__":
    tic_tac_toe()