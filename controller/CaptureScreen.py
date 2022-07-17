from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QPixmap
from view.UI_CaptureScreen import CaptureScreen


class CaptureScreenWindow(CaptureScreen):
    # _signal = pyqtSignal(QPixmap)
    _signal = pyqtSignal(QPixmap)

    def __init__(self):
        super().__init__()

    def save_image(self):
        # print(self.capture_image)
        # self._signal.emit(self.capture_image)
        self._signal[QPixmap].emit(self.capture_image)
        # self.capture_image.save('picture.png', quality=95)  # 保存图片到当前文件夹中
