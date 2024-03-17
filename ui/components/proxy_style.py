from PyQt5.QtWidgets import QProxyStyle
from PyQt5.QtCore import Qt


class ProxyStyle(QProxyStyle):
    def styleHint(self, hint, opt=None, widget=None, returnData=None):
        res = super().styleHint(hint, opt, widget, returnData)
        if hint == self.SH_Slider_AbsoluteSetButtons:
            res |= Qt.LeftButton
        return res
