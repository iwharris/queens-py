__author__ = 'iwharris'

base_state = [[0 for x in range(8)] for y in range(8)]  # Blank state

def solve(state, queen_count=0, solutions=[]):
    return solutions + [state]

def print_states(states):
    for state in states:
        print '\n'.join([''.join(['Q' if state[x][y]==1 else 'x' if state[x][y]==-1 else '.' for x in range(8)]) for y in range(8)])

if __name__ == '__main__':
    print_states(solve(base_state, []))