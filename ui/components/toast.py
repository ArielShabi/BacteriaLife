from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget


class Toast(QWidget):
    def __init__(self, duration: int = 2000) -> None:
        super().__init__()
        self.duration = duration
        self.init_ui()

    def init_ui(self) -> None:
        layout = QVBoxLayout()
        self.label = QLabel("toast")
        self.label.setStyleSheet(
            "background-color: #9ACD32; color: black; padding: 8px; border-radius: 4px;")
        layout.addWidget(self.label)
        self.setLayout(layout)

        self.setWindowTitle("Toast")
        self.setWindowFlags(self.windowFlags() |
                            Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)

    def show_toast(self, message: str) -> None:
        self.label.setText(message)

        QTimer.singleShot(self.duration, self.close_toast)
        self.show()

    def close_toast(self) -> None:
        self.close()
