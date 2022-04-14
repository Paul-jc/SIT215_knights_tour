from string import whitespace
import sys
import pygame
from random import choice


# Colors for use throughout the visualisation
class Colors:
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    CYAN = (0, 255, 255)
    MAGENTA = (255, 0, 255)


# Images used to build the visulaisation
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
# TODO - impliment check for minimum possible board
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
        print("Move one")
    else:
        return 0
    return chessboard


def move_two(chessboard):  # right two, down one
    if chessboard.current_position[0] + 2 <= chessboard.columns-1 and chessboard.current_position[1] + 1 <= chessboard.rows-1 and [chessboard.current_position[0] + 2, chessboard.current_position[1] + 1] not in chessboard.transited:
        chessboard.current_position = [
            chessboard.current_position[0] + 2, chessboard.current_position[1] + 1]
        print("Move two")
    else:
        return 0
    return chessboard


def move_three(chessboard):  # right two, up one
    if chessboard.current_position[0] + 2 <= chessboard.columns - 1 and chessboard.current_position[1] >= 1 and [chessboard.current_position[0] + 2, chessboard.current_position[1] - 1] not in chessboard.transited:
        chessboard.current_position = [
            chessboard.current_position[0] + 2, chessboard.current_position[1] - 1]
        print("Move three")
    else:
        return 0
    return chessboard


def move_four(chessboard):  # right one, up two
    if chessboard.current_position[0] + 1 <= chessboard.columns - 1 and chessboard.current_position[1] >= 2 and [chessboard.current_position[0] + 1, chessboard.current_position[1] - 2] not in chessboard.transited:
        chessboard.current_position = [
            chessboard.current_position[0] + 1, chessboard.current_position[1] - 2]
        print("Move four")
    else:
        return 0
    return chessboard


def move_five(chessboard):  # left one, up two
    if chessboard.current_position[0] >= 1 and chessboard.current_position[1] >= 2 and [chessboard.current_position[0] - 1, chessboard.current_position[1] - 2] not in chessboard.transited:
        chessboard.current_position = [
            chessboard.current_position[0] - 1, chessboard.current_position[1] - 2]
        print("Move five")
    else:
        return 0
    return chessboard


def move_six(chessboard):  # left two, up one
    if chessboard.current_position[0] >= 2 and chessboard.current_position[1] >= 1 and [chessboard.current_position[0] - 2, chessboard.current_position[1] - 1] not in chessboard.transited:
        chessboard.current_position = [
            chessboard.current_position[0] - 2, chessboard.current_position[1] - 1]
        print("Move six")
    else:
        return 0
    return chessboard


def move_seven(chessboard):  # left two, down one
    if chessboard.current_position[0] >= 2 and chessboard.current_position[1] + 1 <= chessboard.rows - 1 and [chessboard.current_position[0] - 2, chessboard.current_position[1] + 1] not in chessboard.transited:
        chessboard.current_position = [
            chessboard.current_position[0] - 2, chessboard.current_position[1] + 1]
        print("Move seven")
    else:
        return 0
    return chessboard


def move_eight(chessboard):  # left one, down two
    if chessboard.current_position[0] >= 1 and chessboard.current_position[1] + 2 <= chessboard.rows - 1 and [chessboard.current_position[0] - 1, chessboard.current_position[1] + 2] not in chessboard.transited:
        chessboard.current_position = [
            chessboard.current_position[0] - 1, chessboard.current_position[1] + 2]
        print("Move eight")
    else:
        return 0
    return chessboard


# Compiles list of moves and randomly selects one
def random_move(chessboard):
    moves = [move_one, move_two, move_three, move_four, move_five,
             move_six, move_seven, move_eight]
    random_move = 0
    while random_move == 0:
        random_move = choice(moves)(chessboard)
        chessboard.transited.append(chessboard.current_position)
    return random_move


# ******************Replace with algorithm********************
def calculate_route(chessboard):
    runGame = 0
    moves = 0
    route = []
    while moves < 10:
        chessboard = random_move(chessboard)
        moves += 1

    return chessboard


def visualise_board(chessboard):
    white_square = pygame.image.load("black-square-100.png")
    blue_square = pygame.image.load("blue-square.png")
    knight = pygame.image.load("red_knight.png")

    pygame.init()
    screen = pygame.display.set_mode(chessboard.size)
    move = 0
    number_pos = []
    runGame = True
    transited_vis = []
    print("starting")
    print(chessboard.transited)

    for move in chessboard.transited:
        screen.fill(Colors.WHITE)

        for i in range(chessboard.columns):
            for j in range(chessboard.rows):
                if [i, j] in transited_vis:
                    screen.blit(blue_square, (i * 100, j * 100))
                else:
                    screen.blit(white_square, (i * 100, j * 100))

        print(move)
        screen.blit(knight, (move[0] * 100, move[1] * 100))
        pygame.display.update()
        pygame.event.get()
        currentKeys = pygame.key.get_pressed()

        transited_vis.append(move)
        print(transited_vis)

        pygame.time.delay(1000)
        if currentKeys[pygame.K_ESCAPE]:
            runGame = False

    pygame.quit()

# main function


def main():
    chessboard = get_board_size()
    chessboard = calculate_route(chessboard)
    visualise_board(chessboard)


if __name__ == "__main__":
    main()
