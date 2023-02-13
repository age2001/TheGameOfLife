from time import sleep
import matplotlib.pyplot as plt
from matplotlib import colors
import PySimpleGUI as sg
from tgol import next_board_state

"""
# Render implementation to print each new board state to the command line.
"""
def cl_render(board):
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

def plt_render(board, width, height):
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

def gui_render(board):
    pass
