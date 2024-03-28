from typing import Optional
from PyQt5.QtCore import QTimer, QObject, pyqtSignal


from PyQt5.QtCore import QObject, QTimer, pyqtSignal
from typing import Optional

class Timer(QObject):
    """
    A class that represents a timer.

    Args:
        interval (int): The interval in milliseconds between each timeout signal.

    Attributes:
        timeout (pyqtSignal): A signal emitted when the timer times out.
        timer (QTimer): The underlying QTimer object used for timing.
        interval (int): The interval in milliseconds between each timeout signal.

    """

    timeout = pyqtSignal()

    def __init__(self, interval: int) -> None:
        super().__init__()
        self.timer: QTimer = QTimer(self)
        self.timer.timeout.connect(self.timeout.emit)
        self.interval = interval

    def start(self, interval: Optional[int] = None) -> None:
        """
        Starts the timer.

        Args:
            interval (int, optional): The interval in milliseconds between each timeout signal. If provided, it will override the interval set during initialization.

        """
        if interval:
            self.interval = interval
        self.timer.start(self.interval)

    def stop(self) -> None:
        """
        Stops the timer.

        """
        self.timer.stop()

    def is_alive(self) -> bool:
        """
        Checks if the timer is currently running.

        Returns:
            bool: True if the timer is running, False otherwise.

        """
        return self.timer.isActive()
