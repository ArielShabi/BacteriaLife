from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtCore import QTimer,QPropertyAnimation, QPoint

from logic.game_runner import GameRunner
from ui.board_ui import BoardUi

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        game = GameRunner()
        game.create_board()
        self.game = game                
        self.board_ui = BoardUi(self.game.board)
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("Smooth Button Movement")
        self.setCentralWidget(self.board_ui)

        

