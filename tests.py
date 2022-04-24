import backtrack_knight
import itertools
import pandas as pd
import numpy as np
from datetime import datetime


board_size = 8
for board_size in range(9, 12, 1):
    data = pd.DataFrame(columns=['function', 'board_size', 'start_position',
                                 'start', 'end', 'time', 'calculations', 'moves', 'solved'])
    # step is 2 if the board is odd, 1 if even
    #step = 2 if board_size % 2 == 1 else 1
    step = 1
    positions = [0, board_size-1]
    #positions = [0, 0]
    # for i, j in itertools.product(positions, positions):
    start = datetime.now()
    position = (0, 0)
    print(board_size)
    print(position)
    board, total_moves, total_calculations = backtrack_knight.knights_tour(
        board_size, position, False)
    end = datetime.now()
    print(board)
    print(total_moves)
    print(end - start)
    line = {'function': 'backtrack_knight',
            'board_size': board_size,
            'start_position': position,
            'start': start,
            'end': end,
            'time': end - start,
            'calculations': total_calculations,
            'moves': total_moves,
            'solved': board[0][0] != -1}

    data = data.append(line, ignore_index=True)

    print(data)
    data.to_csv('backtrack_knight.csv', mode='a', header=False)
