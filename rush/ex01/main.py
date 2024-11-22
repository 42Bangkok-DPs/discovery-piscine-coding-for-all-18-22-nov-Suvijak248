#!/usr/bin/env python3
import sys
from checkmate import is_king_checked

def read_board(file_path):
    try:
        with open(file_path, 'r') as f:
            board = [line.strip() for line in f.readlines()]
            # Ensure all rows are of the same length (square board)
            if all(len(row) == len(board) for row in board):
                return board
            else:
                return None
    except FileNotFoundError:
        return None

def is_valid_board(board):
    if board is None:
        return False
    
    king_count = sum(row.count('K') for row in board)
    # There must be exactly one King on the board
    if king_count != 1:
        return False

    # Check if all rows are of equal length (square board)
    board_size = len(board)
    if not all(len(row) == board_size for row in board):
        return False

    return True

def process_board(board):
    if not is_valid_board(board):
        return "Error"
    try:
        if is_king_checked(board):
            return "Success"
        else:
            return "Fail"
    except Exception:
        return "Error"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <file1.chess> [file2.chess ...] | cat -e$")
        sys.exit(1)

    for file_path in sys.argv[1:]:
        board = read_board(file_path)
        print(process_board(board))