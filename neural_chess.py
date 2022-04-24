import itertools
import numpy as np

moves = [[-2, -2, -1, -1, 1, 1, 2, 2],
         [-1, 1, -2, 2, -2, 2, -1, 1]]

moves = [(1, -2), (2, -1), (2, 1), (1, 2),
         (-1, 2), (-2, 1), (-2, -1), (-1, -2)]

board_size = (5, 5)
rows = [*range(board_size[0])]
cols = [*range(board_size[1])]


board_array = [['' for _ in range(board_size[0])]
               for _ in range(board_size[1])]


for i, j in itertools.product(range(board_size[0]), range(board_size[1])):
    position = [i, j]
    board_array[i][j] = position

print(board_array)


# print(moves[0])
# for i in range(8):
#    print((moves[0][i], moves[1][i]))

# move_array = [[(moves[0][i], moves[1][i]) for i in range(8)]
#              for _ in range(64)]


for i, j, move in itertools.product(range(board_size[0]), range(board_size[1]), moves):
    #print(j, j, moves)
    print(board_array[i][j])
    #print(board_array[i][j] * [-1, -1])
    print([sum(x) for x in zip(board_array[i][j], move)])
    print("===========================================================")
    #new_positions = board_array[i, j] + (move[0][move], move[1][move])
    #print(i, j)
    # for move in range(8):
    #    new_position = board_array.copy()
    #    new_position[i][j] = new_position[i][j] + \
    #        [moves[0][move], moves[1][move]]
    #    print(new_position)
    #    print("===========================================================")
