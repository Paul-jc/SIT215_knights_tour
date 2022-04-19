from distutils.log import debug
import random
import chess


# Holds the possible moves for the knight
class Moves:
    moves = [[-2, -2, -1, -1, 1, 1, 2, 2],
             [-1, 1, -2, 2, -2, 2, -1, 1]]


# Holds total moves
class TotalMoves:
    # Initialise the total moves to 0
    def __init__(self, total_moves=0):
        self.total_moves = total_moves

    # function to increment the total moves
    def increment_total_moves(self):
        self.total_moves += 1

    def get_total_moves(self):
        return self.total_moves


def knight_tour_helper(n, start_pos, board, x, y, counter, total_moves, debug):
    if debug:
        print(
            f"counter: {counter}, total_moves: {total_moves.get_total_moves()}")

    if counter == n * n:  # If the move counter is equal to the total number of squares on the board, the solution is complete
        return True

    # Iterate total_moves
    total_moves.increment_total_moves()

    # Check that the move is on the board and there are no duplicates (as denoted by already not being -1) and the starting position is 0
    if x < 0 or x >= n or y < 0 or y >= n or board[y][x] != -1:
        return False

    # Set the current position to the counter
    board[y][x] = counter

    # Loop through the possible moves
    for x_move, y_move in zip(Moves.moves[0], Moves.moves[1]):
        # Recursively call the function with the new coordinates
        if knight_tour_helper(n, start_pos, board, x + x_move, y + y_move, counter + 1, total_moves, debug):
            return True

    board[y][x] = -1  # If the recursive function returns false, the move is undone
    return False


def knights_tour(n, start_pos, debug):
    # Boards initialised with -1 on every square to denote unvisited
    board = [[-1 for _ in range(n)] for _ in range(n)]

    total_moves = TotalMoves()

    # Call the recursive function
    knight_tour_helper(n=n, start_pos=start_pos,
                       board=board, x=start_pos[1], y=start_pos[0], counter=0, total_moves=total_moves, debug=debug)
    return board, total_moves.get_total_moves()


def matrix_to_moves(matrix, move_list):  # Convert the matrix to a list of moves
    for i in range(len(matrix)):  # Loop through the rows
        for j in range(len(matrix[i])):  # Loop through the columns
            move_num = matrix[i][j]  # Get the move number
            # Add the move to the list using the move number as the index
            move_list[move_num] = [i, j]  # Add the move to the list
    return move_list


def validate_input(size, start_pos):
    # Check if the size of the board is less than 15 and warn user of length of time required
    if size < 15:
        print("This will take a long time to solve")

    # Check if start_pos is within the board
    if start_pos[0] < 0 or start_pos[0] >= size or start_pos[1] < 0 or start_pos[1] >= size:
        print("Invalid starting position")
        get_user_input()
    return True


def get_user_input():
    # Get the size of the board from the user
    n = int(input("Enter the number of rows/columns: "))
    # Get the starting position from the user - minus 1 to convert to 0 indexing
    start_pos = [int(input("Enter the starting row: ")) - 1, int(
        input("Enter the starting column: ")) - 1]
    # Validate the input and return the size and starting position
    if validate_input(n, start_pos):
        return n, start_pos


def main():
    n, start_pos = get_user_input()
    # Default debug to false
    debug = True

    board, total_moves = knights_tour(n, start_pos, debug)
    print(f"Total moves: {total_moves}")

    # Initialise the move list with all [-1, -1] as a place holder
    move_list = [[-1, -1] for _ in range(n**2)]

    # Convert the board to a list of moves
    move_list = matrix_to_moves(board, move_list)

    # Convert to chessboard from chess library
    chessboard = chess.ChessBoard(columns=n, rows=n, size=(
        n*100, n*100), initial_position=move_list[0], current_position=move_list[-1], transited=move_list)
    # Pass the board to the chess library
    chess.visualise_board(chessboard, debug=debug)


if __name__ == '__main__':
    main()
