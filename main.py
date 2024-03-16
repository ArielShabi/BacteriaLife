import sys
from PyQt5.QtWidgets import QApplication

from ui.main_window import MainWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)

    font = app.font()
    font.setFamily("Roboto")
    font.setPointSize(10)

    app.setFont(font)

    window = MainWindow()
    app.main_window = window
    window.show()
    sys.exit(app.exec_())
