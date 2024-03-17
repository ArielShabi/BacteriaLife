import sys
from PyQt5.QtWidgets import QApplication

from ui.main_window import MainWindow
from ui.components.proxy_style import ProxyStyle

if __name__ == "__main__":
    app = QApplication(sys.argv)

    font = app.font()
    font.setFamily("Roboto")
    font.setPointSize(10)

    app.setFont(font)
    app.setStyle(ProxyStyle())

    window = MainWindow()
    app.main_window = window
    window.show()
    sys.exit(app.exec_())
