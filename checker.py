"""Verify the correct completion of a board."""

from helper import c2i


def check_classic(num_flows, board):
    """Check classic square and rectangle boards."""
    # check for incomplete board
    for row in board:
        if None in row:
            return False

    # there are exactly 2 endpoints for each flow
        # does this get checked secretly in the other algorithm
    endpoint_counts = [0] * num_flows
    for row in board:
        for box in row:
            if c2i(box) >= num_flows:
                return False
            endpoint_counts[c2i(box)] += 1

    for count in endpoint_counts:
        if count != 2:
            return False

    for i, row in enumerate(board):
        for j, box in enumerate(row):
            count = 0
            if i == 0:
                # top left corner
                if j == 0:
                    count += c2i(box) == c2i(board[i][j + 1])
                    count += c2i(box) == c2i(board[i + 1][j])
                # top right corner
                elif j == len(row) - 1:
                    count += c2i(box) == c2i(board[i][j + 1])
                    count += c2i(box) == c2i(board[i - 1][j])
                # top side
                else:
                    count += c2i(box) == c2i(board[i][j + 1])
                    count += c2i(box) == c2i(board[i][j - 1])
                    count += c2i(box) == c2i(board[i + 1][j])
            elif i == len(board) - 1:
                # bottom left corner
                if j == 0:
                    count += c2i(box) == c2i(board[i][j + 1])
                    count += c2i(box) == c2i(board[i - 1][j])
                # bottom right corner
                elif j == len(row) - 1:
                    count += c2i(box) == c2i(board[i][j - 1])
                    count += c2i(box) == c2i(board[i - 1][j])
                # bottom side
                else:
                    count += c2i(box) == c2i(board[i][j + 1])
                    count += c2i(box) == c2i(board[i][j - 1])
                    count += c2i(box) == c2i(board[i - 1][j])
            else:
                # left side
                if j == 0:
                    count += c2i(box) == c2i(board[i + 1][j])
                    count += c2i(box) == c2i(board[i - 1][j])
                    count += c2i(box) == c2i(board[i][j + 1])
                # right side
                elif j == len(row) - 1:
                    count += c2i(box) == c2i(board[i + 1][j])
                    count += c2i(box) == c2i(board[i - 1][j])
                    count += c2i(box) == c2i(board[i][j - 1])
                # middle
                else:
                    count += c2i(box) == c2i(board[i + 1][j])
                    count += c2i(box) == c2i(board[i - 1][j])
                    count += c2i(box) == c2i(board[i][j + 1])
                    count += c2i(box) == c2i(board[i][j - 1])

            # non continuous
            # does this make the other check irrelevant? is this necessary?
            if count < 1:
                return False

            # overfolding
            if count > 2:
                return False

            if count == 1:
                if not isinstance(box, str):
                    return False

    return True
