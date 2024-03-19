from abc import ABC, abstractmethod
from pyqtgraph.widgets import GraphicsView

from logic.history_saver import HistorySaver


class AbstractGraph(ABC):

    def __init__(self, history: HistorySaver):
        self.history = history

    @abstractmethod
    def create_graph(self) -> GraphicsView:
        pass

    @abstractmethod
    def update_data(self):
        pass
