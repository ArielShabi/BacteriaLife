from PyQt5.QtWidgets import QSlider


class UnevenStepSlider(QSlider):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._steps = []

    def setSteps(self, steps):
        self._steps = sorted(steps)
        self.setMinimum(0)
        self.setMaximum(len(steps)-1)

    def onValueChanged(self, function_to_call: callable):
        def wrapper(pos: int):
            value = self._steps[pos]
            function_to_call(value)

        self.valueChanged.connect(wrapper)

    # def value(self):
    #     return self._steps[super().value()]

    # def setValue(self, val: int):
    #     value = super().value()
    #     if value in self._steps:
    #         return value
    #     for i, step in enumerate(self._steps[:-1]):
    #         if step < value < self._steps[i+1]:
    #             return self._steps[i]
    #     return self._steps[-1]
