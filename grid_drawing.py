from time import sleep
import matplotlib.pyplot as plt
from matplotlib import colors
import PySimpleGUI as sg
from tgol import next_board_state, random_state, dead_state
from render_helper import cell_gui_render

"""
# Board render function to print each board state to command line
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
# Board render function using matplotlib grid
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
# Board render function using pysimplegui grid
"""
def gui_render(board, width, height, cell_size):
    next_board = board
    total_cells_width = width // cell_size
    total_cells_height = height // cell_size

    layout = [  [sg.Text('Drawing on a %dx%d Grid' % (total_cells_width, total_cells_height))],
                [sg.Button('Start'), sg.Button('Pause'), sg.Button('Random'), sg.Button('Blank'), sg.Button('Exit')],
                [sg.Graph((width, height), (0,0), (width, height), background_color='black', drag_submits=True, key='GRAPH')],
    ]

    window = sg.Window('The Game of Life').Layout(layout)
    graph = window['GRAPH']

    keep_playing = False

    while True:
        event, values = window.Read(timeout=0.001)            

        if event == 'Start':
            keep_playing = True

        if event == 'Pause':
            keep_playing = False

        if event == 'Exit' or event == sg.WINDOW_CLOSED:
            break

        if event == 'Random':
            next_board = random_state(width, height)
            cell_gui_render(next_board, graph, total_cells_width, total_cells_height, cell_size)
            continue

        if event == 'Blank':
            next_board = dead_state(width, height)
            cell_gui_render(next_board, graph, total_cells_width, total_cells_height, cell_size)
            continue
        
        if keep_playing:
            next_board = next_board_state(next_board, width, height)
            graph.erase()
            cell_gui_render(next_board, graph, total_cells_width, total_cells_height, cell_size)
    
    window.close()
