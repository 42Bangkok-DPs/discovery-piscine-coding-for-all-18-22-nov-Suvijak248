#!/usr/bin/env python3

from rush.ex00.checkmate import checkmate

def main():
    board = """\
R...
.K..
..P.
....\
"""
    checkmate(board)

if __name__ == "__main__":
    main()