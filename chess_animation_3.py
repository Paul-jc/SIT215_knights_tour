from datetime import datetime
from decimal import Clamped
from re import T
import turtle
import time


"""
Adapted from code found on
http://blog.justsophie.com/algorithm-for-knights-tour-in-python/
Warnsdorff Heuristic method added as well as visualisation
"""

<<<<<<< HEAD
=======
# TODO clean up redundent turtle animation code.
# TODO resize squares to accomodate larger board sizes
# TODO option to generate path a lines only (show the spider-web shape)

>>>>>>> mic-0-hal/main

class Visualisation:
    def __init__(self, size):
        # set up the screen display of the board
        self.size = size
        self.window = turtle.Screen()
        self.window.title("Knights tour. SIT215 Group 13")
        # self.window.setup(width=1100, height=1100) # (0,0) is in the centre
        self.window.setup(width=size*100, height=size *
                          100)  # (0,0) is in the centre
        self.window.tracer(0)
        self.chessboard = turtle.Turtle()
        # draw board background
        self.chessboard.penup()
        self.a = 0  # for alternating row colours
        self.b = 0  # for alternating column colours
        self.board_squares = [turtle.Turtle() for _ in range(size*size)]
        self.visited = []

    def animate(self, path):
        self.fill_board()
        self.chessboard.penup()
        # self.chessboard.goto(self.map_coords(path[0]))
        self.chessboard.goto(self.coords(path[0]))
        self.chessboard.pendown()
        self.chessboard.color("red")
        for i in range(len(path)):
            # self.visited_cell(self.board_squares[i], self.map_coords(path[i]), i)
            self.visited_cell(self.board_squares[i], self.coords(path[i]), i)

    def fill_board(self):
        for i in range(self.size):
            if (self.b == 0):
                self.a = 1
            else:
                self.a = 0
            for j in range(self.size):
                self.chessboard.penup()
                self.chessboard.goto(
                    j*100-(self.size/2*100), i*100*(-1)+self.size/2*100)
                self.chessboard.pendown()
                if (self.a == 0):
                    self.chessboard.fillcolor('light grey')
                    self.a = 1
                else:
                    self.chessboard.fillcolor('white')
                    self.a = 0
                self.chessboard.begin_fill()
                for _ in range(4):
                    self.chessboard.forward(100)
                    self.chessboard.right(90)
                self.chessboard.end_fill()
            if (self.b == 0):
                self.b = 1
            else:
                self.b = 0

    def visited_text(self, i):
        self.chessboard.color("black")
        self.chessboard.write(i, align='center', font=('Arial', 20, 'normal'))
        self.window.update()
        self.chessboard.color("red")

    # displays the moves on the chess board display
    def visited_cell(self, text, x_y_path, i):
        self.chessboard.goto(x_y_path[0], x_y_path[1])
        self.visited_text(i)
        # change sleep time to change animation speed
        time.sleep(0.25)

        self.chessboard.shapesize(
            stretch_wid=4, stretch_len=4)  # 20 pixels is default

    # translates the chessboard coordinates into cartesian coordinates on the screen
    def coords(self, x_y_path):
        middle = (self.size / 2) * 100
        return (x_y_path[0] * 100 - middle + 50,
                middle - x_y_path[1] * 100 - 50)


class KnightsTour:
    def __init__(self, width, height):
        self.w = width
        self.h = height
        self.visited = []
        self.visited_count = 1  # Holds current depth of search
        self.path = []  # empty list for to hold list of moves
        self.board = []  # empty list for the board
        self.total_moves = 0  # total moves made
        self.total_calculations = 0  # total calculations made
        self.path_found = False  # boolean for if path is found
        self.t0 = 0
        self.t1 = 0
        self.testing = False  # Set to true to expose testing print messages
        self.generate_board()

    def generate_board(self):
        """
        Creates a nested list to represent the game board
        each element of list is a list of same size
        """
        for _ in range(self.h):  # for every height row
            # append a elements the length of a column
            self.board.append([0]*self.w)

    def start_timer(self):
        self.t0 = time.time()

    def stop_timer(self):
        self.t1 = time.time()

    # Get time by comparing t1 and t2
    def get_time(self):
        return self.t1 - self.t0

    def print_board(self):
        """"
        Prints the move numbers of the solved chess board
        """
        print("  ")
        print("------")
        for elem in self.board:
            print(elem)  # column-wise OR row-wise???
        print("------")
        print("  ")

    def animate(self):
        """"
        Shows the animation of moves on the screen
        """
        animation = Visualisation(self.w)
        animation.fill_board()
        animation.animate(self.path)

    def generate_legal_moves(self, cur_pos):
        """
        Returns legal move based off the current position
        """
        possible_pos = []  # array of options
        move_offsets = [(1, 2), (1, -2), (-1, 2), (-1, -2),
                        (2, 1), (2, -1), (-2, 1), (-2, -1)]  # x,y coordinates for moves

        for move in move_offsets:  # try each possible of the 8 moves for the knight
            # add the element in first position of tupple
            new_x = cur_pos[0] + move[0]
            # add the element of second position of tupple
            new_y = cur_pos[1] + move[1]

            # check if going wrong height direction
            # or if horizontally out of bounds of board
            # or if going wrong width direction
            # or if vertically out of bounds of board
            if (new_x >= self.h) or new_x < 0 or new_y >= self.w or new_y < 0:
                continue
            else:
                # if check pass then append to array of options
                possible_pos.append((new_x, new_y))
        return possible_pos

    def assign_warnsdorff_scores(self, empty_neighbours):
        # assign a score for the value of the move for sorting
        scores = []
        for empty in empty_neighbours:
            # self.total_calculations += 1
            score = [empty, 0]
            # returns array of possible positions as offsets
            moves = self.generate_legal_moves(empty)
            for move in moves:
                # check the array of arrays against the array of moves by their index
                # if this position is blank (0) then make it the next move
                if self.board[move[0]][move[1]] == 0:
                    score[1] += 1
            scores.append(score)
        return scores

    def find_neighbours(self, start_pos, wand):
        neighbour_list = self.generate_legal_moves(
            start_pos)  # returns list of possible solutions
        # list for neighbours that havent been visited
        empty_neighbours = []
        # add a neighbour if the cell is empty (hasnt been visited)
        for neighbour in neighbour_list:
            np_value = self.board[neighbour[0]][neighbour[1]]
            self.total_calculations += 1
            if np_value == 0:
                empty_neighbours.append(neighbour)
            # this activates warnsdorffs_heuristic for greatly improved pathfinding speed
            # sort the moves in ascending order of closeness
            scores = self.assign_warnsdorff_scores(empty_neighbours)
            scores_sort = sorted(scores, key=lambda s: s[1])
            # return the list of moves, sorted by closeness
            sorted_neighbours = [s[0] for s in scores_sort]

        if (wand == 1):
            empty_neighbours = sorted_neighbours

        return empty_neighbours

    def tour(self, start_pos, wand):
        """
        Recursive definition of knights tour. Inputs are as follows:
        start_pos = starting position
        """
        self.board[start_pos[0]][start_pos[1]
                                 ] = self.visited_count  # generate number of moves based on board size
        self.path.append(start_pos)  # first move is the coordinate passed in

        if self.testing:
            print("Visiting: ", start_pos)
        for _ in range(self.w*self.h):
            self.visited.append(start_pos)

        self.total_moves += 1

        if len(self.path) == self.w * self.h - 1:
            self.path_found = True
            if self.t0 != 0:
                self.stop_timer()
                runtime = self.get_time()
                print("Total Runtime: ", round(runtime, 2), "seconds")
            print("Total Moves: ", self.total_moves)
            print("Total Calculations: ", self.total_calculations)
            if not self.testing:
                self.print_board()
                print("N = ", self.w)
                print("Path taken:\n", self.path)
                self.animate()
                wait = input("Press Enter to continue.")
                print("Done!")
            return
        else:
            sorted_neighbours = self.find_neighbours(start_pos, wand)
            for neighbour in sorted_neighbours:  # start with the first move option
                # continue recursivelly calling function
                self.visited_count += 1
                self.tour(neighbour, wand)

            # starting position is passed in through function
            self.board[start_pos[0]][start_pos[1]] = 0
            try:
                self.path.pop()  # retun up tree if at a dead end
                if self.testing:
                    print("Going back to: ", self.path[-1])
            except IndexError:
                print("No path found")
                self.path_found = False
                return

# Get user input for the method and the size of the board


def get_user_selection():
    method = int(
        input("Enter 0 for depth search, 1 for warnsdorff heuristic: "))
    size = int(input("input size of board: "))
    return method, size


def main():
    # Execute the state space algorithm
    method, size = get_user_selection()
    kt = KnightsTour(size, size)  # Initialises instance of KnightsTour class

    # Starting depth of search tree, new path, starting coordinates, option to use warnsdorffs_heuristic
    # Decided to opt for 0, 0 starting position because there are squares that are unsolvable on an odd x odd board however having it as a function input was useful during testing
    kt.tour(start_pos=(0, 1), wand=method)


if __name__ == '__main__':
    main()
