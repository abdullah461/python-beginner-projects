def find_next_empty(puzzle):
    # finds the next row, col on the puzzle thats not filled yet --> represent with -1
    # return col, row tuple (or (None, None) if there is none)

    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r,c
            
    return None, None   # if no spaces in the puzzle are empty (-1)

def  is_valid(puzzle, guess, row, col):
    # figures out whether the guess at row and col of puzzle is valid guess
    # returns true if its valid else false
    
    # lets start with row
    row_vals = puzzle[row]
    if guess in row_vals:
        return False

    # the column
    # col_vals = []
    # for i in range(9):
    #     col_vals.append(puzzle[i][col])

    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False

    # we want to gw 3x3 square starts
    # and iterate
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False
    return True

def solve_soduku(puzzle):
    # solve soduku using backtracking!
    # our puzzle is a list of lists, where each inner list is a row in our soduku puzzle
    # return whether a solution (if solution exists)
                    
    # step 1: choose somewhere on the puzzle to make a guess

    row, col = find_next_empty(puzzle)

    # step 1:1 if theres nowwhere left
    if row is None:
        return True

    #step 2: if there is a place to put a number, then make a guess bte 1 and 9
    for guess in range (1,10):
        # check if guess is valid
        if is_valid(puzzle, guess, row, col):
            # step 3
            puzzle[row][col] = guess

            # now recurese using the puzzle
            # step 4: recursively call the function
            if solve_soduku(puzzle):
                return True

            # step 5: if gues doesnt solve puzzle then backtrack and try new number
            puzzle[row][col] = -1 #reset them guess

    # step 6: if numbers tried didnt work then puzzle unsolvable!
    return False

if __name__ == '__main__':
    example_board = [
        [3, 9, -1,      -1,5,-1,   -1,-1,-1],
        [-1, -1, -1,    2,-1,-1,   -1,-1,5],
        [-1, -1, -1,    7,1,9,   -1,8,-1],

        [-1, 5, -1,    -1,6,8,   -1,-1,-1],
        [2, -1, 6,    -1,-1,3,   -1,-1,-1],
        [-1, -1, -1,    -1,-1,-1,   -1,-1,4],

        [5, -1, -1,    -1,-1,-1,   -1,-1,-1],
        [6, 7, -1,    -1,-1,5,   -1,4,-1],
        [1, -1, 9,    -1,-1,-1,   2,-1,-1],

    ]

    print(solve_soduku(example_board))
    print(example_board)