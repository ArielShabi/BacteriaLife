from datetime import datetime
from typing import Callable, List
from PyQt5.QtWidgets import QWidget, QPushButton, QGridLayout
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt
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
    def __init__(self, change_page: Callable[[], None], history_saver: HistorySaver, game: GameRunner) -> None:
        super().__init__()

        self.change_page = change_page

        self.history = history_saver
        self.graphs: List[AbstractGraph] = [
            PopulationSizeGraph(history_saver),
            AverageStatsGraph(history_saver),
            FoodAmountGraph(history_saver),
            StatsScatterGraph(history_saver)
        ]

        game.add_listener(ON_TURN_FINISHED, lambda _: self.__update_graphs())

        self.initUI()

    def initUI(self) -> None:
        self.go_back_button = QPushButton()
        self.go_back_button.setIcon(QIcon("assets/back.svg"))
        self.go_back_button.setFixedSize(BUTTON_SIZE, BUTTON_SIZE)
        self.go_back_button.clicked.connect(self.change_page)

        self.download_button = QPushButton()
        self.download_button.setIcon(QIcon("assets/download.svg"))
        self.download_button.setFixedSize(BUTTON_SIZE, BUTTON_SIZE)
        self.download_button.clicked.connect(self.__save_graphs_to_file)

        self.page_grid = QGridLayout()

        self.setLayout(self.page_grid)

        self.page_grid.addWidget(self.go_back_button, 0, 0)
        self.page_grid.addWidget(self.download_button,
                                 0, 1, alignment=Qt.AlignmentFlag.AlignRight)

        graph_grid = QGridLayout()

        for i in range(len(self.graphs)):
            graph_creator = self.graphs[i]
            graph_widget = graph_creator.create_graph()
            graph_widget.setBackground(DARK_GRAPH_BACKGROUND)
            graph_grid.addWidget(graph_widget, (i//2), i % 2)

        self.graphs_container = QWidget()
        self.graphs_container.setLayout(graph_grid)

        self.page_grid.addWidget(self.graphs_container, 1, 0, 1, 2)

        self.setLayout(self.page_grid)

    def on_page_set(self) -> None:
        self.__update_graphs()

    def __update_graphs(self) -> None:
        for graph in self.graphs:
            graph.update_data()

    def __save_graphs_to_file(self) -> None:
        geometry = self.graphs_container.geometry()

        pixmap = QPixmap(geometry.size())

        self.graphs_container.render(pixmap)

        pixmap.save(f'graphs_{datetime.now().strftime(
            "%Y-%m-%d %H_%M_%S %f")}.png', 'PNG')
