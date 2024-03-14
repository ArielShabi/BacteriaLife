from PyQt5.QtWidgets import QWidget

STYLE_SHEETS_ROOT_FOLDER = "ui/stylesheets/"

def apply_style_sheet_file(widget: QWidget, filename: str):
    with open(STYLE_SHEETS_ROOT_FOLDER+filename, "r") as fh:
        widget.setStyleSheet(fh.read())
