#    Main Author(s): Vincent Le
#    Main Reviewer(s): Devon Chan, Foad Ozgoli

from a1_partc import Queue

# This function will receive a 2D array of numbers as a parameter. 
# It will identify if the grid cell contains any numbers that are greater than or equal to the number of neighboring cells.
# It will return a list of tuples, representing the coordinates/indexs of the cell that is currently overflowing.
# The function will return 'None' if there is now overflowing numbers.

def get_overflow_list(grid):
    overflow_list = []
    rows = len(grid)
    cols = len(grid[0])

    for r in range(rows):
        for c in range(cols):
            value = abs(grid[r][c])
            neighbors = (r > 0) + (r < rows - 1) + (c > 0) + (c < cols - 1)
            if value >= neighbors:
                overflow_list.append((r, c))
    if not overflow_list:
        return None

    return overflow_list


# This function will receive a 2D array of numbers and a Queue object as a parameter.
# It will identify if any cell is overflowing and will update the grid accordingly.
# The function will set the current cell to 0 and adds 1 to any neighboring cell.
# It will add the new grid to the back of the queue.
# The function will run until there is no more overflowing cells and will return the number of times the function has ran.

def overflow(grid, queue):
    overflow_list = get_overflow_list(grid)
    count = 1
    # A3 additions
    if overflow_list is None:
        return 0

    # Check if all values have the same sign
    same_sign = True

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] >= 0:
                continue
            else:
                same_sign = False
                break
        if not same_sign:
            break
    else:
        same_sign = True
        
    if same_sign:
        queue.enqueue(grid)
        return (count-1)
    # End A3 additions
    grid_copy = [row[:] for row in grid]

    for i in range(len(overflow_list)):
        is_negative = grid_copy[overflow_list[i][0]][overflow_list[i][1]] < 0
        grid_copy[overflow_list[i][0]][overflow_list[i][1]] = 0

    for i in range(len(overflow_list)):
        row, col = overflow_list[i]

        if row + 1 < len(grid):
            grid_copy[row+1][col] = abs(grid_copy[row+1][col]) + 1
            if is_negative:
                grid_copy[row+1][col] *= -1

        if col + 1 < len(grid[0]):
            grid_copy[row][col+1] = abs(grid_copy[row][col+1]) + 1
            if is_negative:
                grid_copy[row][col+1] *= -1

        if row - 1 >= 0:
            grid_copy[row-1][col] = abs(grid_copy[row-1][col]) + 1
            if is_negative:
                grid_copy[row-1][col] *= -1

        if col - 1 >= 0:
            grid_copy[row][col-1] = abs(grid_copy[row][col-1]) + 1
            if is_negative:
                grid_copy[row][col-1] *= -1

    queue.enqueue(grid_copy)

    if get_overflow_list(grid_copy) is not None:
        return overflow(grid_copy, queue) + 1
    else:
        return count
