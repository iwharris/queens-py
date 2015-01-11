## Queens ##

This is a quick and dirty solution to the "Eight queens puzzle." It finds all unique solutions to the puzzle, printing each solution as it is encountered.

From the [Wikipedia article](http://wikipedia.org/wiki/Eight_queens_puzzle):

> The eight queens puzzle is the problem of placing eight chess queens on an 8×8 chessboard so that no two queens threaten each other. Thus, a solution requires that no two queens share the same row, column, or diagonal. The eight queens puzzle is an example of the more general n-queens problem of placing n queens on an n×n chessboard, where solutions exist for all natural numbers n with the exception of n=2 or n=3.

This implementation can be used to solve the the general **n-queens problem**. You can adjust **n** by modifying the value of `N_QUEENS`.

It uses a recursive, kinda-bruteforce approach with backtracking. It is **by no means optimal**. For example, memory usage can be improved by using a single 64-bit integer and bit-shifting to represent the board state for **n queens** up to **n = 8**.