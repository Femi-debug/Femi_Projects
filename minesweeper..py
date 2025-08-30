def make_grid(grid):
    for row in grid:           
        print(row)

# Example grid
sample_grid = [
    ['#', '-', '-'],
    ['-', '#', '#'],
    ['#', '-', '-'],
    ['-', '#', '-']
]

print("minesweeper grid: ")
make_grid(sample_grid)