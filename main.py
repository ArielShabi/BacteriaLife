import sys
from PyQt5.QtWidgets import QApplication

from ui.main_window import MainWindow

def show_help():
    print("Usage: python main.py")
    print("Runs the bacteria life simulation GUI.")
    print("Enjoy :)")


if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == "--help":
        show_help()
        sys.exit(0)
    
    
    app = QApplication(sys.argv)

    font = app.font()
    font.setFamily("Roboto")
    font.setPointSize(10)

    app.setFont(font)

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


