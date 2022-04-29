import random
from re import M
import pygame
import time


# Limitation for memory usage:
MEMORYLIMIT = 20

# Animate the final results


class Animation:
    def __init__(self, board):
        self.board = board
        self.size = board.size
        print(f"Size: {self.size}")

    # pygame.init()
    def pygame_init(self):
        pygame.init()

        self.screen = pygame.display.set_mode(
            [self.size * 50 + 1, self.size * 50 + 1])
        pygame.display.set_caption("Knight's Tour")

    def draw_board(self):
        for i in range(self.board.size):
            for j in range(self.board.size):
                pygame.draw.rect(self.screen, (255, 255, 255),
                                 (i * 50, j * 50, 50, 50))
                pygame.draw.rect(self.screen, (0, 0, 0),
                                 (i * 50 + 1, j * 50 + 1, 48, 48))
        pygame.display.update()

    def draw_board2(self):
        for i in range(self.board.size+2):
            pygame.draw.line(self.screen, (0, 255, 255), (i*50, 0),
                             (i*50, self.board.size*50))
            pygame.draw.line(self.screen, (0, 255, 255), (0, i*50),
                             (self.board.size*50, i*50))
        pygame.display.update()

    def draw_knight_path(self):
        print(board.neurons)
        print(len(board.neurons))
        for n in board.neurons:
            print(n)
            print(n.output)
            if n.output[n.iterations] == 1:
                pygame.draw.line(self.screen,
                                 (0, 0, 255),
                                 self.point(n.x, n.y),
                                 self.point(n.x + n.dx, n.y + n.dy))

        pygame.display.update()

    def point(self, x, y):
        return (x * 50 + 25, (self.board.size - 1 - y) * 50 + 25)

    def draw_path(self):
        print(self.board.neurons)
        for n in self.board.neurons:
            print(n.output[n.incrementation])
            if n.output[n.incrementation] == 1:
                print(n.output[n.incrementation])
                color = (0, 0, 255)
                pygame.draw.line(self.screen,
                                 color,
                                 self.point(
                                     n.position[0].x, n.position[0].y),
                                 self.point(
                                     n.position[1].x, n.position[1].y)
                                 )
        pygame.display.update()

    def start(self):
        self.pygame_init()
        self.draw_board2()
        self.draw_path()
        time.sleep(20)

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
        return any([v in e.position for e in self.edges])


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
        self.position = (x, y)
        self.init()

    def init(self):
        self.incrementation = 0
        self.state = 0
        self.previous_state = 0
        self.visited = False
        self.output = {0: random.randint(0, 1)}

    # Check if neuron has changed state
    def has_changed(self):
        return self.state != self.previous_state or self.output[self.incrementation] != self.output[self.incrementation - 1]

    # Check if neuron has been visited
    # def has_visited(self):
    #    if self.visited:
    #        return True
    #    else:
    #        return False

    # Get sum of neighbors
    def sum_of_neighbours(self, increment):
        s = 0
        for pos in self.position[0].edges+self.position[1].edges:
            s += pos.output[increment]
        return s

    # update state of neuron
    def update_state(self):
        print('making it into update state')
        self.incrementation += 1
        self.previous_state = self.state
        self.state = self.previous_state + 4 - \
            self.sum_of_neighbours(self.incrementation-1)
        if self.state > 3:
            self.output[self.incrementation] = 1
        elif self.state < 0:
            self.output[self.incrementation] = 0
        else:
            self.output[self.incrementation] = self.output[self.incrementation-1]

        if len(self.output) > MEMORYLIMIT:
            del self.output[self.incrementation-MEMORYLIMIT]


# Class for the board
class Board:
    # Initialize the board with board size, empty list for the board and the number of iterations as 0
    def __init__(self, size):
        self.size = size
        self.board = []
        self.neurons = []
        self.testing = False
        self.iterations = 0

        # generates 2d array of size x size
        self.board = [[Square(x, y) for y in range(size)] for x in range(size)]
        self.init()

        if self.testing:
            print(self.board)
            print(len(self.board))
            print(len(self.board[0]))

    def init(self):
        for m in [(2, 1), (-2, 1), (1, 2), (-1, 2)]:
            self.add_move(m)

    # Adds move to the board
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

    def link(self, v1, v2):
        v1 = self.vertex_at(v1)
        v2 = self.vertex_at(v2)
        self.neurons.append(link_squares(v1, v2))

    def vertex_iter(self):
        for s in self.board:
            for y in s:
                yield y

    def edge_iter(self):
        for n in self.neurons:
            yield n

    def vertex_at(self, pos):
        return self.board[pos[0]][pos[1]]

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

        if board.is_complete() and not board.is_convergent():
            print("complete")
            return True

        self.update_board()

    # Check if moves result in all squares being linked
    def is_complete(self):
        for n in self.neurons:
            if n.has_changed():
                return False
        return True

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
    # board.print_board()
    # Update the board
    board.update_board()
    # Print the board
    # print(board.get_board())
    # board = Board(board.size)
    # move = board.get_moves()
    # board.add_move(move)
    # board.increment_iterations()
    print("done")
    # board.print_second()
    animation = Animation(board)
    while True:
        animation.start()
