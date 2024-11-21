import sys
from checkmate import is_king_checked

def is_king_checked(board):
    king_position = None

    # Locate the King on the board
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == 'K':
                king_position = (i, j)
                break
        if king_position:
            break

    if not king_position:
        raise ValueError("No King found on the board")

    # Define the logic to check for threats to the King
    # This part needs to evaluate surrounding pieces according to chess rules

    # Example: Check for threats in adjacent cells (simplistic case)
    x, y = king_position
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(board) and 0 <= ny < len(board[0]):
            if board[nx][ny] in {'Q', 'R', 'B'}:  # Example: Queen, Rook, Bishop threaten King
                return True

    return False
