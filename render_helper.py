from random import choice

"""
# Helper function to pysimplegui render function for drawing the next state on the window graph
"""
def cell_gui_render(board, graph, cells_width, cells_height, cell_size):
    for i in range(cells_height + 1):
                for j in range(cells_width + 1):
                    top_left = (j * cell_size, i * cell_size + cell_size)
                    bot_right = (j * cell_size + cell_size, i * cell_size)
                    if board[i][j] == 1:
                        # color = random_color()
                        color = 'white'
                        graph.DrawRectangle(top_left, bot_right, fill_color= color, line_color = color)
                    else:
                        graph.DrawRectangle(top_left, bot_right, fill_color='black', line_color='black')

def random_color():
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
    return choice(colors)