from disk import Disk
from ai import AI
from human import Human
import time

TIMERVALUE, TEXTSIZE, NEGATIVE_ONE, PRINTVALUE = 100, 50, -1, 1


class Board:
    """Draws the board and handles disk interactions"""

    def __init__(self, width, height, columns, rows, diameter):
        self.WHITE = 255  # rgb for white
        self.BLACK = 0  # rgb for black
        self.width = width  # width of the game board
        self.height = height  # height of the game board
        self.columns = columns
        self.rows = rows
        self.disk_diameter = diameter  # diameter of the disks
        self.tile_width = self.width / self.columns
        self.tile_height = self.height / self.rows
        self.total_disk = self.columns * self.rows
        self.white_disk = 0
        self.black_disk = 0
        self.turn = 1  # keeps track of white and black turns
        self.turn_print = PRINTVALUE  # prints player or computer's turn
        self.timer = TIMERVALUE
        self.game_over = False
        self.open_positions = self.find_possible_positions()
        self.disk_array = self.set_board()
        self.ai = AI(self.columns, self.rows)
        self.human = Human(self.columns, self.rows)
        self.write_result = True

    def find_possible_positions(self):
        """Finds all possible positions on the board"""
        pos_set = set()
        for i in range(self.columns):
            for j in range(self.rows):
                pos_set.add((i, j))
        return pos_set

    def human_legal_moves(self):
        """Finds all legal moves for the human player"""
        self.human.find_moves(self.disk_array, self.open_positions)

    def ai_legal_moves(self):
        """Finds all legal moves for the computer"""
        x, y = self.ai.find_moves(self.disk_array, self.open_positions)
        return x, y

    def human_add_disk(self, x, y):
        """Adds disk onto the board for the human player"""
        self.human_legal_moves()
        i = int(x // self.tile_width)
        j = int(y // self.tile_height)
        if len(self.human.cordinates) > 0:
            if (i, j) in self.human.legal_moves:
                self.black_disk += 1
                x_pos = self.tile_width * i + self.tile_width / 2
                y_pos = self.tile_height * j + self.tile_height / 2
                self.disk_array[i][j] = Disk(
                    self.BLACK, x_pos, y_pos, self.disk_diameter)
                self.flip_disks(self.human.cordinates[(i, j)], self.BLACK)
                self.black_disk += len(self.human.cordinates[(i, j)])
                self.white_disk -= len(self.human.cordinates[(i, j)])
                self.open_positions.discard((i, j))
                self.turn *= NEGATIVE_ONE
                self.turn_print = PRINTVALUE
        elif len(self.human.cordinates) == 0:
            self.turn *= NEGATIVE_ONE
            self.turn_print = PRINTVALUE

    def ai_add_disk(self):
        """Adds disk onto the board for the ai"""
        x, y = self.ai_legal_moves()
        if x != NEGATIVE_ONE and y != NEGATIVE_ONE:
            spacer = self.tile_height / 2
            self.disk_array[x][y] = Disk(
                self.WHITE, x * self.tile_width + spacer,
                y * self.tile_height + spacer, self.disk_diameter)
            self.flip_disks(self.ai.cordinates, self.WHITE)
            self.open_positions.discard((x, y))
            self.white_disk += 1 + len(self.ai.cordinates)
            self.black_disk -= len(self.ai.cordinates)
        self.turn *= NEGATIVE_ONE
        self.timer = TIMERVALUE
        self.turn_print = PRINTVALUE

    def thinking_screen(self):
        """Prints Thinking during ai's turn"""
        TEXTSTARTWIDTH = self.width / 2 - 200
        TEXTSTARTHEIGHT = self.height / self.rows
        red = (255, 0, 0)
        fill(red[0], red[1], red[2])
        textSize(TEXTSIZE)
        text("Thinking ...", TEXTSTARTWIDTH, TEXTSTARTHEIGHT)
        self.timer -= 1

    def flip_disks(self, points, color):
        """Flips opponents disks """
        for p in points:
            x = p[0]
            y = p[1]
            self.disk_array[x][y].color = color
            self.disk_array[x][y].display

    def set_board(self):
        """sets up the board with four disks in the middle"""
        disk_array = [[Disk("None", x, y, self.disk_diameter) for x in
                       range(self.rows)] for y in range(self.columns)]
        i = (self.rows // 2) - 1
        j = (self.columns // 2) - 1
        x_pos = self.tile_width * i + self.tile_width / 2
        y_pos = self.tile_height * j + self.tile_height / 2
        disk_array[i][j] = Disk(self.WHITE, x_pos, y_pos, self.disk_diameter)
        disk_array[i + 1][j] = Disk(self.BLACK, x_pos +
                                    self.tile_width, y_pos, self.disk_diameter)
        disk_array[i][j + 1] = Disk(self.BLACK, x_pos,
                                    y_pos + self.tile_height,
                                    self.disk_diameter)
        disk_array[i + 1][j + 1] = Disk(self.WHITE, x_pos + self.tile_width,
                                        y_pos + self.tile_height,
                                        self.disk_diameter)
        self.white_disk = 2  # starts with two white disks
        self.black_disk = 2  # starts with two black disks
        self.open_positions.discard((i, j))
        self.open_positions.discard((i, j + 1))
        self.open_positions.discard((i + 1, j))
        self.open_positions.discard((i + 1, j + 1))
        return disk_array

    def display(self):
        """Displays the board and the disks on the board"""
        NUM_ONE = 1
        NUM_ZERO = 0
        for i in range(NUM_ONE, self.columns):
            line(i * self.tile_width, NUM_ZERO,
                 i * self.tile_width, self.height)
            stroke(0.0, 0.0, 10)
            strokeWeight(2)
        for i in range(NUM_ONE, self.rows):
            line(NUM_ZERO, i * self.tile_height,
                 self.width, i * self.tile_height)
            stroke(0.0, 0.0, 10)
            strokeWeight(2)
        for i in range(len(self.disk_array)):
            for j in range(len(self.disk_array[i])):
                self.disk_array[i][j].display()

    def write_to_file(self):
        """Writes the result into the scores.txt file"""
        try:
            f = open("scores.txt", "r+")
        except:
            f = open("scores.txt", "w")
            f = open("scores.txt", "r+")
        words = f.readline().split()
        if len(words) == 0:
            f = open("scores.txt", "a+")
            f.write("{0} {1} \n".format(self.human.name, self.black_disk))
        elif int(words[1]) >= self.black_disk:
            f = open("scores.txt", "a+")
            f.write("{0} {1} \n".format(self.human.name, self.black_disk))
        else:
            with open('scores.txt', 'r') as original:
                data = original.read()
            with open('scores.txt', 'w') as modified:
                modified.write("{0} {1} \n".format(
                    self.human.name, self.black_disk) + data)
        f.close()

    def game_status(self):
        """Checks if the game is over and displays result"""
        TEXTSTARTWIDTH = self.width / 2 - 200
        TEXTSTARTHEIGHT = self.height / self.rows
        if self.total_disk == (self.black_disk + self.white_disk) or \
                (len(self.ai.legal_moves) == 0 and
                 len(self.human.cordinates) == 0):
            self.display()
            if self.game_over:
                time.sleep(0.75)
                background(150)
                if self.write_result:
                    self.write_to_file()
                    self.write_result = False
                if self.black_disk > self.white_disk:
                    fill(1)
                    textSize(TEXTSIZE)
                    text("{0} Wins \n WITH SCORE \n OF {1}".format(
                        self.human.name, self.black_disk), TEXTSTARTWIDTH,
                        TEXTSTARTHEIGHT)
                elif self.black_disk < self.white_disk:
                    fill(1)
                    textSize(TEXTSIZE)
                    text("Computer Wins \n WITH SCORE \n OF {0}".format(
                        self.white_disk), TEXTSTARTWIDTH,
                        TEXTSTARTHEIGHT)
                else:
                    fill(1)
                    textSize(TEXTSIZE)
                    text("TIE GAME \n WITH SCORE \n OF {0}".format(
                        self.black_disk), TEXTSTARTWIDTH,
                        TEXTSTARTHEIGHT)
            self.game_over = True
