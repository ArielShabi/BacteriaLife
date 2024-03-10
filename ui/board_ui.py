from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene
from PyQt5.QtSvg import QGraphicsSvgItem
from PyQt5.QtCore import QSizeF

from models.board import Board


class BoardUi(QGraphicsView):
    def __init__(self, board: Board):
        super().__init__()
        self.board = board
        self.initUI(board.width, board.height)

    def initUI(self, x, y):
        # Create a scene
        self.scene = QGraphicsScene()

        # Set the size of the scene (board dimensions)
        self.scene.setSceneRect(0, 0, x, y)

        # Add SVG items to the scene at desired positions

        for bacteria, locations in self.board.bacterias:
            svg_item1 = QGraphicsSvgItem("assets/bacteria.svg")
            svg_item1.setScale(0.1)
            self.scene.addItem(svg_item1)
            svg_item1.setPos(locations[0][0], locations[0][1])

        # Set the scene to the view
        self.setScene(self.scene)
