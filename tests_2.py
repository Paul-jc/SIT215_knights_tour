import chess_animation_3
import itertools
import pandas as pd
import numpy as np
from datetime import datetime


for board_size, method in itertools.product(range(6, 12, 1), [0, 1]):
    data = pd.DataFrame(columns=['function', 'board_size', 'start_position',
                                 'start', 'end', 'time', 'calculations', 'moves', 'solved'])
    # step is 2 if the board is odd, 1 if even
    #step = 2 if board_size % 2 == 1 else 1
    step = 1
    #positions = [0, board_size-1]
    # for i, j in itertools.product(positions, positions):
    start = datetime.now()
    position = [0, 0]
    #position = (i, j)
    print(board_size)
    print(position)
    kt = chess_animation_3.KnightsTour(board_size, board_size)
    path = []
    kt.tour(1, path, position, method, True)
    end = datetime.now()
    board = kt.board
    total_moves = kt.total_moves
    total_calculations = kt.total_calculations
    path_found = kt.path_found
    print(board)
    print(total_moves)
    print(end - start)
    line = {'function': 'warnsdorffs_heuristic' if method == 1 else 'state_space_search',
            'board_size': board_size,
            'start_position': position,
            'start': start,
            'end': end,
            'time': end - start,
            'calculations': total_calculations,
            'moves': total_moves,
            'solved': path_found}

    data = data.append(line, ignore_index=True)

    print(data)
    data.to_csv('knight.csv', mode='a', header=False)
