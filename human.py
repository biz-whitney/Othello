from move import Move


class Human:
    """Class to control the human player part of the game"""

    def __init__(self, cols, rows):
        self.columns = cols
        self.rows = rows
        self.name = "Player"
        self.white = 255
        self.black = 0
        self.legal_moves = set()
        self.cordinates = set()
        self.disk_array = None
        self.move = Move(self.columns, self.rows, self.black, self.white)

    def find_moves(self, disk_array, open_positions):
        """Finds all legal moves for the human player"""
        self.move.possible_moves(disk_array, open_positions)
        self.legal_moves = set(self.move.legal_moves.keys())
        self.cordinates = self.move.cordinates
