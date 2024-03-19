from typing import Callable
from PyQt5.QtWidgets import QWidget, QPushButton, QGridLayout
from PyQt5.QtGui import QIcon

from const import BUTTON_SIZE
from logic.game_runner import ON_TURN_FINISHED, GameRunner
from logic.history_saver import HistorySaver
from ui.graphs.abstract_graph import AbstractGraph
from ui.graphs.average_stats_graph import AverageStatsGraph
from ui.graphs.food_amount_graph import FoodAmountGraph
from ui.graphs.population_size_graph import PopulationSizeGraph
from ui.graphs.stats_scatter_graph import StatsScatterGraph

DARK_GRAPH_BACKGROUND = "#444444"


class GraphPage(QWidget):
    def __init__(self, change_page: Callable, history_saver: HistorySaver, game: GameRunner):
        super().__init__()
        
        self.change_page = change_page
        
        self.history = history_saver
        self.graphs: list[AbstractGraph] = [
            PopulationSizeGraph(history_saver),
            AverageStatsGraph(history_saver),
            FoodAmountGraph(history_saver),
            StatsScatterGraph(history_saver)
        ]

        game.add_listener(ON_TURN_FINISHED, lambda _: self.__update_graphs())

        self.initUI()

    def initUI(self):
        self.go_back_button = QPushButton(icon=QIcon("assets/back.svg"))
        self.go_back_button.setFixedSize(BUTTON_SIZE, BUTTON_SIZE)
        self.go_back_button.clicked.connect(self.change_page)
        self.grid = QGridLayout()

        self.grid.addWidget(self.go_back_button, 0, 0)

        for i in range(len(self.graphs)):
            graph_creator = self.graphs[i]
            graph_widget = graph_creator.create_graph()
            graph_widget.setBackground(DARK_GRAPH_BACKGROUND)
            self.grid.addWidget(graph_widget, 1+(i//2), i % 2)

        self.setLayout(self.grid)

    def on_page_set(self):
        self.__update_graphs()

    def __update_graphs(self):
        for graph in self.graphs:
            graph.update_data()
