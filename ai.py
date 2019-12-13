from move import Move
import time

NEGATIVE_ONE = -1  # Used to keep player and computer turns


class AI:
    """Class to control the computer portion of the game"""

    def __init__(self, cols, rows):
        self.columns = cols
        self.rows = rows
        self.white = 255
        self.black = 0
        self.legal_moves = {}  # {(x, y): val}
        self.cordinates = {}  # {(x,y): {(x1, y1), (x2, y2)}}
        self.disk_array = None
        self.move = Move(self.columns, self.rows, self.white, self.black)

    def find_moves(self, disk_array, open_positions):
        """Finds all legal moves for the ai"""
        self.move.possible_moves(disk_array, open_positions)
        self.legal_moves = sorted(
            self.move.legal_moves.items(), key=lambda x: x[1], reverse=True)
        if len(self.legal_moves) != 0:
            self.cordinates = self.move.cordinates[self.legal_moves[0][0]]
            return self.legal_moves[0][0][0], self.legal_moves[0][0][1]
        else:
            return NEGATIVE_ONE, NEGATIVE_ONE
