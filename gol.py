import numpy as np
import time
import random
import os
import sys

len_y = 30
len_x = 90

def print_board(b):
    os.system('cls')
    output = ""
    for y in range(len_y):
        for x in range(len_x):
            state = b[y, x]
            if state:
                output += "x"
            else:
                output += " "
        output += "\n"

    print(output, flush=True)


def gol_rules(cell_is_alive, num_neighbours):
    if num_neighbours < 2:
        return False
    if cell_is_alive and (num_neighbours == 2 or num_neighbours == 3):
        return True
    if num_neighbours > 3:
        return False
    if not cell_is_alive and num_neighbours == 3:
        return True

    return False


def alive_neighbours(board, y, x):
    x_left = x-1
    if x_left < 0:
        x_left = 0

    x_right = x+1
    if x_right >= len_x:
        x_right = x

    y_top = y-1
    if y_top < 0:
        y_top = 0

    y_bottom = y+1
    if y_bottom >= len_y:
        y_bottom = y

    alive_counter = 0
    for i in range(x_left, x_right+1):
        for j in range(y_top, y_bottom+1):
            alive_counter += int(board[j, i])

    if board[y, x]:
        alive_counter -= 1

    return alive_counter

def addGlider(i, j, board):
    """adds a glider with top-left cell at (i, j)"""
    glider = np.array([[False, True, False],
                       [False, False, True],
                       [True, True, True]])
    board[i:i+3, j:j+3] = glider

def init_random(board):
    if not glider:
        for y in range(len_y):
            for x in range(len_x):
                board[y, x] = random.randint(0, 1)
    else:
        for y in range(len_y):
            for x in range(len_x):
                board[y, x] = random.randint(0, 0)
        addGlider(5, 5, board)
        
    
glider = False
if __name__ == '__main__':
    if len(sys.argv) > 1:
        glider = sys.argv[1] == "--glider"

    game_board = np.empty((len_y, len_x), dtype=bool)
    new_board = np.empty((len_y, len_x), dtype=bool)
    init_random(game_board)
    print_board(game_board)

    while True:
        for y in range(len_y):
            for x in range(len_x):
                neighbours_count = alive_neighbours(game_board, y, x)
                is_alive = game_board[y, x]
                new_cell = gol_rules(is_alive, neighbours_count)
                new_board[y, x] = new_cell
        print_board(new_board)
        game_board = new_board.copy()
        time.sleep(0.25)


