import wx
from source.sounddata import SoundData


class PanelSoundData(wx.Panel):

    WIDTH = 974
    HEIGHT = 435
    HEIGHT_SOUNDDATA = 72

    def __init__(self, soundwindow, path_oggfiles):
        wx.Panel.__init__(self, soundwindow, pos=(10, 45),
                          size=(self.WIDTH, self.HEIGHT))

        self.soundwindow = soundwindow
        self.list_sounddata = []

        scrolledwindow = wx.ScrolledWindow(
            self, -1, style=wx.HSCROLL | wx.VERTICAL, pos=(0, 0), size=(self.WIDTH, self.HEIGHT))
        i = 0

        for path_ogg in path_oggfiles:
            pos_sounddata = (0, self.HEIGHT_SOUNDDATA * i)
            sounddata = SoundData(scrolledwindow, self,
                                  path_ogg, pos_sounddata)
            self.list_sounddata.append(sounddata)
            i = i + 1

        count = len(self.list_sounddata)
        totalheight = self.HEIGHT_SOUNDDATA * count
        scrolledwindow.SetScrollbars(0, self.HEIGHT_SOUNDDATA, 0, int(
            totalheight / self.HEIGHT_SOUNDDATA))

    def get_newsourcelist(self):
        new_sourcelist = []
        for sounddata in self.list_sounddata:
            source, ogg = sounddata.get_source_and_ogg()
            if source != '':
                new_sourcelist.append([source, ogg])
        return new_sourcelist

    def get_sounddatalist(self):
        return self.list_sounddata

    def switch_viewermode(self):
        for sounddata in self.list_sounddata:
            sounddata.switch_viewermode()

    def get_pngfilepath(self, path_ogg=None):
        pass

    def set_sourcepathlist(self, pathlist):
        for path, sounddata in zip(pathlist, self.list_sounddata):
            sounddata.set_sourcepath(path)
