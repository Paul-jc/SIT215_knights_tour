An implimentation and comparison of knight's tour using brute force, backtracking, state space, warnsdorff and neural network methods.

chess.py has basic board visualisation used as a library for our brute force and backtrack methods

backtrack_and_brute_force_knight.py is run using the command 'python backtrack_and_brute_force_knight.py' or 'python3 backtrack_and_brute_force_knight.py' depending on the system you are running. This will give options for both the backtrack and brute force methods. Prompts will be given for selecting the desired algorithm and starting position - square 1, 1 is the top left corner of the board.

state_space_knights_tour.py is run using the command 'python state_space_knights_tour.py' or 'python3 state_space_knights_tour.py' depending on the system you are running. This will give options for both depth search as well as warnsdorff methods. Prompts will be given for selecting the desired algorithm and size of the board - the starting position can be overwritten within the main() function.

neural_knights_tour.py is run by using the command 'python neural_knights_tour.py' or 'python3 neural_knights_tour.py' depending on the system you are running. The size of the board can be changed withing the main function

In all cases the minimum size of board is 5. In the case of the neural network algorithm, odd size boards are unsolvable due to being a closed knights tour search requiring an even number of squares on the board.