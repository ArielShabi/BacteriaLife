import pyqtgraph as pg
from PyQt5.QtGui import QColor

from const import MAX_BACTERIA_SENSE, MAX_BACTERIA_SPEED
from models.board_data import BoardData
from ui.graphs.abstract_graph import AbstractGraph

SPEED_COLOR = "#FF0033"
SENSE_COLOR = "#1E90FF"


class AverageStatsGraph(AbstractGraph):
    def create_graph(self) -> pg.PlotWidget:
        self.average_stats_graph = pg.PlotWidget()
        self.average_stats_graph.setTitle('Average stats vs Time')
        self.average_stats_graph.setLabel('left', 'Average stats')
        self.average_stats_graph.setLabel('bottom', 'Time (turns)')

        self.speed_plot = self.average_stats_graph.plot(name='Avg Speed')
        self.speed_plot.setPen(SPEED_COLOR)
        self.sense_plot = self.average_stats_graph.plot(name='Avg Sense')
        self.sense_plot.setPen(SENSE_COLOR)

        self.average_stats_graph.setYRange(
            0, max(MAX_BACTERIA_SPEED, MAX_BACTERIA_SENSE))

        return self.average_stats_graph

    def update_data(self):
        turns = self.history.turns

        average_speed, average_sense = zip(*[
            self.__get_turn_average_stats(turn) for turn in turns
        ])

        self.average_stats_graph.setXRange(1, len(turns))

        self.speed_plot.setData(list(range(len(turns))), average_speed)
        self.sense_plot.setData(list(range(len(turns))), average_sense)

    def __get_turn_average_stats(self, turn: BoardData) -> tuple[float, float]:
        speed = 0
        sense = 0

        if not turn.bacterias:
            return 0, 0

        for bacteria, _ in turn.bacterias:
            speed += bacteria.properties.speed
            sense += bacteria.properties.sense

        speed /= len(turn.bacterias)
        sense /= len(turn.bacterias)
        return speed, sense
