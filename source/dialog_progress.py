import threading
import time
import wx
import os


class ProgressDialog(wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(
            self, parent, -1, 'progress message', size=(500, 100))

        self.SetBackgroundColour(wx.WHITE)
        self.base = wx.Panel(self)
        self.message = wx.StaticText(self.base, -1, '', pos=(20, 10))

    def update_message(self, filepath):
        filename = os.path.basename(filepath)
        message = filename + ' を .ogg形式に変換しています...'
        self.message.SetLabel(message)
        self.Update()

    def start(self):
        self.Show()

    def close(self):
        self.flag_bar = False
        self.Close()
