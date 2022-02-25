# running test cases
from pathlib import Path
import pdb

# TODO move all of these functions to helper.
def read_board(filename):
    """Read board from specification format."""
    fstream = open(str(filename))
    line = fstream.readline().split()
    [n, m] = map(int, line)  # so clean, how fun


    # cannot initialize a list of lists using multiplication
    board = []
    for _ in range(m):
        board.append([None] * n)

    num_flows = 0
    while True:
        # TODO make this whole thing suck less
        line = fstream.readline().split()
        if not line:
            break
        letter = line.pop(0)[0]
        num_flows += 1
        coords = list(map(int, line))
        for i in range(int(len(coords)/2)):  # TODO figure out why integer division is failing
            if i == 0 or i == len(coords)/2 - 1:
                board[coords[2*i + 1]][coords[2*i]] = letter  # TODO confirm width and height are not mixed
            else:
                board[coords[2*i + 1]][coords[2*i]] = c2i(letter)


    return (n, m, num_flows, board)


def print_board(board):
    """Print board to standard output."""

    # TODO make this a bit prettier.
    for row in board:
        print(row)


def c2i(c):
    """Change character to integer."""
    return ord(c) - 97

def i2c(i):
    """Change integer to character."""
    chr(i + 97)


def test_classic_11():
    """Read and print test case 11"""
    p = Path.cwd()
    p = p/'test_cases'
    (_, _, _, board) = read_board(p/'classic_level_11.txt')


    print("Starting board:")
    print_board(board)

    (_, _, _, board) = read_board(p/'classic_level_11_answers.txt')
    print("Solved board:")
    print_board(board)


test_classic_11()


