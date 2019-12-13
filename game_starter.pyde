# Processing file for Othello game
from board import Board

WIDTH = 800
HEIGHT = 800
COLUMNS = 8
ROWS = 8
DISK_DIAMETER = 90
NEGATIVE_ONE = -1
COMPUTERSTURN = -1
PLAYERSTURN = 1
PRINTTURN = 1

board = Board(WIDTH, HEIGHT, COLUMNS, ROWS, DISK_DIAMETER)


# Sets up the game
def setup():
    size(WIDTH, HEIGHT)
    answer = input('enter your name')
    if answer:
        print('hi ' + answer)
        board.human.name = answer
    elif answer == '':
        print('[empty string]')
    else:
        print(answer)  # Canceled dialog will print None


# Displays interactive text box to input player name
def input(self, message=''):
    from javax.swing import JOptionPane
    return JOptionPane.showInputDialog(frame, 'Enter Your Name')


# Displays the game setting
def draw():
    timer = board.timer
    turn = board.turn
    turn_print = board.turn_print
    background(0, 128, 0)
    board.display()
    if turn == PLAYERSTURN:
        board.human_legal_moves()
        if turn_print == PRINTTURN:
            print("{0}'s TURN".format(board.human.name))
            board.turn_print = 0
        if len(board.human.cordinates) > 0:
            if mousePressed and (mouseButton == LEFT):
                board.human_add_disk(pmouseX, pmouseY)
        else:
            board.human_add_disk(NEGATIVE_ONE, NEGATIVE_ONE)
    elif turn == COMPUTERSTURN:
        if turn_print == PRINTTURN:
            print("COMPUTER'S TURN")
            board.turn_print = 0
        if timer == 0:
            board.ai_add_disk()
        else:
            board.thinking_screen()
    board.game_status()
