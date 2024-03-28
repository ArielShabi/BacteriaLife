from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget


class Toast(QWidget):
    """
    A custom toast widget for displaying temporary messages.

    Args:
        duration (int): The duration in milliseconds for which the toast should be displayed. Default is 2000ms.

    Attributes:
        duration (int): The duration in milliseconds for which the toast should be displayed.

    """

    def __init__(self, duration: int = 2000) -> None:
        """
        Initializes the Toast widget.

        Args:
            duration (int): The duration in milliseconds for which the toast should be displayed. Default is 2000ms.

        """
        super().__init__()
        self.duration = duration
        self.init_ui()

    def init_ui(self) -> None:
        """
        Initializes the user interface of the Toast widget.

        """
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
        """
        Displays the toast with the specified message.

        Args:
            message (str): The message to be displayed in the toast.

        """
        self.label.setText(message)

        QTimer.singleShot(self.duration, self.close_toast)
        self.show()

    def close_toast(self) -> None:
        """
        Closes the toast widget.

        """
        self.close()
