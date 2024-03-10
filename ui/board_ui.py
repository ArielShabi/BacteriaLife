from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene
from PyQt5.QtSvg import QGraphicsSvgItem
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QBrush, QPen


from models.board import Board
from ui.bacteria_ui import BacteriaUI


class BoardUi(QGraphicsView):
    def __init__(self, board: Board):
        super().__init__()
        self.board = board
        self.initUI()

    def initUI(self):
        self.scene: QGraphicsScene = QGraphicsScene()
        self.setStyleSheet("border: 1px solid black;")

        self.setScene(self.scene)

    def update_board(self, board: Board) -> None:
        self.board = board
        self.scene.clear()
        width_offset = self.rect().width() / self.board.width
        height_offset = self.rect().height() / self.board.height
        for bacteria, locations in self.board.bacterias:

            bacteria_ui = BacteriaUI(bacteria, width_offset, height_offset)

            self.scene.addItem(bacteria_ui)
            bacteria_ui.setPos(
                width_offset*locations[0][0], height_offset * locations[0][1])
