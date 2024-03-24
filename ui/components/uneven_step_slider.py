from typing import Any, Callable
from PyQt5.QtWidgets import QSlider


class UnevenStepSlider(QSlider):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self._steps: list[float] = []

    def setSteps(self, steps: list[float]) -> None:
        self._steps = sorted(steps)
        self.setMinimum(0)
        self.setMaximum(len(steps)-1)

    def on_value_changed(self, function_to_call: Callable[[float], None]) -> None:
        def wrapper(pos: int) -> None:
            value = self._steps[pos]
            function_to_call(value)

        self.valueChanged.connect(wrapper)
