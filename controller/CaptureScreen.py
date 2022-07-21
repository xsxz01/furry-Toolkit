from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QPixmap
from view.UI_CaptureScreen import CaptureScreen


class CaptureScreenWindow(CaptureScreen):
    _signal = pyqtSignal(QPixmap)

    def __init__(self):
        super().__init__()

    def save_image(self):
        self._signal[QPixmap].emit(self.capture_image)
