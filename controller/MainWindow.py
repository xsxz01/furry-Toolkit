from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow

from controller.CaptureScreen import CaptureScreen
from view import UI_MainWindow


class MainWindow(QMainWindow, UI_MainWindow.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

    @pyqtSlot()
    def capture_btn_clicked(self):
        print('按钮被点击')
        self.screenWindow = CaptureScreen()
        self.screenWindow.show()