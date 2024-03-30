from PyQt5.QtWidgets import QMainWindow, QStackedWidget
from helpers.color import get_bacteria_color
from logic.bacteria_creator import get_random_bacteria
from logic.game_runner import GameRunner
from logic.history_runner import HistoryRunner
from logic.history_saver import HistorySaver
from ui.pages.graph_page import GraphPage
from ui.pages.simulation_page import SimulationPage
from ui.ui_utils import create_colored_icon

CSS_FILE = "main_window.css"

class MainWindow(QMainWindow):
    """
    The main window of the Bacteria Game application.

    This class represents the main window of the Bacteria Game application.
    It contains a stacked widget that displays the simulation page and the graph page.
    The user can switch between these pages using the navigation buttons.

    Attributes:
        simulation_page (SimulationPage): The simulation page widget.
        graph_page (GraphPage): The graph page widget.
        stackedWidget (QStackedWidget): The stacked widget that holds the pages.

    Methods:
        go_to_simulation_page: Switches to the simulation page.
        go_to_graph_page: Switches to the graph page.
        initUI: Initializes the user interface of the main window.
        __set_icon: Sets the window icon based on a random bacteria.

    """

    def __init__(self) -> None:
        super().__init__()
        self.initUI()
        history_saver = HistorySaver()
        game = GameRunner(history_runner=HistoryRunner(history_saver))
        self.simulation_page = SimulationPage(
            self.go_to_graph_page, history_saver, game)
        self.graph_page = GraphPage(
            self.go_to_simulation_page, history_saver, game)
        self.stackedWidget = QStackedWidget()
        self.setCentralWidget(self.stackedWidget)
        self.stackedWidget.addWidget(self.simulation_page)
        self.stackedWidget.addWidget(self.graph_page)

    def go_to_simulation_page(self) -> None:
        """
        Switches to the simulation page.

        This method is called when the user wants to switch to the simulation page.
        It sets the current index of the stacked widget to 0, which displays the simulation page.

        Returns:
            None
        """
        self.stackedWidget.setCurrentIndex(0)

    def go_to_graph_page(self) -> None:
        """
        Switches to the graph page.

        This method is called when the user wants to switch to the graph page.
        It sets the current index of the stacked widget to 1, which displays the graph page.
        It also calls the `on_page_set` method of the graph page to update its content.

        Returns:
            None
        """
        self.stackedWidget.setCurrentIndex(1)
        self.graph_page.on_page_set()

    def initUI(self) -> None:
        """
        Initializes the user interface of the main window.

        This method sets the window title and calls the `__set_icon` method to set the window icon.

        Returns:
            None
        """
        super().__init__()
        self.setWindowTitle("Bacteria Life")
        self.__set_icon()

    def __set_icon(self) -> None:
        """
        Sets the window icon based on a random bacteria.

        This method generates a random bacteria and retrieves its color.
        It then sets the window icon using the `create_colored_icon` function from the `ui_utils` module.

        Returns:
            None
        """
        random_bacteria = get_random_bacteria()
        color = get_bacteria_color(random_bacteria.properties)
        self.setWindowIcon(create_colored_icon("assets/bacteria.svg", color))
