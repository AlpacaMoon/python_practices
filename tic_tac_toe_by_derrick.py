#1
import random

def display_board(board):
   print('+-------+-------+-------+')
   for i in range(3):
       print('|       |       |       |')
       print('|',board[i][0],'|',board[i][1],'|',board[i][2],'|',sep='   ')
       print('|       |       |       |')
       print('+-------+-------+-------+')


def enter_move(board):
    # The function accepts the board current status, asks the user about their move, 
    # checks the input and updates the board according to the user's decision.
    while True:
        move=int(input('Enter move in range 1-9:'))
        if move <1 or move > 9:
            print('Invalid input. Enter move in range 1-9:')
        else:
            if board[(move-1)//3][(move%3)-1] not in ['X','O']:
                board[(move-1)//3][(move%3)-1]= 'O'
                break
            else:
                print('Invalid move as space is occupied, enter another move in range 1-9:')


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    lst=[]
    for r in range(3):
        for c in range(3):
            if board[r][c] not in ['X','O']:
                lst.append((r,c))
    return lst

def victory_for(board, sign):
    # The function analyzes the board status in order to check if 
    # the player using 'O's or 'X's has won the game
    for r in range(3):
        if board[r][0]== board[r][1]==board[r][2]==sign:
            return sign
    for c in range(3):
        if board[0][c] == board[1][c]==board[2][c]==sign:
            return sign
    if (board[0][0] == board[1][1] == board[2][2]==sign) or board[0][2]== board[1][1]==board[2][0]==sign:
        return sign


def draw_move(board):
    move_made=False
    while move_made == False:
        move = random.randrange(10)
        if board[(move-1)//3][(move%3)-1] not in ['X','O']:
            board[(move-1)//3][(move%3)-1]= 'X'
            move_made = True
        
def main():
    board=[[x+(3*y) for x in range(1,4)] for y in range(3)]
    board[1][1]='X'
    while True:
        if len(make_list_of_free_fields(board))>0:
            display_board(board)
            enter_move(board)
            if victory_for(board,'O') =='O':
                display_board(board)
                print('Player O has won!')
                break
            draw_move(board)
            display_board(board)
            if victory_for(board,'X')=='X':
                display_board(board)
                print('Player X has won!')
                break
        else:
            print("Game is drawn!")
            break

main()
