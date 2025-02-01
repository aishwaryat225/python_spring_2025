def print_sudoku(grid):
    """Function to print the Sudoku grid"""
    for row in grid:
        print(" ".join(str(num) if num != 0 else '.' for num in row))
    print("\n")


def is_valid(grid, row, col, num):
    """Check if num can be placed at grid[row][col]"""
    for i in range(9):
        if grid[row][i] == num or grid[i][col] == num:
            return False
    
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False
    
    return True


def find_empty_cell(grid):
    """Find an empty cell in the Sudoku grid"""
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i, j
    return None


def solve_sudoku(grid):
    """Solve Sudoku using backtracking algorithm"""
    empty_cell = find_empty_cell(grid)
    if not empty_cell:
        return True
    
    row, col = empty_cell
    for num in range(1, 10):
        if is_valid(grid, row, col, num):
            grid[row][col] = num
            if solve_sudoku(grid):
                return True
            grid[row][col] = 0  # Backtrack
    
    return False


if __name__ == "__main__":
    sudoku_puzzle = [
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
    print_sudoku(sudoku_puzzle)
    
    if solve_sudoku(sudoku_puzzle):
        print("Solved Sudoku:")
        print_sudoku(sudoku_puzzle)
    else:
        print("No solution exists!")
