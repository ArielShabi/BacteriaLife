import pyqtgraph as pg
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QGridLayout

from logic.history_saver import HistorySaver
from ui.graphs.abstract_graph import AbstractGraph
from ui.graphs.average_stats_graph import AverageStatsGraph
from ui.graphs.food_amount_graph import FoodAmountGraph
from ui.graphs.population_size_graph import PopulationSizeGraph
from ui.graphs.stats_scatter_graph import StatsScatterGraph

DARK_GRAPH_BACKGROUND = "#444444"


class GraphPage(QWidget):
    def __init__(self, history_saver: HistorySaver):
        super().__init__()
        # FIX can be empty
        self.history = history_saver
        self.graphs: list[AbstractGraph] = [
            PopulationSizeGraph(history_saver),
            AverageStatsGraph(history_saver),
            FoodAmountGraph(history_saver),
            StatsScatterGraph(history_saver)
        ]

        self.initUI()

    def initUI(self):
        # self.layout = QVBoxLayout(self)
        self.go_back_button = QPushButton("Graph")
        self.grid = QGridLayout()

        self.grid.addWidget(self.go_back_button, 0, 0)

        for i in range(len(self.graphs)):
            graph_creator = self.graphs[i]
            graph_widget = graph_creator.create_graph()
            graph_widget.setBackground(DARK_GRAPH_BACKGROUND)
            self.grid.addWidget(graph_widget, 1+(i//2), i % 2)

        self.setLayout(self.grid)

    def on_page_set(self):
        for graph in self.graphs:
            graph.update_data()
