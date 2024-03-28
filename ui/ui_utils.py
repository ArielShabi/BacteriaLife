from typing import Union
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPainter, QPixmap, QColor
from PyQt5.QtSvg import QSvgRenderer


STYLE_SHEETS_ROOT_FOLDER = "ui/stylesheets/"


def apply_style_sheet_file(widget: QWidget, filename: Union[str, list[str]]) -> None:
    """
    Apply a style sheet file to a QWidget.

    Args:
        widget (QWidget): The widget to apply the style sheet to.
        filename (Union[str, list[str]]): The filename or list of filenames of the style sheet file(s).

    Returns:
        None
    """
    if isinstance(filename, str):
        filenames = [filename]
    elif isinstance(filename, list):
        filenames = filename

    style_sheet = ""
    for file in filenames:
        with open(STYLE_SHEETS_ROOT_FOLDER + file, "r") as fh:
            style_sheet += fh.read()

    widget.setStyleSheet(style_sheet)


def create_colored_icon(svg_path: str, color: QColor) -> QIcon:
    """
    Create a colored QIcon from an SVG file.

    Args:
        svg_path (str): The path to the SVG file.
        color (QColor): The color to apply to the SVG.

    Returns:
        QIcon: The colored QIcon.
    """
    renderer = QSvgRenderer(svg_path)
    pixmap = QPixmap(renderer.defaultSize())
    pixmap.fill(Qt.GlobalColor.transparent)
    painter = QPainter(pixmap)
    renderer.render(painter)
    painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
    painter.fillRect(pixmap.rect(), QColor(color))
    painter.end()
    return QIcon(pixmap)
