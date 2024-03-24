import pyqtgraph as pg

from ui.graphs.abstract_graph import AbstractGraph

GRAPH_COLOR = "#B600FF"


class PopulationSizeGraph(AbstractGraph):
    def create_graph(self) -> pg.PlotWidget:
        self.population_size_graph = pg.PlotWidget()
        self.population_size_graph.setTitle('Population vs Time')
        self.population_size_graph.setLabel('left', 'Population size')
        self.population_size_graph.setLabel('bottom', 'Time (turns)')
        self.plot = self.population_size_graph.plot()
        self.plot.setPen(GRAPH_COLOR)
        return self.population_size_graph

    def update_data(self)-> None:
        turns = self.history.turns

        if len(turns) == 0:
            return

        population_size = [len(turn.bacterias) for turn in turns]

        self.population_size_graph.setXRange(1, len(turns))
        self.population_size_graph.setYRange(0, max(population_size))

        self.plot.setData(list(range(len(turns))), population_size)
