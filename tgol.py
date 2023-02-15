"""
# The Game of Life Algorithm
# Adjustments to the rules for the cells can be made in function cell_state()
"""

from random import random

"""
# Function creates initial board state with every cell set to "dead" (0)
# Returns board (array of arrays)
"""
def dead_state(width, height):
    dead_board = []
    for i in range(height):
        dead_board.append([0] * width)
    return dead_board

"""
# Function randomizes the state of each cell on creation
# Returns int
"""
def random_state(width, height):
    state = dead_state(width, height)

    for row in range(len(state)):
        for cell in range(len(state[row])):
            random_number = random()
            if random_number >= 0.5:
                state[row][cell] = 0
            else:
                state[row][cell] = 1
    return state

"""
# Function to calculate the next board state from current parameters
# Returns board (array of arrays)
"""
def next_board_state(current_board, width, height):
    new_board = []

    for i in range(height):
        new_board.append([0] * width)

    for y in range(0, height):
        for x in range(0, width):
            new_board[y][x] = check_neighbors(x, y, width - 1, height - 1, current_board)

    return new_board

"""
# Helper function that checks whether a cell is dead or alive (0 or 1) for next board state
# Returns int
# TODO: Implement GUI for user changing cell rules
"""
def cell_state(x, y, board, total_neighbor_cells):
    # Any live cell with 0 or 1 live neighbors becomes dead, because of underpopulation
    # Any live cell with 2 or 3 live neighbors stays alive, because its neighborhood is just right
    # Any live cell with more than 3 live neighbors becomes dead, because of overpopulation
    # Any dead cell with exactly 3 live neighbors becomes alive, by reproduction
    if board[y][x] == 1:
        match total_neighbor_cells:
            case 0:
                return 0
            case 1:
                return 0
            case 2:
                return 1
            case 3:
                return 1
            case _:
                return 0
    else:
        match total_neighbor_cells:
            case 3:
                return 1
            case _:
                return 0

"""
# Helper function to check the state of the neighbors 3x3 around a cell
# Neighbor cells depends on if the cell is on the border, or in the middle of the grid
# Returns int
#        
#       Cell Board Guide
#    topLeft  | board[y-1][x-1]
#    topMid   | board[y-1][x]
#    topRight | board[y-1][x+1]
#    midLeft  | board[y][x-1]
#    midRight | board[y][x+1]
#    botLeft  | board[y+1][x-1]
#    botMid   | board[y+1][x]
#    botRight | board[y+1][x+1]    
"""
def check_neighbors(x, y, maxX, maxY, board):
    total_neighbor_cells = 0
    if x == 0:
        if y == 0:
            neighbor_cells = [board[y][x+1], board[y+1][x], board[y+1][x+1]]
        elif y == maxY:
            neighbor_cells = [board[y][x+1], board[y-1][x], board[y-1][x+1]]
        else:
            neighbor_cells = [board[y-1][x], board[y-1][x+1], board[y][x+1], board[y+1][x], board[y+1][x+1]]

    elif x == maxX:
        if y == 0:
            neighbor_cells = [board[y][x-1], board[y+1][x], board[y+1][x-1]]
        elif y == maxY:
            neighbor_cells = [board[y][x-1], board[y-1][x-1], board[y-1][x]]
        else:
            neighbor_cells = [board[y-1][x], board[y-1][x-1], board[y][x-1], board[y+1][x-1], board[y+1][x]]

    else:
        if y == 0:
            neighbor_cells = [board[y][x-1], board[y][x+1], board[y+1][x-1], board[y+1][x], board[y+1][x+1]]
        elif y == maxY:
            neighbor_cells = [board[y-1][x-1], board[y-1][x], board[y-1][x+1], board[y][x-1], board[y][x+1]]
        else:
            neighbor_cells = [board[y-1][x-1], board[y-1][x], board[y-1][x+1], board[y][x-1], board[y][x+1], board[y+1][x-1], board[y+1][x], board[y+1][x+1]]


    # Counting the number of living cells surrounding a particular cell    
    for cell in neighbor_cells:
        if cell == 1:
            total_neighbor_cells += 1

    return cell_state(x, y, board, total_neighbor_cells)