from typing import Optional
from PyQt5.QtCore import QTimer, QObject, pyqtSignal


class Timer(QObject):
    timeout = pyqtSignal()

    def __init__(self, interval: int) -> None:
        super().__init__()
        self.timer: QTimer = QTimer(self)
        self.timer.timeout.connect(self.timeout.emit)
        self.interval = interval

    def start(self, interval:  Optional[int] = None) -> None:
        if interval:
            self.interval = interval
        self.timer.start(self.interval)

    def stop(self) -> None:
        self.timer.stop()

    def is_alive(self) -> bool:
        return self.timer.isActive()
