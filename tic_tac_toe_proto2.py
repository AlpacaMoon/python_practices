from random import randrange
from random import choice

class TTT_Exception(Exception):
    pass

class TTT_Invalid_Input(TTT_Exception):
    def __str__(self):
        return "Invalid input. The input should be an integer between 1 and 9. "

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    for i in range(3):
        print("+-------+-------+-------+")
        print("|       |       |       |")
        print("|", board[i][0], "|", board[i][1], "|", board[i][2], "|", sep = "   ")
        print("|       |       |       |")
    print("+-------+-------+-------+")

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_fields = []
    for row in board:
        for col in row:
            if isinstance(col, int):
                free_fields.append(col)
    return free_fields

def save_move_to_board(board, move, sign):
    for row in range(3):
        for col in range(3):
            if board[row][col] == move:
                board[row][col] = sign
                return

def player_move(board):
    # The function accepts the board current status, asks the user about their move, 
    # checks the input and updates the board according to the user's decision.
    free_fields = make_list_of_free_fields(board)
    while True:
        try:
            move = int(input("Enter your move (1-9): "))
            if move < 1 or move > 9 or move not in free_fields:
                raise TTT_Invalid_Input
        except Exception as e:
            print(e)
        else:
            break
    save_move_to_board(board, move, 'O')
    print("You placed your move at " + str(move) + '!')

def computer_move(board):
    # The function draws the computer's move and updates the board.
    free_fields = make_list_of_free_fields(board)
    move = randrange(1,10)
    while move not in free_fields:
        move = randrange(1,10)
    save_move_to_board(board, move, 'X')
    print("The computer placed its move at " + str(move) + '!')

def victory_for(board, sign):
    # The function analyzes the board status in order to check if 
    # the player using 'O's or 'X's has won the game
    for i in range(3):
        if (board[i][0] == board[i][1] == board[i][2] == sign) or (board[0][i] == board[1][i] == board[2][i] == sign):
            return True
    if (board[0][0] == board[1][1] == board[2][2] == sign) or (board[0][2] == board[1][1] == board[2][0] == sign):
        return True
    return False

def next_player(sign):
    return 'O' if sign == 'X' else 'X'

def enter_move(board, sign):
    player_move(board) if sign == 'O' else computer_move(board)

def main():
    print("Welcome to Tic-Tac-Toe!")

    # Game loop, loops when a game is finished and to start a new game
    while True:
        sign = choice(['O', 'X'])
        board = [[(col + (row * 3)) for col in range(1,4)] for row in range(3)]
        if sign == 'O':
            display_board(board)
        # Turn loop, loops each turn
        while len(make_list_of_free_fields(board)) > 0:
            if make_list_of_free_fields(board) == []:
                print("It's a draw~")
                break
            enter_move(board, sign)
            display_board(board)
            if victory_for(board, sign):
                print("You win!") if sign == 'O' else print("You lose!")
                break
            sign = next_player(sign)
        if not input("< Press enter to play another game >") == '':
            break

main()