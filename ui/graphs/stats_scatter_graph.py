from collections import defaultdict
import functools
from pyqtgraph import PlotWidget, ScatterPlotItem, mkBrush

from const import MAX_BACTERIA_SENSE, MAX_BACTERIA_SPEED
from helpers.color import get_bacteria_color
from models.bacteria import Bacteria
from ui.graphs.abstract_graph import AbstractGraph

GRAPH_COLOR = "#39FF14"
DOT_SIZE_FACTOR = 8


class StatsScatterGraph(AbstractGraph):
    def create_graph(self) -> PlotWidget:
        self.stats_graph = PlotWidget()
        self.stats_graph.setTitle('Stats Scatter')
        self.stats_graph.setLabel('left', 'Speed')
        self.stats_graph.setLabel('bottom', 'Sense')
        self.plot = self.stats_graph.plot()
        self.scatter_plot = ScatterPlotItem()
        self.stats_graph.addItem(self.scatter_plot)
        self.plot.setPen(GRAPH_COLOR)

        self.stats_graph.setYRange(0, MAX_BACTERIA_SPEED)
        self.stats_graph.setXRange(0, MAX_BACTERIA_SENSE)

        return self.stats_graph

    def update_data(self):
        last_turn = self.history.turns[-1]
        bacterias = [bacteria for bacteria, _ in last_turn.bacterias]

        spots = []

        def reduce_stats(stats_bacterias_dict: dict[tuple[int, int], int], bacteria: Bacteria) -> dict:
            stats_bacterias_dict[(bacteria.properties.sense,
                                  bacteria.properties.speed)] += 1
            return stats_bacterias_dict

        stats_bacterias = functools.reduce(
            reduce_stats, bacterias, defaultdict(int))

        for stats, amount in stats_bacterias.items():
            spot_dic = {'pos': (stats), 'size': DOT_SIZE_FACTOR*(amount**0.5),
                        'brush': get_bacteria_color(stats[1], stats[0])}
            spots.append(spot_dic)

        def tooltip(x, y, data):
            return f"""Sense: {int(x)}, Speed: {int(y)} amount: {data[(x, y)]}"""

        self.scatter_plot.setData(spots,
                                  data=stats_bacterias,
                                  hoverable=True,
                                  hoverPen='r',
                                  tip=tooltip,
                                  )
