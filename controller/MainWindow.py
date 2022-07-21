from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5.QtGui import QPixmap, QKeySequence
from PyQt5.QtWidgets import QMainWindow, QShortcut, QMessageBox
from system_hotkey import SystemHotkey

from controller.CaptureScreen import CaptureScreenWindow
from view import UI_MainWindow


class MainWindow(QMainWindow, UI_MainWindow.Ui_MainWindow):
    sig_keyhot = pyqtSignal(str)

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.screenWindow = CaptureScreenWindow()
        self.screenWindow._signal[QPixmap].connect(self.handle_capture_picture)
        # 2. 设置我们的自定义热键响应函数
        self.sig_keyhot[str].connect(self.MKey_pressEvent)
        # 3. 初始化两个热键
        self.hk_start, self.hk_stop = SystemHotkey(), SystemHotkey()
        # 4. 绑定快捷键和对应的信号发送函数
        self.hk_start.register(('control', '1'), callback=lambda x: self.send_key_event("capture_start"))
        self.hk_stop.register(('control', '2'), callback=lambda x: self.send_key_event("None"))

        self.setupUi(self)

    @pyqtSlot()
    def capture_btn_clicked(self):
        self.screenWindow.show()

    @pyqtSlot(QPixmap)
    def handle_capture_picture(self, img):
        print("获取到图片", img)
        self.img_raw = img
        local_img = QPixmap(img).scaled(self.picture_label.width(), self.picture_label.height())
        # self.picture_label.setScaledContents(True)
        self.picture_label.setPixmap(local_img)

    # 热键处理函数
    @pyqtSlot(str)
    def MKey_pressEvent(self, i_str):
        if i_str == 'capture_start':
            self.screenWindow.show()
        elif i_str == 'None':
            QMessageBox.information(self, '温馨提示', '其他功能请等待后续添加哦')

    # 热键信号发送函数(将外部信号，转化成qt信号)
    def send_key_event(self, i_str):
        self.sig_keyhot[str].emit(i_str)
