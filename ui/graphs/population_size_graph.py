from abc import ABC, abstractmethod
import pyqtgraph as pg

from ui.graphs.abstract_graph import AbstractGraph


class PopulationSizeGraph(AbstractGraph):
    def create_graph(self) -> pg.PlotWidget:
        self.population_size_graph = pg.PlotWidget()
        self.plot = self.population_size_graph.plot()
        return self.population_size_graph

    def update_data(self):
        turns = self.history.turns

        population_size = [len(turn.bacterias) for turn in turns]

        self.population_size_graph.setXRange(1, len(turns))
        self.population_size_graph.setYRange(0, max(population_size))

        self.plot.setData(list(range(len(turns))), population_size)
