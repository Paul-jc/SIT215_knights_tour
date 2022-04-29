from random import randint
import pygame


"""
Originally adapted from https://github.com/Yacoby/KnightsTour
"""

# Limitation for memory usage:
MEMORYLIMIT = 20


# Animate the final results
class Animation:
    def __init__(self, board):
        self.board = board
        self.size = board.size

    # Initialise pygame screen
    def pygame_init(self):
        pygame.init()

        self.screen = pygame.display.set_mode(
            [self.size * 50 + 1, self.size * 50 + 1])
        pygame.display.set_caption("Knight's Tour")

    # Draw grid to screen
    def draw_board(self):
        for i in range(self.board.size+2):
            pygame.draw.line(self.screen, (0, 255, 255), (i*50, 0),
                             (i*50, self.board.size*50))
            pygame.draw.line(self.screen, (0, 255, 255), (0, i*50),
                             (self.board.size*50, i*50))
        pygame.display.update()

    # Convert coordinates to pygame coordinates
    def point(self, x, y):
        return (x * 50 + 25, (self.board.size - 1 - y) * 50 + 25)

    # Draw line for each move in board path
    def draw_path(self):
        for n in self.board.neurons:
            if n.output[n.incrementation] == 1:
                color = (255, 0, 50)
                pygame.draw.line(self.screen,
                                 color,
                                 self.point(
                                     n.position[0].x, n.position[0].y),
                                 self.point(
                                     n.position[1].x, n.position[1].y)
                                 )
        for s in board.vertex_iter():
            pygame.draw.circle(self.screen, (255, 0, 50),
                               self.point(s.x, s.y), 5)
        pygame.display.update()

    def pygame_quit(self):
        pygame.quit()


# Class for square on a board
class Square:
    # Initialize a square with empty list for edges and x and y coordinates
    def __init__(self, x, y):
        self.edges = []
        self.x = x
        self.y = y

    # function to return true if square is linked to v
    def is_linked(self, v):
        return any(v in e.position for e in self.edges)


# function to link squares together in moves
def link_squares(v1, v2):
    for e in v1.edges:
        if v2 in e.position:
            raise Exception("edge already exists")

    for e in v2.edges:  # ensures that there isn't already a link
        if v1 in e.position:
            raise Exception("edge already exists")

    e = Neuron(v1, v2)
    v1.edges.append(e)
    v2.edges.append(e)
    return e


class Neuron:
    # Represents a neuron in the network which is a square
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.position = (x, y)  # tuple to reresent position on the board
        self.init()

    def init(self):
        self.incrementation = 0  # number of times neuron has changed state
        self.state = 0  # current state of neuron
        self.previous_state = 0  # previous state of neuron - to see if neuron has been changed
        self.visited = False
        self.output = {0: randint(0, 1)}

    # Check if neuron has changed state
    def has_changed(self):
        return self.state != self.previous_state or self.output[self.incrementation] != self.output[self.incrementation - 1]

    # Get sum of neighbors (how many squares are linked to this neuron by a move)
    def sum_of_neighbours(self, increment):
        return sum(pos.output[increment] for pos in self.position[0].edges + self.position[1].edges)

    # Update state of neuron
    def update_state(self):
        self.incrementation += 1
        self.previous_state = self.state
        self.state = self.previous_state + 4 - \
            self.sum_of_neighbours(
                self.incrementation-1)  # -1 because the output is the previous state
        if self.state > 3:
            # if ther are greater than 3 squares linked to this neuron, it is a 1
            self.output[self.incrementation] = 1
        elif self.state < 0:
            # if there is less than 0 squares linked to this neuron, it is a 0
            self.output[self.incrementation] = 0
        else:
            # if there are 0 or 1 squares linked to this neuron, it is the same as the previous state
            self.output[self.incrementation] = self.output[self.incrementation-1]

        if len(self.output) > MEMORYLIMIT:
            # ensures that the memory limit is not exceeded
            del self.output[self.incrementation-MEMORYLIMIT]


# Class for the board
class Board:
    # Initialize the board with board size, empty list for the board and the number of iterations as 0
    def __init__(self, size):
        self.size = size
        self.board = []  # list of squares
        self.neurons = []  # list of neurons (also squares)
        self.running = True
        self.testing = False
        self.iterations = 0

        # generates 2d array of size x size
        self.board = [[Square(x, y) for y in range(size)] for x in range(size)]
        self.init()

        if self.testing:
            print(self.board)
            print(len(self.board))
            print(len(self.board[0]))

    # Initialize the board with the first move
    def init(self):
        for m in [(2, 1), (-2, 1), (1, 2), (-1, 2)]:
            self.add_move(m)

    # Adds move to the board and links the squares together
    def add_move(self, move):
        my = move[0]
        mx = move[1]

        def get_range(x):
            if x >= 0:
                return range(0, self.size-x)
            return range(abs(x), self.size)

        for x in get_range(mx):
            for y in get_range(my):
                self.link((x, y), (x+mx, y+my))

    # Links the squares together
    def link(self, v1, v2):
        v1 = self.vertex_at(v1)
        v2 = self.vertex_at(v2)
        self.neurons.append(link_squares(v1, v2))

    def vertex_iter(self):
        for s in self.board:
            yield from s

    def edge_iter(self):
        yield from self.neurons

    # Returns the square at the given coordinates
    def vertex_at(self, pos):
        return self.board[pos[0]][pos[1]]

    # ge a set of patterns found within the neurons past output
    def get_possible_patterns(self, neuron, iteration, lookback=range(1, MEMORYLIMIT)):
        offsets = []
        for offset in lookback:
            if neuron.output[iteration] == neuron.output[iteration-offset]:
                for i in range(1, MEMORYLIMIT - offset):
                    if neuron.output[iteration-i] != neuron.output[iteration-i-offset]:
                        break
                else:
                    offsets.append(offset)
        return set(offsets)

    # get the distance before the output will repeat itself
    def get_pattern_offset(self, iterations):
        if iterations < MEMORYLIMIT or not len(self.neurons):
            return set([])

        patterns = self.get_possible_patterns(self.neurons[0], iterations)
        for neuron in self.neurons[1:]:
            patterns = patterns.intersection(
                self.get_possible_patterns(neuron, iterations, patterns))
        return patterns

    # Updates the board with new set of moves from get_moves
    def update_board(self):
        for neuron in self.neurons:
            neuron.update_state()

    # check if the board has changed since the last iteration
    def is_complete(self):
        return not any(n.has_changed() for n in self.neurons)

    # checks if the neuron state forms a pattern
    def is_convergent(self):
        return not len(self.get_pattern_offset(self.neurons[0].incrementation))

    # resets all neurons to original state
    def reset_neurons(self):
        for neuron in self.neurons:
            neuron.init()

    # Increments the number of iterations by 1
    def increment_iterations(self):
        self.iterations += 1

    # Returns the number of iterations
    def get_iterations(self):
        return self.iterations

    # Returns the board
    def get_board(self):
        return self.board


if __name__ == "__main__":
    # Initialize the board
    board = Board(6)

    running = True
    while running:
        board.update_board()
        if board.is_complete() and board.is_convergent():
            running = False
            board.update_board()
        if board.is_complete() and not board.is_convergent():
            board.reset_neurons()

    # Animates the board
    animation = Animation(board)
    animation.pygame_init()
    animation.draw_board()
    animation.draw_path()
    print("Complete")

    displaying = True
    while displaying:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                displaying = False
