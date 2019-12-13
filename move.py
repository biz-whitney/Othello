class Move:
    """Class to check all possible legal moves"""

    def __init__(self, cols, rows, own_color, opponent_color):
        self.columns = cols
        self.rows = rows
        self.own_color = own_color
        self.opponent_color = opponent_color
        self.legal_moves = {}  # {(x, y): val}
        self.cordinates = {}  # {(x,y): {(x1, y1), (x2, y2)}}
        self.disk_array = None

    def possible_moves(self, disk_array, open_positions):
        """Checks possible moves on the current board"""
        self.legal_moves = {}
        self.cordinates = {}
        self.disk_array = disk_array
        for pos in open_positions:
            self.legal_moves[pos] = 0
            self.cordinates[pos] = set()
            if self.check_position(pos[0] + 1, pos[1] + 1):
                self.check_diagonal_one(pos, pos[0] + 1, pos[1] + 1)
            if self.check_position(pos[0] - 1, pos[1] - 1):
                self.check_diagonal_two(pos, pos[0] - 1, pos[1] - 1)
            if self.check_position(pos[0] + 1, pos[1] - 1):
                self.check_diagonal_three(pos, pos[0] + 1, pos[1] - 1)
            if self.check_position(pos[0] - 1, pos[1] + 1):
                self.check_diagonal_four(pos, pos[0] - 1, pos[1] + 1)
            if self.check_position(pos[0] + 1, pos[1]):
                self.check_horizontal_right(pos, pos[0] + 1, pos[1])
            if self.check_position(pos[0] - 1, pos[1]):
                self.check_horizontal_left(pos, pos[0] - 1, pos[1])
            if self.check_position(pos[0], pos[1] + 1):
                self.check_vertical_down(pos, pos[0], pos[1] + 1)
            if self.check_position(pos[0], pos[1] - 1):
                self.check_vertical_up(pos, pos[0], pos[1] - 1)
            if self.legal_moves[pos] == 0:
                self.legal_moves.pop(pos)
                self.cordinates.pop(pos)

    def check_position(self, x, y):
        """ Checks if a disk could be added to the x,y position"""
        try:
            if self.disk_array[x][y].color == self.opponent_color:
                return True
            return False
        except IndexError:
            return False

    def check_diagonal_one(self, pos, x, y):
        """Checks if opponents disks could be flipped
        going left and down from x,y"""
        count = 0
        position_set = {(x, y)}
        while x < self.columns and y < self.rows:
            if self.disk_array[x][y].color == self.opponent_color:
                position_set.add((x, y))
                count += 1
                x += 1
                y += 1
            elif self.disk_array[x][y].color == self.own_color:
                self.legal_moves[pos] += count
                for xy in position_set:
                    self.cordinates[pos].add(xy)
                return
            else:
                return

    def check_diagonal_two(self, pos, x, y):
        """Checks if opponents disks could be flipped
        going right and up from x,y"""
        count = 0
        position_set = set()
        while x >= 0 and y >= 0:
            if self.disk_array[x][y].color == self.opponent_color:
                position_set.add((x, y))
                count += 1
                x -= 1
                y -= 1
            elif self.disk_array[x][y].color == self.own_color:
                count += 1
                self.legal_moves[pos] += count
                for xy in position_set:
                    self.cordinates[pos].add(xy)
                return
            else:
                return

    def check_diagonal_three(self, pos, x, y):
        """Checks if opponents disks could be flipped
        going right and down from x,y"""
        count = 0
        position_set = {(x, y)}
        while x < self.columns and y >= 0:
            if self.disk_array[x][y].color == self.opponent_color:
                position_set.add((x, y))
                count += 1
                x += 1
                y -= 1
            elif self.disk_array[x][y].color == self.own_color:
                self.legal_moves[pos] += count
                for xy in position_set:
                    self.cordinates[pos].add(xy)
                return
            else:
                return

    def check_diagonal_four(self, pos, x, y):
        """Checks if opponents disks could be flipped
        going left and up from x,y"""
        count = 0
        position_set = {(x, y)}
        while x >= 0 and y < self.rows:
            if self.disk_array[x][y].color == self.opponent_color:
                position_set.add((x, y))
                count += 1
                x -= 1
                y += 1
            elif self.disk_array[x][y].color == self.own_color:
                self.legal_moves[pos] += count
                for xy in position_set:
                    self.cordinates[pos].add(xy)
                return
            else:
                return

    def check_horizontal_right(self, pos, x, y):
        """Checks if opponents disks could be flipped going right from x,y"""
        count = 0
        position_set = {(x, y)}
        while x < self.columns:
            if self.disk_array[x][y].color == self.opponent_color:
                position_set.add((x, y))
                count += 1
                x += 1
            elif self.disk_array[x][y].color == self.own_color:
                self.legal_moves[pos] += count
                for xy in position_set:
                    self.cordinates[pos].add(xy)
                return
            else:
                return

    def check_horizontal_left(self, pos, x, y):
        """Checks if opponents disks could be flipped going left from x,y"""
        count = 0
        position_set = {(x, y)}
        while x >= 0:
            if self.disk_array[x][y].color == self.opponent_color:
                position_set.add((x, y))
                count += 1
                x -= 1
            elif self.disk_array[x][y].color == self.own_color:
                self.legal_moves[pos] += count
                for xy in position_set:
                    self.cordinates[pos].add(xy)
                return
            else:
                return

    def check_vertical_down(self, pos, x, y):
        """Checks if opponents disks could be flipped going down from x,y"""
        count = 0
        position_set = {(x, y)}
        while y < self.rows:
            if self.disk_array[x][y].color == self.opponent_color:
                position_set.add((x, y))
                count += 1
                y += 1
            elif self.disk_array[x][y].color == self.own_color:
                self.legal_moves[pos] += count
                for xy in position_set:
                    self.cordinates[pos].add(xy)
                return
            else:
                return

    def check_vertical_up(self, pos, x, y):
        """Checks if opponents disks could be flipped going up from x,y"""
        count = 0
        position_set = {(x, y)}
        while y >= 0:
            if self.disk_array[x][y].color == self.opponent_color:
                position_set.add((x, y))
                count += 1
                y -= 1
            elif self.disk_array[x][y].color == self.own_color:
                self.legal_moves[pos] += count
                for xy in position_set:
                    self.cordinates[pos].add(xy)
                return
            else:
                return
