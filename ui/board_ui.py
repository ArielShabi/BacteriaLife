from typing import Optional
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene, QSizePolicy
from PyQt5.QtCore import Qt
from PyQt5.QtSvg import QGraphicsSvgItem
from PyQt5.QtGui import QResizeEvent

from helpers.color import get_bacteria_color, get_food_color, get_portal_color
from models.board_data import BoardData
from project_types import Location
from ui.bacteria_ui import BoardItemSvg
from ui.ui_utils import apply_style_sheet_file

CSS_FILE = "board.css"

BACTERIA_SVG = "assets/bacteria.svg"
FOOD_SVG = "assets/apple.svg"
PORTAL_SVG = "assets/magic-portal.svg"


class BoardUi(QGraphicsView):
    def __init__(self, board: BoardData):
        """
        Initializes the BoardUi class.

        Args:
            board (BoardData): The board data.

        Returns:
            None
        """
        super().__init__()
        self.board = board
        self.initUI()

    def initUI(self) -> None:
        """
        Initializes the user interface.

        Returns:
            None
        """
        self.board_scene: QGraphicsScene = QGraphicsScene()

        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        apply_style_sheet_file(self, CSS_FILE)
        self.setScene(self.board_scene)
        self.fitInView(self.board_scene.sceneRect(),
                       Qt.AspectRatioMode.KeepAspectRatio)

    def resizeEvent(self, event: Optional[QResizeEvent]) -> None:
        """
        Handles the resize event.

        Args:
            event (Optional[QResizeEvent]): The resize event.

        Returns:
            None
        """
        super().resizeEvent(event)
        view_port = self.viewport()

        if view_port is None:
            return

        self.board_scene.setSceneRect(
            0, 0, view_port.size().width(), view_port.size().height())
        self.update_board(self.board)

    def update_board(self, board: BoardData) -> None:
        """
        Updates the board with new data.

        Args:
            board (BoardData): The updated board data.

        Returns:
            None
        """
        self.board = board
        self.board_scene.clear()
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

    def __add_item(self, width_offset: float, height_offset: float,
                   location: Location, svg: QGraphicsSvgItem
                   ) -> None:
        """
        Adds an item to the board scene.

        Args:
            width_offset (float): The width offset.
            height_offset (float): The height offset.
            location (Location): The location of the item.
            svg (QGraphicsSvgItem): The SVG item to add.

        Returns:
            None
        """
        max_x = self.rect().width()-svg.scale() * \
            svg.boundingRect().width()
        max_y = self.rect().height()-svg.scale() * \
            svg.boundingRect().height()
        item_x = min(max_x, width_offset * location[1])
        item_y = min(max_y,  height_offset * location[0])
        self.board_scene.addItem(svg)
        svg.setPos(
            item_x, item_y)
