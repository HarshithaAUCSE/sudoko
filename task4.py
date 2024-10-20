# Function to print the Sudoku grid
def print_grid(grid):
    for row in grid:
        print(" ".join(str(cell) for cell in row))

# Function to find an empty cell (represented by 0)
def find_empty(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return (i, j)  # row, col
    return None

# Function to check if a number is valid in the current position
def is_valid(grid, num, pos):
    row, col = pos
    
    # Check row
    if any(grid[row][i] == num for i in range(9)):
        return False
    
    # Check column
    if any(grid[i][col] == num for i in range(9)):
        return False
    
    # Check 3x3 box
    box_x = col // 3
    box_y = row // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if grid[i][j] == num:
                return False
    
    return True

# Backtracking algorithm to solve Sudoku
def solve_sudoku(grid):
    empty = find_empty(grid)
    
    if not empty:
        return True  # No more empty spaces, puzzle solved
    
    row, col = empty
    
    # Try placing numbers 1 to 9
    for num in range(1, 10):
        if is_valid(grid, num, (row, col)):
            grid[row][col] = num  # Tentatively place the number
            
            if solve_sudoku(grid):  # Recursively try to solve the rest
                return True
            
            grid[row][col] = 0  # Backtrack and try another number
    
    return False  # Trigger backtracking

# Example Sudoku puzzle (0 represents empty cells)
sudoku_grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print("Sudoku Puzzle:")
print_grid(sudoku_grid)

# Solve the Sudoku puzzle
if solve_sudoku(sudoku_grid):
    print("\nSudoku Solved:")
    print_grid(sudoku_grid)
else:
    print("No solution exists for the given Sudoku.")
