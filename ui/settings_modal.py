from typing import Optional
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QGridLayout, QSpinBox, QCheckBox, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QShowEvent

from models.settings import Settings

MAX_SLIDER_VALUE = 10
SLIDER_SIZE = 150
SETTINGS_MODAL_MIN_WIDTH = 300


class SettingsModal(QDialog):
    """
    A dialog window for configuring settings.

    Args:
        settings (Settings): The current settings object.

    Attributes:
        settings (Settings): The current settings object.
        board_width (QSpinBox): The spin box for selecting the board width.
        board_height (QSpinBox): The spin box for selecting the board height.
        grid_layout (QGridLayout): The grid layout for organizing the widgets.
        magic_door_check_box (QCheckBox): The check box for enabling/disabling the magic door.
        portal_from_x (QSpinBox): The spin box for selecting the x-coordinate of the portal's starting point.
        portal_from_y (QSpinBox): The spin box for selecting the y-coordinate of the portal's starting point.
        portal_to_x (QSpinBox): The spin box for selecting the x-coordinate of the portal's destination.
        portal_to_y (QSpinBox): The spin box for selecting the y-coordinate of the portal's destination.
        portal_inputs_container (QWidget): The container widget for the portal input fields.

    """

    def __init__(self, settings: Settings) -> None:
        """
        Initializes the SettingsModal.

        Args:
            settings (Settings): The current settings object.

        """
        super().__init__()
        self.settings = settings
        self.setWindowTitle("Settings")
        
        self.setMinimumWidth(SETTINGS_MODAL_MIN_WIDTH)
        self.setWindowIcon(QIcon("assets/cog.svg"))
        self.initUI()

    def initUI(self) -> None:
        """
        Initializes the user interface of the SettingsModal.

        """
        layout = QVBoxLayout()
        grid_layout = QGridLayout()

        header_label = QLabel("Choose your settings:")
        layout.addWidget(header_label, alignment=Qt.AlignmentFlag.AlignCenter)

        self.board_width = QSpinBox()
        self.board_width.setMinimum(0)
        self.board_width.setMaximum(1000)
        self.board_width.valueChanged.connect(self.__on_board_width_change)
        board_size_label = QLabel("x")

        self.board_height = QSpinBox()
        self.board_height.setMinimum(0)
        self.board_height.setMaximum(1000)
        self.board_height.valueChanged.connect(self.__on_board_height_change)

        grid_layout.addWidget(QLabel("Board Size:"), 0, 0)
        grid_layout.addWidget(self.board_width, 0, 1)
        grid_layout.addWidget(board_size_label, 0, 2)
        grid_layout.addWidget(self.board_height, 0, 3)

        self.grid_layout = grid_layout

        self.__init_portal()

        ok_button = QPushButton("Save")
        ok_button.clicked.connect(self.accept)

        layout.addLayout(grid_layout)
        layout.addWidget(ok_button)

        self.setLayout(layout)

    def accept(self) -> None:
        """
        Accepts the settings and closes the dialog.

        """
        self.settings.board_size = (
            self.board_width.value(), self.board_height.value())
        if (not self.__is_magic_door_valid()):
            self.settings.magic_door = None
        else:
            self.settings.magic_door = (
                (self.portal_from_x.value(), self.portal_from_y.value()),
                (self.portal_to_x.value(), self.portal_to_y.value())
            )

        super().accept()

    def showEvent(self, event: Optional[QShowEvent]) -> None:
        """
        Overrides the showEvent method to update the UI with the current settings.

        Args:
            event (QShowEvent): The show event.

        """
        super().showEvent(event)
        self.board_width.setValue(self.settings.board_size[0])
        self.board_height.setValue(self.settings.board_size[1])

        if (self.settings.magic_door):
            self.magic_door_check_box.setChecked(True)
            self.portal_from_x.setValue(self.settings.magic_door[0][0])
            self.portal_from_y.setValue(self.settings.magic_door[0][1])
            self.portal_to_x.setValue(self.settings.magic_door[1][0])
            self.portal_to_y.setValue(self.settings.magic_door[1][1])
        else:
            self.magic_door_check_box.setChecked(False)

    def __init_portal(self) -> None:
        """
        Initializes the magic door input fields.

        """
        self.magic_door_check_box = QCheckBox()
        self.magic_door_check_box.stateChanged.connect(
            self.__on_portal_checkbox_change)

        self.grid_layout.addWidget(QLabel("Magic door:"), 1, 0)
        self.grid_layout.addWidget(self.magic_door_check_box, 1, 1)

        self.portal_from_x = QSpinBox()
        self.portal_from_x.setMinimum(0)

        self.portal_from_y = QSpinBox()
        self.portal_from_y.setMinimum(0)

        self.portal_to_x = QSpinBox()
        self.portal_to_x.setMinimum(0)

        self.portal_to_y = QSpinBox()
        self.portal_to_y.setMinimum(0)

        self.portal_inputs_layout = QGridLayout()

        self.portal_inputs_layout.addWidget(QLabel("Portal from:"), 0, 0)
        self.portal_inputs_layout.addWidget(self.portal_from_x, 0, 1)
        self.portal_inputs_layout.addWidget(QLabel("x"), 0, 2)
        self.portal_inputs_layout.addWidget(self.portal_from_y, 0, 3)

        self.portal_inputs_layout.addWidget(QLabel("Portal to:"), 1, 0)
        self.portal_inputs_layout.addWidget(self.portal_to_x, 1, 1)
        self.portal_inputs_layout.addWidget(QLabel("x"), 1, 2)
        self.portal_inputs_layout.addWidget(self.portal_to_y, 1, 3)

        self.portal_inputs_container = QWidget()
        self.portal_inputs_container.setLayout(self.portal_inputs_layout)

        self.portal_inputs_container.setVisible(False)

        self.grid_layout.addWidget(self.portal_inputs_container, 2, 0, 1, 4)

    def __on_portal_checkbox_change(self) -> None:
        """
        Handles the change event of the magic door check box.

        """
        if self.magic_door_check_box.isChecked():
            self.portal_inputs_container.setVisible(True)
        else:
            self.portal_inputs_container.setVisible(False)
            # Weird PyQt bug, the layout doesn't update properly
            self.adjustSize()
            self.adjustSize()

    def __is_magic_door_valid(self) -> bool:
        """
        Checks if the magic door input values are valid.

        Returns:
            bool: True if the magic door is valid, False otherwise.

        """
        if (self.magic_door_check_box.isChecked()):
            return (self.portal_from_x.value() != self.portal_to_x.value() or self.portal_from_y.value() != self.portal_to_y.value())
        return False

    def __on_board_width_change(self) -> None:
        """
        Updates the maximum values of the portal input fields based on the board width.

        """
        self.portal_from_x.setMaximum(self.board_width.value())
        self.portal_to_x.setMaximum(self.board_width.value())

    def __on_board_height_change(self) -> None:
        """
        Updates the maximum values of the portal input fields based on the board height.

        """
        self.portal_from_y.setMaximum(self.board_height.value())
        self.portal_to_y.setMaximum(self.board_height.value())
