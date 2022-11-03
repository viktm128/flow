"""Basic helper functions and other utility functions defined here."""

def read_board(filename):
    """Read board from specification format."""
    fstream = open(str(filename))
    line = fstream.readline().split()
    [x, y] = map(int, line)  # so clean, how fun


    # cannot initialize a list of lists using multiplication
    board = [0] * y
    for i, _ in enumerate(board):
        board[i] = [0] * x

    num_flows = 0
    while True:
        flow = fstream.readline().split()
        if not flow:
            print("this is needed")
            break

        num_flows += 1

        # need to enumerate it y, x because of weird printing rules
        board[int(flow[0][3])][int(flow[0][1])] = num_flows
        board[int(flow[1][3])][int(flow[1][1])] = num_flows


    return (x, y, num_flows, board)


def print_board(board):
    """Print board to standard output."""

    # TODO make this a bit prettier.
    for row in board:
        print(row)


if __name__ == "__main__":
    _, _, _, board = read_board('test_cases/test_basic.txt')
    print_board(board)