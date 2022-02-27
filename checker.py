# check to see if a given board is completed correctly
# TODO how to import from helper.pysd

import pdb


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
            if 

    # any non endpoint is adjacent to exactly 2 same colored pieces
        # box[i+1][j], box[i-1][j], box[i][j+1], box[i][j-1]
        # if you are connected to 1, you need to be a letter
                    