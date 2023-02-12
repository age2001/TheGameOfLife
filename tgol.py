from random import random, seed
from time import sleep
from os import system
#from GridDrawing import renderPlot

import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np

def dead_state(width, height):
    dead_board = []
    for i in range(height):
        dead_board.append([0] * width)
    return dead_board

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

def next_board_state(current_board, width, height):
    new_board = []

    for i in range(height):
        new_board.append([0] * width)

    for y in range(0, height):
        for x in range(0, width):
            new_board[y][x] = check_neighbors(x, y, width - 1, height - 1, current_board)

    return new_board

def check_neighbors(x, y, maxX, maxY, board):
    total_cells = 0
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



    for cell in neighbor_cells:
        if cell == 1:
            total_cells += 1

    #Any live cell with 0 or 1 live neighbors becomes dead, because of underpopulation
    #Any live cell with 2 or 3 live neighbors stays alive, because its neighborhood is just right
    #Any live cell with more than 3 live neighbors becomes dead, because of overpopulation
    #Any dead cell with exactly 3 live neighbors becomes alive, by reproduction

    if board[y][x] == 1 and total_cells == 0:
        return 0
    elif board[y][x] == 1 and total_cells == 1:
        return 0
    elif board[y][x] == 1 and total_cells == 2:
        return 1
    elif board[y][x] == 1 and total_cells == 3:
        return 1
    elif board[y][x] == 0 and total_cells == 3:
        return 1
    else:
        return 0

def render(board):
    width = len(board[0])
    print((width + 2) * '-')
    for row in board:
        line = '|'
        for cell in row:
            if cell == 1:
                line += '0'
            else:
                line += ' '
        line += '|'
        print(line)
    print((width + 2) * '-')
    sleep(0.5)

def renderPlot(board, width, height):
    first = True
    data = board

    # create discrete colormap
    cmap = colors.ListedColormap(['black', 'white'])
    bounds = [0, 1, 2]
    norm = colors.BoundaryNorm(bounds, cmap.N)

    fig, ax = plt.subplots()
    ax.imshow(data, cmap=cmap, norm=norm)

    # draw gridlines
    #ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=1.5)
    #ax.set_xticks(np.arange(-.5, width, 1));
    #ax.set_yticks(np.arange(-.5, height, 1));
    #ax.set_yticklabels([])
    #ax.set_xticklabels([])
    plt.xticks([])
    plt.yticks([])


    while True:
        if first:
            plt.show(block = False)
            plt.pause(0.1)
            first = False
        else:
            data = next_board_state(data, width, height)
            ax.clear()
            plt.xticks([])
            plt.yticks([])
            ax.imshow(data, cmap=cmap, norm=norm)
            plt.pause(0.1)

#       Cell Board Guide
#    topLeft  | board[y-1][x-1]
#    topMid   | board[y-1][x]
#    topRight | board[y-1][x+1]
#    midLeft  | board[y][x-1]
#    midRight | board[y][x+1]
#    botLeft  | board[y+1][x-1]
#    botMid   | board[y+1][x]
#    botRight | board[y+1][x+1]


#                   ----------------Test Code-----------------

"""
width = 15
height = 15
first = True
while True:
    if first:
        board = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        renderPlot(board, width, height)
        first = False
    else:
        board = next_board_state(board, width, height)
        renderPlot(board, width, height)
"""

#                  ----------------Main Code----------------

width = 50
height = 50
first = True

renderPlot(random_state(width, height), width, height)

#while True:
#    if first:
#        board = random_state(width, height)
#        renderPlot(board, width, height, first)
#        first = False
#    else:
#        board = next_board_state(board, width, height)
#        renderPlot(board, width, height, first)