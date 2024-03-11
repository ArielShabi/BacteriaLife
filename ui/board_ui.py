from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene
from PyQt5.QtSvg import QGraphicsSvgItem
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QBrush, QPen


from models.board import Board
from models.food import Food
from ui.bacteria_ui import BacteriaUI
from ui.food_ui import FoodUI


class BoardUi(QGraphicsView):
    def __init__(self, board: Board):
        super().__init__()
        self.board = board
        self.initUI()

    def initUI(self):
        self.scene: QGraphicsScene = QGraphicsScene()
        self.setStyleSheet("border: 1px solid black;")

        self.setScene(self.scene)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.scene.setSceneRect(0, 0, self.viewport(
        ).size().width(), self.viewport().size().height())

    def update_board(self, board: Board) -> None:
        self.board = board
        self.scene.clear()
        width_offset = self.rect().width() / self.board.width
        height_offset = self.rect().height() / self.board.height

        for bacteria, locations in self.board.bacterias:

            bacteria_ui = BacteriaUI(bacteria, width_offset, height_offset)

            max_x = self.rect().width()-bacteria_ui.scale() * \
                bacteria_ui.boundingRect().width()
            max_y = self.rect().height()-bacteria_ui.scale() * \
                bacteria_ui.boundingRect().height()
            food_x = min(max_x, width_offset * locations[0][0])
            food_y = min(max_y, height_offset * locations[0][1])
            self.scene.addItem(bacteria_ui)
            bacteria_ui.setPos(
                food_x, food_y)

        for food, location in self.board.foods:
            food_ui = FoodUI(food, width_offset, height_offset)

            max_x = self.rect().width()-food_ui.scale() * \
                food_ui.boundingRect().width()
            max_y = self.rect().height()-food_ui.scale() * \
                food_ui.boundingRect().height()
            food_x = min(max_x, width_offset * location[0])
            food_y = min(max_y, height_offset * location[1])
            self.scene.addItem(food_ui)
            food_ui.setPos(
                food_x, food_y)
