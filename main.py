from tgol import random_state
from grid_drawing import plt_render

def main():
    width = 100
    height = 100

    plt_render(random_state(width, height), width, height)

if __name__ == "__main__":
    main()