import sys
from PyQt5.QtWidgets import QApplication

from ui.main_window import MainWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    app.main_window = window  # Create a reference cycle
    window.show()
    sys.exit(app.exec_())
