import wx
from PIL import ImageGrab


class ScreenShot(wx.Frame):
    left, right, top, bottom = 0, 0, 0, 0
    img = None

    def __init__(self, parent):
        wx.Frame.__init__(self, parent,
                          style=wx.MAXIMIZE  # 全屏显示
                          )
        # 设置背景色
        self.SetBackgroundColour((255, 0, 0))
        # 设置透明度
        self.SetTransparent(30)
        # 注册事件
        self.Bind(wx.EVT_LEFT_DOWN, self.OnDown, self)
        self.Bind(wx.EVT_LEFT_UP, self.OnUp, self)
        # 显示button
        self.Show(True)

    def OnDown(self, event):
        pos = event.GetPosition()
        self.top = pos.y
        self.left = pos.x

    def OnUp(self, event):
        pos = event.GetPosition()
        self.bottom = pos.y
        self.right = pos.x

        print(self.left, self.top, self.right, self.bottom)
        self.img = self.catch_area(
            self.left, self.top, self.right, self.bottom)

        # 截图完毕后关闭button
        self.Close(False)

    def catch_area(self, left, top, right, bottom):
        return ImageGrab.grab((left, top, right, bottom))

# 测试用例
app = wx.App(False)
frame = ScreenShot(None)
app.MainLoop()
