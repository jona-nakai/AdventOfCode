import sys
import copy

def remove_roll(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '@':
                surrounding_rolls = 0
                offsets = [[-1, -1],
                           [-1, 0],
                           [-1, 1],
                           [0, -1],
                           [0, 1],
                           [1, -1],
                           [1, 0],
                           [1, 1]]
                for offset in offsets:
                    if all([0 <= i + offset[0] <= len(grid) - 1,
                            0 <= j + offset[1] <= len(grid[i]) - 1]):
                        if grid[i + offset[0]][j + offset[1]] == '@':
                            surrounding_rolls += 1

                if surrounding_rolls < 4:
                    grid[i][j] = '.'
                    return grid
    return grid

def main(grid):
    removed_rolls = 0
    while True:
        initial_grid = copy.deepcopy(grid)
        grid = remove_roll(grid)
        if initial_grid == grid:
            break
        else:
            removed_rolls += 1
    return removed_rolls

if __name__ == "__main__":
    filename = sys.argv[1]
    with open(filename) as f:
        content = f.read()
        content_split = content.split('\n')[:-1]
        content_split_completely = list()
        for s in content_split:
            content_split_completely.append(list(s))
        
        grid = content_split_completely

        print(main(grid))
