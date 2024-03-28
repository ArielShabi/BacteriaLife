from typing import Any, Callable
from PyQt5.QtWidgets import QSlider


class UnevenStepSlider(QSlider):
    """
    A custom slider widget that allows uneven steps between minimum and maximum values.

    Args:
        *args: Variable length argument list.
        **kwargs: Arbitrary keyword arguments.

    Attributes:
        _steps (list[float]): A list of float values representing the uneven steps.

    """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """
        Initializes the UnevenStepSlider.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        """
        super().__init__(*args, **kwargs)
        self._steps: list[float] = []

    def setSteps(self, steps: list[float]) -> None:
        """
        Sets the uneven steps for the slider.

        Args:
            steps (list[float]): A list of float values representing the uneven steps.

        Returns:
            None

        """
        self._steps = sorted(steps)
        self.setMinimum(0)
        self.setMaximum(len(steps)-1)

    def on_value_changed(self, function_to_call: Callable[[float], None]) -> None:
        """
        Connects a function to the valueChanged signal of the slider.

        Args:
            function_to_call (Callable[[float], None]): A function that takes a float value as input.

        Returns:
            None

        """
        def wrapper(pos: int) -> None:
            value = self._steps[pos]
            function_to_call(value)

        self.valueChanged.connect(wrapper)
