"""
This stub file is to aid in the PyCharm auto-completion of the Qt imports.
"""

from typing import Any, Union

from PyQt5 import QtCore, QtGui, QtSvg, QtTest, QtWidgets

App: QtWidgets.QApplication
VERSION_INFO: str
QT_LIB: str
QtVersion: str
def exec_() -> QtWidgets.QApplication: ...
def mkQApp(name: Union[str, None] = None) -> QtWidgets.QApplication: ...
def isQObjectAlive(obj: QtCore.QObject) -> bool: ...


class GraphicsView(QtWidgets.QGraphicsView):
    ...


class PlotWidget(GraphicsView):
    ...
    
class GraphicsItem(object):
    ...

class GraphicsObject(GraphicsItem, QtWidgets.QGraphicsObject):
    ...

class ScatterPlotItem(GraphicsObject):
    def setData(self, *args: Any, **kwargs: Any) -> None:
        ...
    ...