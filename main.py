from tgol import random_state
from grid_drawing import plt_render, gui_render

#TODO: Create gui for user to enter board size
def main():
    width = 900
    height = 900
    CELL_SIZE = 5

    # plt_render(random_state(width, height), width, height)
    gui_render(random_state(width, height), width, height, CELL_SIZE)

if __name__ == '__main__':
    main()