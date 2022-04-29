import sys
import pygame
from random import randint


# Colors for use throughout the visualisation
class Colors:
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)


# Images used to build the visulisation
class Images():
    def __init__(self,
                 white_square=pygame.image.load("black-square-100.png"),
                 blue_square=pygame.image.load("blue-square.png"),
                 knight=pygame.image.load("red_knight.png")):  # Image sourced from https://www.kindpng.com/downpng/hJimihJ_knight-in-red-clip-art-at-clker-red/
        self.white_square = white_square
        self.blue_square = blue_square
        self.knight = knight


# Chessboard parameters
class ChessBoard():
    def __init__(self, columns, rows, size, initial_position, current_position, transited):
        self.columns = columns
        self.rows = rows
        self.size = width, height = (rows * 100), (columns * 100)
        self.initial_position = initial_position
        self.current_position = self.initial_position
        self.transited = transited


# Checks if the user input is valid
def check_user_input(input):
    try:
        # Convert it into integer
        val = int(input)
    except ValueError:
        try:
            # Convert it into float
            val = float(input)
            print("Input is a float  number. Number = ", val)
        except ValueError:
            print("No.. input is not a number. It's a string")


# Check if starting position is on the board
def check_starting_pos_input(chessboard):
    if chessboard.initial_position[0] > chessboard.columns or chessboard.initial_position[1] > chessboard.rows:
        print("Invalid starting position. Please enter a valid starting position")
        sys.exit()


# Get the size of the board from the user and the starting position of the knight
def get_board_size():
    columns = int(input("Enter the number of columns: "))
    check_user_input(columns)
    rows = int(input("Enter the number of rows: "))
    check_user_input(rows)
    starting_column = int(input("Enter the starting column: "))
    check_user_input(starting_column)
    starting_row = int(input("Enter the starting row: "))
    check_user_input(starting_row)

    chessboard = ChessBoard(rows=rows,
                            columns=columns,
                            size=(columns*100, rows*100),
                            initial_position=[
                                starting_column-1, starting_row-1],
                            current_position=[
                                starting_column-1, starting_row-1],
                            transited=[])
    check_starting_pos_input(chessboard)
    return chessboard


def move_one(chessboard):  # right one, down two
    if chessboard.current_position[0] + 1 <= chessboard.columns-1 and chessboard.current_position[1] + 2 <= chessboard.rows-1 and [chessboard.current_position[0] + 1, chessboard.current_position[1] + 2] not in chessboard.transited:
        chessboard.current_position = [
            chessboard.current_position[0] + 1, chessboard.current_position[1] + 2]
    return chessboard


def check_move_one(chessboard):
    return chessboard.current_position[0] + 1 <= chessboard.columns - 1 and chessboard.current_position[1] + 2 <= chessboard.rows - 1 and [chessboard.current_position[0] + 1, chessboard.current_position[1] + 2] not in chessboard.transited


def move_two(chessboard):  # right two, down one
    if chessboard.current_position[0] + 2 <= chessboard.columns-1 and chessboard.current_position[1] + 1 <= chessboard.rows-1 and [chessboard.current_position[0] + 2, chessboard.current_position[1] + 1] not in chessboard.transited:
        chessboard.current_position = [
            chessboard.current_position[0] + 2, chessboard.current_position[1] + 1]
    return chessboard


def check_move_two(chessboard):
    return chessboard.current_position[0] + 2 <= chessboard.columns - 1 and chessboard.current_position[1] + 1 <= chessboard.rows - 1 and [chessboard.current_position[0] + 2, chessboard.current_position[1] + 1] not in chessboard.transited


def move_three(chessboard):  # right two, up one
    if chessboard.current_position[0] + 2 <= chessboard.columns - 1 and chessboard.current_position[1] >= 1 and [chessboard.current_position[0] + 2, chessboard.current_position[1] - 1] not in chessboard.transited:
        chessboard.current_position = [
            chessboard.current_position[0] + 2, chessboard.current_position[1] - 1]
    return chessboard


def check_move_three(chessboard):
    return chessboard.current_position[0] + 2 <= chessboard.columns - 1 and chessboard.current_position[1] >= 1 and [chessboard.current_position[0] + 2, chessboard.current_position[1] - 1] not in chessboard.transited


def move_four(chessboard):  # right one, up two
    if chessboard.current_position[0] + 1 <= chessboard.columns - 1 and chessboard.current_position[1] >= 2 and [chessboard.current_position[0] + 1, chessboard.current_position[1] - 2] not in chessboard.transited:
        chessboard.current_position = [
            chessboard.current_position[0] + 1, chessboard.current_position[1] - 2]
    return chessboard


def check_move_four(chessboard):
    return chessboard.current_position[0] + 1 <= chessboard.columns - 1 and chessboard.current_position[1] >= 2 and [chessboard.current_position[0] + 1, chessboard.current_position[1] - 2] not in chessboard.transited


def move_five(chessboard):  # left one, up two
    if chessboard.current_position[0] >= 1 and chessboard.current_position[1] >= 2 and [chessboard.current_position[0] - 1, chessboard.current_position[1] - 2] not in chessboard.transited:
        chessboard.current_position = [
            chessboard.current_position[0] - 1, chessboard.current_position[1] - 2]
    return chessboard


def check_move_five(chessboard):
    return chessboard.current_position[0] >= 1 and chessboard.current_position[1] >= 2 and [chessboard.current_position[0] - 1, chessboard.current_position[1] - 2] not in chessboard.transited


def move_six(chessboard):  # left two, up one
    if chessboard.current_position[0] >= 2 and chessboard.current_position[1] >= 1 and [chessboard.current_position[0] - 2, chessboard.current_position[1] - 1] not in chessboard.transited:
        chessboard.current_position = [
            chessboard.current_position[0] - 2, chessboard.current_position[1] - 1]
    return chessboard


def check_move_six(chessboard):
    return chessboard.current_position[0] >= 2 and chessboard.current_position[1] >= 1 and [chessboard.current_position[0] - 2, chessboard.current_position[1] - 1] not in chessboard.transited


def move_seven(chessboard):  # left two, down one
    if chessboard.current_position[0] >= 2 and chessboard.current_position[1] + 1 <= chessboard.rows - 1 and [chessboard.current_position[0] - 2, chessboard.current_position[1] + 1] not in chessboard.transited:
        chessboard.current_position = [
            chessboard.current_position[0] - 2, chessboard.current_position[1] + 1]
    return chessboard


def check_move_seven(chessboard):
    return chessboard.current_position[0] >= 2 and chessboard.current_position[1] + 1 <= chessboard.rows - 1 and [chessboard.current_position[0] - 2, chessboard.current_position[1] + 1] not in chessboard.transited


def move_eight(chessboard):  # left one, down two
    if chessboard.current_position[0] >= 1 and chessboard.current_position[1] + 2 <= chessboard.rows - 1 and [chessboard.current_position[0] - 1, chessboard.current_position[1] + 2] not in chessboard.transited:
        chessboard.current_position = [
            chessboard.current_position[0] - 1, chessboard.current_position[1] + 2]
    return chessboard


def check_move_eight(chessboard):
    return chessboard.current_position[0] >= 1 and chessboard.current_position[1] + 2 <= chessboard.rows - 1 and [chessboard.current_position[0] - 1, chessboard.current_position[1] + 2] not in chessboard.transited


def legal_move(chessboard):
    if check_move_one or check_move_two or check_move_three or check_move_four or check_move_five or check_move_six or check_move_seven or check_move_eight:
        return True
    else:
        return False


def get_legal_moves(chessboard):
    moves = []
    if check_move_one(chessboard) == True:
        moves.append(move_one)

    if check_move_two(chessboard) == True:
        moves.append(move_two)

    if check_move_three(chessboard) == True:
        moves.append(move_three)

    if check_move_four(chessboard) == True:
        moves.append(move_four)

    if check_move_five(chessboard) == True:
        moves.append(move_five)

    if check_move_six(chessboard) == True:
        moves.append(move_six)

    if check_move_seven(chessboard) == True:
        moves.append(move_seven)

    if check_move_eight(chessboard) == True:
        moves.append(move_eight)

    return moves


# Compiles list of moves and randomly selects one
def random_move(chessboard):
    legal_moves = get_legal_moves(chessboard)
    moves = 0
    while len(legal_moves) > 0:
        print(legal_moves)
        random = randint(0, len(legal_moves)-1)
        chessboard = legal_moves[random](chessboard)
        chessboard.transited.append(
            chessboard.current_position)
        moves += 1
        legal_moves = get_legal_moves(chessboard)

    print(chessboard.transited)

    return chessboard


# ******************Replace with algorithm,  for libary testing purposes only********************
def calculate_route(chessboard):
    chessboard = random_move(chessboard)

    return chessboard


def number_to_image(number):
    number_font = pygame.font.Font(None, 50)
    return number_font.render(str(number), True, Colors.BLACK, None)


# takes chessboard and moves through the route
def visualise_board(chessboard, debug=False):
    white_square = pygame.image.load("black-square-100.png")
    blue_square = pygame.image.load("blue-square.png")
    knight = pygame.image.load("red_knight.png")

    if debug:
        print(chessboard.transited)
    pygame.init()
    screen = pygame.display.set_mode(chessboard.size)
    move_num = 0
    number_pos = []
    transited_vis = []

    for move in chessboard.transited:
        if debug:
            print(move)
        screen.fill(Colors.WHITE)

        for i in range(chessboard.columns):
            for j in range(chessboard.rows):
                if [i, j] in transited_vis:
                    screen.blit(blue_square, (i * 100, j * 100))
                else:
                    screen.blit(white_square, (i * 100, j * 100))
                if [i, j] == move:
                    screen.blit(knight, (i * 100, j * 100))
                    number_pos.append(
                        [move_num, [i * 100, j * 100]])

        for number in number_pos:
            screen.blit(number_to_image(number[0]), number[1])

        screen.blit(knight, (move[0] * 100, move[1] * 100))
        pygame.display.update()
        pygame.event.get()
        currentKeys = pygame.key.get_pressed()

        transited_vis.append(move)

        pygame.time.delay(1000)
        if currentKeys[pygame.K_ESCAPE]:
            runGame = False
        move_num += 1

    while True:
        None


# main function
def main():
    chessboard = get_board_size()
    chessboard = calculate_route(chessboard)
    visualise_board(chessboard)


if __name__ == "__main__":
    main()
