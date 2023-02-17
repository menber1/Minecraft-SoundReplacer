import wx
from source.packdata import PackData


class PackdataPanel(wx.Panel):

    WIDTH = 977
    HEIGHT = 500
    HEIGHT_PACKDATA = 148

    def __init__(self, startwindow, packdatas):
        wx.Panel.__init__(self, startwindow, size=(self.WIDTH, self.HEIGHT))
        self.SetBackgroundColour(wx.WHITE)
        self.startwindow = startwindow
        self.list_packdata = []

        scrolledwindow = wx.ScrolledWindow(
            self, -1, style=wx.HSCROLL | wx.VERTICAL, pos=(15, 48), size=(self.WIDTH - 15, self.HEIGHT))
        i = 0

        for data in packdatas:
            pos_packdata = (0, self.HEIGHT_PACKDATA * i)
            packdata = PackData(
                scrolledwindow, self.startwindow, data, pos_packdata)
            self.list_packdata.append(packdata)
            i = i + 1

        count = len(self.list_packdata)
        totalheight = self.HEIGHT_PACKDATA * count

        scrolledwindow.SetScrollbars(0, self.HEIGHT_PACKDATA, 0, int(
            totalheight / self.HEIGHT_PACKDATA))
