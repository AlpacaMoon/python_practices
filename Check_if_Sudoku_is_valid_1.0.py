
sudoku = ['', '', '', '', '', '', '', '', '']
for i in range(len(sudoku)):
    sudoku[i] = input("Enter row " + str(i + 1) + ':')

def validSudoku(sudoku):
    #Check for rows
    for row in sudoku:
        if ''.join(sorted(row)) != '123456789':
            print('a')
            return False
    
    #Check for columns
    for i in range(9):
        substr = ''
        for row in sudoku:
            substr += row[i]
        if ''.join(sorted(row)) != '123456789':
            print('b')
            return False

    #Check for 3x3
    for i in range(3):
        for j in range(3):
            substr = ''
            for k in range(3):
                substr += sudoku[(i*3) + k][(j*3) : (j*3)+3]
            if ''.join(sorted(row)) != '123456789':
                print('c')
                return False

    return True
    
print(validSudoku(sudoku))

# sudoku[0][0:3] + sudoku[1][0:3] + sudoku[2][0:3]
# sudoku[0][3:6] + sudoku[1][3:6] + sudoku[2][3:6]
# sudoku[0][6:9] + sudoku[1][6:9] + sudoku[2][6:9]

# sudoku[3][0:3] + sudoku[4][0:3] + sudoku[5][0:3]
# sudoku[3][3:6] + sudoku[4][3:6] + sudoku[5][3:6]
# sudoku[3][6:9] + sudoku[4][6:9] + sudoku[5][6:9]

# sudoku[6][0:3] + sudoku[7][0:3] + sudoku[8][0:3]
# sudoku[6][3:6] + sudoku[7][3:6] + sudoku[8][3:6]
# sudoku[6][6:9] + sudoku[7][6:9] + sudoku[8][6:9]