from PyQt5.QtWidgets import QMainWindow

from view.UI_CaptureScreen import CaptureScreen


class Generator(CaptureScreen, QMainWindow):
    def __init__(self):
        super(CaptureScreen, self).__init__()
        self.setupUi(self)