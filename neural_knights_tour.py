import random


# Class for square on a board
class Square:
    # Initialize a square with empty list for edges and x and y coordinates
    def __init__(self, x, y):
        self.edges = []
        self.x = x
        self.y = y

    # function to return true if square is linked to v
    def is_linked(self, v):
        for edge in self.edges:
            if edge.v == v:
                return True
        return False


# Class for the board
class Board:
    # Initialize the board with board size, empty list for the board and the number of iterations as 0
    def __init__(self, size):
        self.size = size
        self.board = []
        self.iterations = 0

        # generates 2d array of size x size
        self.board = [[Square(x, y) for y in range(size)] for x in range(size)]

    # All possible moves from a square
    def get_moves(self):
        self.moves = [(1, -2), (2, -1), (2, 1), (1, 2),
                      (-1, 2), (-2, 1), (-2, -1), (-1, -2)]

        return random.choice(self.moves)

    # Increments the number of iterations by 1
    def increment_iterations(self):
        self.iterations += 1

    # Returns the number of iterations
    def get_iterations(self):
        return self.iterations

    # Returns the board
    def get_board(self):
        return self.board

    # Adds move to the board
    def add_move(self, move):
        for i in range(self.size):
            for j in range(self.size):
                # if move is plus x and y are in bounds
                if move[0] + i < self.size and move[1] + j < self.size:
                    # add edge to the square
                    self.board[i][j].edges.append(move)

    # Updates the board with new set of moves from get_moves
    def update_board(self):
        for i in range(self.size):
            for j in range(self.size):
                self.add_move(self.get_moves())
        self.increment_iterations()
        self.print_board()
        print("==========================")
        # Check if the board is complete
        if self.is_complete():
            return True
        else:
            self.update_board()

    # Check if moves result in all squares being linked

    def is_complete(self):
        for i in range(self.size):
            for j in range(self.size):
                if len(self.board[i][j].edges) != 8:
                    return False
        return True

    # Prints the board
    def print_board(self):
        board = self.get_board()
        for i in range(self.size):
            for j in range(self.size):
                print(board[i][j].edges)


if __name__ == "__main__":
    random.seed(2)
    # Initialize the board
    board = Board(6)
    board.print_board()
    # Update the board
    # board.update_board()
    # Print the board
    # print(board.get_board())
    # for size in range(6, 14, 2):
    #    # random.seed(1)
    #    board = Board(size)
    #    #print("Size:", size)
    #    #print("Iterations:", board.iterations)
    #    # Increment iterations
    #    # board.increment_iterations()
    #    #print("Iterations:", board.iterations)
    #    #print("Board:", board.board)
    #    for i in range(10):
    #        move = board.get_moves()
    #        print("Move:", move)
    #        board.add_move(move)
    #        #print("Board:", board.get_board())
    #        board.increment_iterations()
    #        print("Iterations:", board.iterations)
    #    print("===========================")
