from typing import Union
from PyQt5.QtWidgets import QWidget

STYLE_SHEETS_ROOT_FOLDER = "ui/stylesheets/"


def apply_style_sheet_file(widget: QWidget, filename: Union[str, list[str]]):
    if isinstance(filename, str):
        filenames = [filename]
    elif isinstance(filename, list):
        filenames = filename

    style_sheet = ""
    for file in filenames:
        with open(STYLE_SHEETS_ROOT_FOLDER + file, "r") as fh:
            style_sheet += fh.read()

    widget.setStyleSheet(style_sheet)
