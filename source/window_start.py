import getpass
import subprocess
import webbrowser

import wx
from source.database_helper import DatabaseHelper
from source.panel.panel_packdata import PackdataPanel
from source.window_sound import SoundWindow
from source.config_manager import ConfigManager


class StartWindow(wx.Frame):

    WIDTH = 1000
    HEIGHT = 550

    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Minecraft SoundReplacer v0.7.1b', size=(self.WIDTH, self.HEIGHT))

        self.SetBackgroundColour(wx.WHITE)
        icon = wx.Icon('./image/icon_frame.ico')
        self.SetIcon(icon)
        self.soundwindow = None
        self.inputwindow = None
        self.packdatapanel = None

        self.button_new = wx.BitmapButton(self, -1, wx.Bitmap('./image/button_plus.png'), pos=(30, 15), size=(16, 16))
        self.button_new.SetBitmapPressed(wx.Bitmap('./image/button_plus_on.png'))
        self.button_new.SetBitmapCurrent(wx.Bitmap('./image/button_plus_hover.png'))
        self.button_new.SetToolTip('新しいリソースパックを追加')
        self.button_new.Bind(wx.EVT_BUTTON, self.click_new)

        self.button_folder_JE = wx.BitmapButton(self, -1, wx.Bitmap('./image/button_folder.png'), pos=(70, 15), size=(16, 16))
        self.button_folder_JE.SetBitmapPressed(wx.Bitmap('./image/button_folder_on.png'))
        self.button_folder_JE.SetBitmapCurrent(wx.Bitmap('./image/button_folder_hover.png'))
        self.button_folder_JE.SetToolTip('Minecraft JE - .minecraft / resourcepacks')
        self.button_folder_JE.Bind(wx.EVT_BUTTON, self.click_folder_JE)

        self.button_folder_BE = wx.BitmapButton(self, -1, wx.Bitmap('./image/button_folder.png'), pos=(110, 15), size=(16, 16))
        self.button_folder_BE.SetBitmapPressed(wx.Bitmap('./image/button_folder_on.png'))
        self.button_folder_BE.SetBitmapCurrent(wx.Bitmap('./image/button_folder_hover.png'))
        self.button_folder_BE.SetToolTip('Minecraft BE - com.mojang / resource_packs')
        self.button_folder_BE.Bind(wx.EVT_BUTTON, self.click_folder_BE)

        self.button_support = wx.BitmapButton(self, -1, wx.Bitmap('./image/button_door.png'), pos=(910, 15), size=(16, 16))
        self.button_support.SetBitmapPressed(wx.Bitmap('./image/button_door_on.png'))
        self.button_support.SetBitmapFocus(wx.Bitmap('./image/button_door_hover.png'))
        self.button_support.SetToolTip('ウェブサイト：https://sites.google.com/view/kusunoki-games/minecraft-soundreplacer')
        self.button_support.Bind(wx.EVT_BUTTON, self.click_website)

        packdatalist = DatabaseHelper().get_packdatalist()
        self.packdatapanel = PackdataPanel(self, packdatalist)

    def click_new(self, event):
        self.destroy_soundwindow()
        self.soundwindow = SoundWindow(self)
        self.soundwindow.Show()

    def click_folder_BE(self, event):
        username = getpass.getuser()
        path = '"C:\\Users\\' + username + '\\AppData\\Local\\Packages\\Microsoft.MinecraftUWP_8wekyb3d8bbwe\\LocalState\\games\\com.mojang\\resource_packs"'
        subprocess.run('explorer {}'.format(path))

    def click_folder_JE(self, event):
        username = getpass.getuser()
        path = '"C:\\Users\\' + username + '\\AppData\\Roaming\\.minecraft\\resourcepacks"'
        subprocess.run('explorer {}'.format(path))

    def click_website(self, event):
        webbrowser.open('https://sites.google.com/view/kusunoki-games/minecraft-soundreplacer')


    def get_soundwindow(self):
        return self.soundwindow

    def destroy_soundwindow(self):
        if type(self.soundwindow) == SoundWindow:
            self.soundwindow.Destroy()
            self.soundwindow = None

    def show_soundwindow(self, data_for_soundwindow, data_for_panelinput=None):
        self.soundwindow = SoundWindow(self, data_for_soundwindow, data_for_panelinput)
        self.soundwindow.Show()

    '''
    def show_soundwindow_viewermode(self, data_for_soundwindow):
        self.soundwindow = SoundWindow(self, data_for_soundwindow)
        self.soundwindow.Show()
        self.soundwindow.switch_viewermode()
    '''

    def updatelist(self):
        self.packdatapanel.Hide()
        self.RemoveChild(self.packdatapanel)
        packdatalist = DatabaseHelper().get_packdatalist()
        self.packdatapanel = PackdataPanel(self, packdatalist)

