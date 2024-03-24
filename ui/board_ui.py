from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene, QSizePolicy
from PyQt5.QtCore import Qt
from PyQt5.QtSvg import QGraphicsSvgItem


from helpers.color import get_bacteria_color, get_food_color, get_portal_color
from models.board import Board
from models.board_data import BoardData
from models.food import Food
from project_types import Location
from ui.bacteria_ui import BoardItemSvg
from ui.food_ui import FoodUI
from ui.ui_utils import apply_style_sheet_file

CSS_FILE = "board.css"

BACTERIA_SVG = "assets/bacteria.svg"
FOOD_SVG = "assets/apple.svg"
PORTAL_SVG = "assets/magic-portal.svg"


class BoardUi(QGraphicsView):
    def __init__(self, board: BoardData):
        super().__init__()
        self.board = board
        self.initUI()

    def initUI(self):
        self.scene: QGraphicsScene = QGraphicsScene()

        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        apply_style_sheet_file(self, CSS_FILE)
        self.setScene(self.scene)
        self.fitInView(self.scene.sceneRect(), Qt.KeepAspectRatio)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.scene.setSceneRect(0, 0, self.viewport(
        ).size().width(), self.viewport().size().height())
        self.update_board(self.board)

    def update_board(self, board: BoardData) -> None:
        self.board = board
        self.scene.clear()
        width_offset = self.rect().width() / self.board.width
        height_offset = self.rect().height() / self.board.height

        for bacteria, bacteria_location in self.board.bacterias:

            bacteria_ui = BoardItemSvg(BACTERIA_SVG, get_bacteria_color(
                bacteria.properties), width_offset, height_offset)

            self.__add_item(width_offset, height_offset,
                            bacteria_location, bacteria_ui)

        for food, location in self.board.foods:
            food_ui = BoardItemSvg(FOOD_SVG, get_food_color(
                food), width_offset, height_offset)
            self.__add_item(width_offset, height_offset, location, food_ui)

        if (self.board.magic_door):
            food_ui = BoardItemSvg(
                PORTAL_SVG, get_portal_color(), width_offset, height_offset)
            self.__add_item(width_offset, height_offset,
                            self.board.magic_door[0], food_ui)

    def __add_item(self, width_offset: float, height_offset: float, location: Location, svg: QGraphicsSvgItem):
        max_x = self.rect().width()-svg.scale() * \
            svg.boundingRect().width()
        max_y = self.rect().height()-svg.scale() * \
            svg.boundingRect().height()
        item_x = min(max_x, width_offset * location[1])
        item_y = min(max_y,  height_offset * location[0])
        self.scene.addItem(svg)
        svg.setPos(
            item_x, item_y)
