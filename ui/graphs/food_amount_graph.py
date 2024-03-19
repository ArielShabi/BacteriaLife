import pyqtgraph as pg

from ui.graphs.abstract_graph import AbstractGraph

GRAPH_COLOR = "#39FF14"


class FoodAmountGraph(AbstractGraph):
    def create_graph(self) -> pg.PlotWidget:
        self.food_amount_graph = pg.PlotWidget()
        self.food_amount_graph.setTitle('Food Amount vs Time')
        self.food_amount_graph.setLabel('left', 'Food amount')
        self.food_amount_graph.setLabel('bottom', 'Time (turns)')
        self.plot = self.food_amount_graph.plot()
        self.plot.setPen(GRAPH_COLOR)
        return self.food_amount_graph

    def update_data(self):
        turns = self.history.turns

        if len(turns) == 0:
            return

        food_amount = [len(turn.foods) for turn in turns]

        self.food_amount_graph.setXRange(1, len(turns))
        self.food_amount_graph.setYRange(0, max(food_amount))

        self.plot.setData(list(range(len(turns))), food_amount)
