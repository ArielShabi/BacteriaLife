import pyqtgraph as pg
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QGridLayout

from logic.history_saver import HistorySaver
from ui.graphs.abstract_graph import AbstractGraph
from ui.graphs.population_size_graph import PopulationSizeGraph


class GraphPage(QWidget):
    def __init__(self, history_saver: HistorySaver):
        super().__init__()
        self.history = history_saver
        self.graphs: list[AbstractGraph] = [
            PopulationSizeGraph(history_saver),
            PopulationSizeGraph(history_saver)
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
            graph_widget.setBackground('w')
            self.grid.addWidget(graph_widget, 1+i, i % 2)

        self.setLayout(self.grid)

    def on_page_set(self):
        for graph in self.graphs:
            graph.update_data()

    def set_population_size_graph(self):
        self.population_size_graph = pg.PlotWidget()
        self.population_size_graph.setBackground('w')

        turns = self.history.turns

        population_size = [len(turn.bacterias) for turn in turns]

        self.population_size_graph.setXRange(1, len(turns))

        self.population_size_graph.plot(
            range(len(turns)+1, 1), population_size)

        self.graphs.append(self.population_size_graph)

    def set_population_size_graph2(self):
        self.population_size_graph2 = pg.PlotWidget()
        time = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        temperature = [30, 32, 34, 32, 33, 31, 29, 32, 35, 30]
        self.population_size_graph2.plot(time, temperature)
        self.graphs.append(self.population_size_graph2)

    def set_population_size_graph3(self):
        self.population_size_graph3 = pg.PlotWidget()
        time = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        temperature = [30, 32, 34, 32, 33, 31, 29, 32, 35, 30]
        self.population_size_graph3.plot(time, temperature)
        self.graphs.append(self.population_size_graph3)

    def set_population_size_graph4(self):
        self.population_size_graph4 = pg.PlotWidget()
        time = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        temperature = [30, 32, 34, 32, 33, 31, 29, 32, 35, 30]
        self.population_size_graph4.plot(time, temperature)
        self.graphs.append(self.population_size_graph4)
