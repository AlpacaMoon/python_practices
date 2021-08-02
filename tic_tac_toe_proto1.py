from random import randrange

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    for row in range(3):
        print("+-------+-------+-------+")
        print("|       |       |       |")
        for col in range(3):
            print("|   ", end = "")
            if board[row][col] == 'N':
                print((row * 3) + col + 1, end = "")
            else:
                print(board[row][col], end = "")
            print("   ", end = "")
        print("|\n|       |       |       |")
    
    print("+-------+-------+-------+")

def enter_move(board):
    # The function accepts the board current status, asks the user about their move, 
    # checks the input and updates the board according to the user's decision.
    free = make_list_of_free_fields(board)
    move = int(input("Enter your move: "))
    while True:
        while move <= 0 or move >= 10:
            move = int(input("Invalid input, please re-enter your move: "))
        
        row = (move - 1) // 3        
        col = (move - 1) % 3
        print((row, col), free)
        if (row, col) in free:
            break
        else:
            move = int(input("The box is already occupied, please re-enter: "))
    board[row][col] = 'O'

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == 'N':
                free.append((row, col))
    return free

def victory_for(board, sign):
    # The function analyzes the board status in order to check if 
    # the player using 'O's or 'X's has won the game
    for i in range(3):
        if  board[i][0] == board[i][1] == board[i][2] == sign or \
            board[0][i] == board[1][i] == board[2][i] == sign:
            return True
    if  board[0][0] == board[1][1] == board[2][2] == sign or \
        board[0][2] == board[1][1] == board[2][0] == sign:
        return True
    return False

def draw_move(board):
    # The function draws the computer's move and updates the board.
    while True:
        row, col = randrange(3), randrange(3)
        if (row, col) in make_list_of_free_fields(board):
            board[row][col] = 'X'
            return

board = [
    ['N', 'N', 'N'], 
    ['N', 'X', 'N'], 
    ['N', 'N', 'N'], 
]
sign = 'X'

display_board(board)
while True:
    sign = 'O'
    enter_move(board)
    display_board(board)
    if victory_for(board, sign):
        break

    sign = 'X'
    draw_move(board)
    display_board(board)
    if victory_for(board, sign):
        break

if sign == 'O':
    print("You won!")
else:
    print("You lose! :)")