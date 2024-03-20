from typing import Callable
from PyQt5.QtWidgets import QSlider


class UnevenStepSlider(QSlider):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._steps = []

    def setSteps(self, steps):
        self._steps = sorted(steps)
        self.setMinimum(0)
        self.setMaximum(len(steps)-1)

    def on_value_changed(self, function_to_call: Callable[[int], None]):
        def wrapper(pos: int):
            value = self._steps[pos]
            function_to_call(value)

        self.valueChanged.connect(wrapper)
