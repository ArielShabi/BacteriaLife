from PyQt5.QtCore import QTimer, QObject, pyqtSignal


class Timer(QObject):
    timeout = pyqtSignal()

    def __init__(self, interval=None) -> None:
        super().__init__()
        self.timer: QTimer = QTimer(self)
        self.timer.timeout.connect(self.timeout.emit)
        self.interval = interval

    def start(self, interval=None):
        if interval:
            self.interval = interval
        self.timer.start(self.interval)

    def stop(self):
        self.timer.stop()

    def is_alive(self):
        return self.timer.isActive()
