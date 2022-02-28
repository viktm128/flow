"""Basic helper functions and other utility functions defined here."""

def c2i(c):
    """Change character to integer."""
    return ord(c) - 97

def i2c(i):
    """Change integer to character."""
    chr(i + 97)



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
