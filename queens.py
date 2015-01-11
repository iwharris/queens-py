__author__ = 'iwharris'

"""
8 Queens puzzle, object-oriented recursive solution.
"""

import copy
import time

solution_set = {}

N_QUEENS = 8

class GameState(object):

    def __init__(self):
        self.board = [[0 for x in range(N_QUEENS)] for y in range(N_QUEENS)]
        self.num_queens = 0

    def __repr__(self):
        return '\n'.join([''.join(['Q' if self.board[x][y]==1 else '.' if self.board[x][y]==-1 else '.' for x in range(N_QUEENS)]) for y in range(N_QUEENS)])

    def get(self, x, y):
        return self.board[x][y]

    def solve(self):
        for x in range(N_QUEENS):
            for y in range(N_QUEENS):
                if self.board[x][y] == 1:
                    new_state = copy.deep_copy(self)
                    new_state.place_queen(x, y)
                    return new_state.solve()

    def place_queen(self, x, y):
        assert x in range(N_QUEENS) and y in range(N_QUEENS) and not self.board[x][y]
        self.board[x][y] = 1
        self.num_queens += 1

        # update valid remaining spaces
        # TODO this can be optimized
        for i in range(N_QUEENS):
            if not self.board[i][y]:
                self.board[i][y] = -1
            if not self.board[x][i]:
                self.board[x][i] = -1
            if x+i in range(N_QUEENS) and y+i in range(N_QUEENS) and not self.board[x+i][y+i]:
                self.board[x+i][y+i] = -1
            if x-i in range(N_QUEENS) and y-i in range(N_QUEENS) and not self.board[x-i][y-i]:
                self.board[x-i][y-i] = -1
            if x-i in range(N_QUEENS) and y+i in range(N_QUEENS) and not self.board[x-i][y+i]:
                self.board[x-i][y+i] = -1
            if x+i in range(N_QUEENS) and y-i in range(N_QUEENS) and not self.board[x+i][y-i]:
                self.board[x+i][y-i] = -1

    def copy(self):
        s = GameState()
        s.board = copy.deepcopy(self.board)
        s.num_queens = self.num_queens
        return s


def solve(state=GameState()):
    if state.num_queens == N_QUEENS:  # Base condition
        #print 'Solution found:'
        #print state
        sol = str(state)
        if sol not in (solution_set):
            solution_set[str(state)] = None
            print sol + '\n\n'
    else:  # Time to recurse
        for x in range(N_QUEENS):
            for y in range(N_QUEENS):
                if not state.get(x,y):
                    new_state = state.copy()
                    new_state.place_queen(x, y)
                    solve(new_state)


start_time = time.time()

solve(GameState())

#for sol in solution_set.keys():
#    print sol + '\n\n'

print '%d unique solutions found.' % len(solution_set.keys())

print 'Elapsed time: %.3fs' % (time.time() - start_time)