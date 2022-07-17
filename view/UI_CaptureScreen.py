import win32clipboard as w
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt, qAbs, QRect
from PyQt5.QtGui import QPen, QPainter, QColor, QGuiApplication

'''
代码来自：@Karbob
'''


class CaptureScreen(QWidget):
    # 初始化变量
    begin_position = None
    end_position = None
    full_screen_image = None
    capture_image = None
    is_mouse_pressLeft = None
    painter = QPainter()

    def __init__(self):
        super(QWidget, self).__init__()
        self.init_window()  # 初始化窗口
        self.capture_full_screen()  # 获取全屏

    def init_window(self):
        self.setMouseTracking(True)  # 鼠标追踪
        self.setCursor(Qt.CrossCursor)  # 设置光标
        self.setWindowFlag(Qt.FramelessWindowHint)  # 窗口无边框
        self.setWindowState(Qt.WindowFullScreen)  # 窗口全屏

    def capture_full_screen(self):
        self.full_screen_image = QGuiApplication.primaryScreen().grabWindow(QApplication.desktop().winId())

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.begin_position = event.pos()
            self.is_mouse_pressLeft = True
        if event.button() == Qt.RightButton:
            # 如果选取了图片,则按一次右键开始重新截图
            if self.capture_image is not None:
                self.capture_image = None
                self.paint_background_image()
                self.update()
            else:
                self.close()

    def mouseMoveEvent(self, event):
        if self.is_mouse_pressLeft is True:
            self.end_position = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        self.end_position = event.pos()
        self.is_mouse_pressLeft = False

    def mouseDoubleClickEvent(self, event):
        if self.capture_image is not None:
            self.save_image()
            self.close()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            if self.capture_image is not None:
                self.save_image()
                self.close()

    def paint_background_image(self):
        shadow_color = QColor(0, 0, 0, 100)  # 黑色半透明
        self.painter.drawPixmap(0, 0, self.full_screen_image)
        self.painter.fillRect(self.full_screen_image.rect(), shadow_color)  # 填充矩形阴影

    def paintEvent(self, event):
        self.painter.begin(self)  # 开始重绘
        self.paint_background_image()
        pen_color = QColor(30, 144, 245)  # 画笔颜色
        self.painter.setPen(QPen(pen_color, 1, Qt.SolidLine, Qt.RoundCap))  # 设置画笔,蓝色,1px大小,实线,圆形笔帽
        if self.is_mouse_pressLeft is True:
            pick_rect = self.get_rectangle(self.begin_position, self.end_position)  # 获得要截图的矩形框
            self.capture_image = self.full_screen_image.copy(pick_rect)  # 捕获截图矩形框内的图片
            self.painter.drawPixmap(pick_rect.topLeft(), self.capture_image)  # 填充截图的图片
            self.painter.drawRect(pick_rect)  # 画矩形边框
        self.painter.end()  # 结束重绘

    def get_rectangle(self, begin_point, end_point):
        pick_rect_width = int(qAbs(begin_point.x() - end_point.x()))
        pick_rect_height = int(qAbs(begin_point.y() - end_point.y()))
        pick_rect_top = begin_point.x() if begin_point.x() < end_point.x() else end_point.x()
        pick_rect_left = begin_point.y() if begin_point.y() < end_point.y() else end_point.y()
        pick_rect = QRect(pick_rect_top, pick_rect_left, pick_rect_width, pick_rect_height)
        # 避免高度宽度为0时候报错
        if pick_rect_width == 0:
            pick_rect.setWidth(2)
        if pick_rect_height == 0:
            pick_rect.setHeight(2)

        return pick_rect

    def save_image(self):
        self.capture_image.save('picture.png', quality=95)  # 保存图片到当前文件夹中
