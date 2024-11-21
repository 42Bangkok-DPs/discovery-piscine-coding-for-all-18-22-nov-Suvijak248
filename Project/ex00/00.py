def checkmate(board):
    board = board.strip().split('\n')
    n = len(board)
    king_pos = None
    
    directions = {
        'R': [(0, 1), (1, 0), (0, -1), (-1, 0)],  # Rook
        'B': [(1, 1), (1, -1), (-1, 1), (-1, -1)],  # Bishop
        'Q': [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)],  # Queen
    }
    pawn_moves = [(-1, -1), (-1, 1)]  # Pawns capture diagonally forward

    for i in range(n):
        for j in range(n):
            if board[i][j] == 'K':
                king_pos = (i, j)
                break
        if king_pos:
            break

    if not king_pos:
        print("Fail")
        return
    
    def can_attack(i, j, x, y, piece):
        if piece in directions:
            for dx, dy in directions[piece]:
                nx, ny = i + dx, j + dy
                while 0 <= nx < n and 0 <= ny < n:
                    if (nx, ny) == (x, y):  # King found in the path
                        return True
                    if board[nx][ny] != '.':  # Blocked by another piece
                        break
                    nx, ny = nx + dx, ny + dy
        
        elif piece == 'P':
            for dx, dy in pawn_moves:
                if (i + dx, j + dy) == (x, y):
                    return True
        
        return False
    
    for i in range(n):
        for j in range(n):
            piece = board[i][j]
            if piece in directions or piece == 'P':
                if can_attack(i, j, king_pos[0], king_pos[1], piece):
                    print("Success")
                    return
    
    print("Fail")