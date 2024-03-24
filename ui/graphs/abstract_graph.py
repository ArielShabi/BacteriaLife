from abc import ABC, abstractmethod
from pyqtgraph import GraphicsView

from logic.history_saver import HistorySaver


class AbstractGraph(ABC):

    def __init__(self, history: HistorySaver):
        self.history = history

    @abstractmethod
    def create_graph(self) -> GraphicsView:
        pass

    @abstractmethod
    def update_data(self) -> None:
        pass
