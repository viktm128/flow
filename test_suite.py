# running test cases
from pathlib import Path
import helper
import pdb


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


