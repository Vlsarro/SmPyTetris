import sys
import random
from PyQt4 import QtCore, QtGui


class Tetris(QtGui.QMainWindow):

    def __init__(self):
        super(Tetris, self).__init__()

        self.initUI()

    def initUI(self):

        pass


class Board(QtGui.QFrame):

    def __init__(self, parent):
        super(Board, self).__init__(parent)

        self.initBoard()

    def initBoard(self):

        pass


class Tetrominoe(object):

    NoShape = 0
    ZShape = 1
    SShape = 2
    LineShape = 3
    TShape = 4
    SquareShape = 5
    LShape = 6
    MirroredLShape = 7


class Shape(object):

    pass


def main():

    app = QtGui.QApplication([])
    tetris = Tetris()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
