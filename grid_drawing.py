from time import sleep
import matplotlib.pyplot as plt
from matplotlib import colors
import PySimpleGUI as sg
from tgol import next_board_state

"""
# Render function to print each board state to command line
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

"""
# Render function using matplotlib grid
"""
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

"""
# Render function using pysimplegui grid
# TODO: Implement GUI to render board state to user using pysimplegui
"""
def gui_render(board, width, height):
    CELL_SIZE = 25
    next_board = board
    total_cells_width = width // CELL_SIZE
    total_cells_height = height // CELL_SIZE

    layout = [  [sg.Text('Drawing on a %dx%d Grid' % (total_cells_width, total_cells_height))],
                [sg.Graph((width, height), (0,0), (width, height), background_color='black', drag_submits=True, key='GRAPH')],
                [sg.Button('Start'), sg.Button('Pause'), sg.Button('Random'), sg.Button('Blank')]
    ]

    window = sg.Window('My new window').Layout(layout)
    graph = window['GRAPH']
    window.Finalize()

    #FIXME Board state updating not working
    # Currently only outputts the initial random board state from the first call and then doesn't update

    while True:
        event, values = window.Read(timeout=10)

        for i in range(total_cells_height + 1):
            for j in range(total_cells_width + 1):
                top_left = (j*25, i*25+25)
                bot_right = (j*25+25, i*25)
                if board[i][j] == 1:
                    graph.DrawRectangle(top_left, bot_right, fill_color='white', line_color='white')
                else:
                    graph.DrawRectangle(top_left, bot_right, fill_color='black', line_color='black')
        next_board = next_board_state(next_board, width, height)
            

    
    window.close()
