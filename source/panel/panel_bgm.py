import wx
from source.sounddata_bgm import SoundDataBGM


class PanelBGM(wx.Panel):

    WIDTH = 974
    HEIGHT = 435
    HEIGHT_SOUNDDATA = 72
    CATEGORY = 'bgm.'

    def __init__(self, soundwindow):
        wx.Panel.__init__(self, soundwindow, pos=(10, 45),
                          size=(self.WIDTH, self.HEIGHT))

        self.soundwindow = soundwindow
        self.list_sounddata = []

        self.scrolledwindow = wx.ScrolledWindow(
            self, -1, style=wx.HSCROLL | wx.VERTICAL, pos=(0, 0), size=(self.WIDTH, self.HEIGHT))
        sounddata = SoundDataBGM(
            self.scrolledwindow, self, self.CATEGORY + '1', (0, 0))
        self.list_sounddata.append(sounddata)

    def create_sounddata(self, title, resourcepath):

        first_resourcepath = self.list_sounddata[0].get_sourcepath()

        if first_resourcepath == '':
            self.list_sounddata[0].Destroy()
            self.list_sounddata = []

        count = len(self.list_sounddata)
        pos_sounddata = (0, self.HEIGHT_SOUNDDATA * count)
        sounddata = SoundDataBGM(
            self.scrolledwindow, self, title, pos_sounddata)
        self.list_sounddata.append(sounddata)
        totalheight = self.HEIGHT_SOUNDDATA * (count + 1)
        self.scrolledwindow.SetScrollbars(
            0, self.HEIGHT_SOUNDDATA, 0, int(totalheight / self.HEIGHT_SOUNDDATA))
        self._switch_plusbutton()
        sounddata.set_sourcepath(resourcepath)

    def get_newsourcelist(self):
        new_sourcelist = []
        for sounddata in self.list_sounddata:
            source, title = sounddata.get_source_and_title()
            if source != '':
                new_sourcelist.append([source, title])

        return new_sourcelist

    def get_sounddatalist(self):
        return self.list_sounddata

    def switch_viewermode(self):
        for sounddata in self.list_sounddata:
            sounddata.switch_viewermode()

    def set_sourcepathlist(self, pathlist):
        for path, sounddata in zip(pathlist, self.list_sounddata):
            sounddata.set_sourcepath(path)

    def add_sounddata(self):

        list_sounddata_source_and_title = []
        new_list_sounddata = []

        for sounddata_ in self.list_sounddata:
            list_sounddata_source_and_title.append(
                sounddata_.get_source_and_title())

        new_title = self.CATEGORY + str(self._get_maxindex() + 1)
        list_sounddata_source_and_title.append(('', new_title))

        self.scrolledwindow.Destroy()
        self.scrolledwindow = wx.ScrolledWindow(self, -1, style=wx.HSCROLL | wx.VERTICAL, pos=(0, 0),
                                                size=(self.WIDTH, self.HEIGHT))

        pos_sounddata = (0, 0)
        for source, title in list_sounddata_source_and_title:
            sounddata = SoundDataBGM(
                self.scrolledwindow, self, title, pos_sounddata)
            sounddata.set_sourcepath(source)
            new_list_sounddata.append(sounddata)
            pos_sounddata = (0, pos_sounddata[1] + self.HEIGHT_SOUNDDATA)

        count = len(new_list_sounddata)
        totalheight = self.HEIGHT_SOUNDDATA * count
        self.scrolledwindow.SetScrollbars(
            0, self.HEIGHT_SOUNDDATA, 0, int(totalheight / self.HEIGHT_SOUNDDATA))

        self.list_sounddata.clear()
        self.list_sounddata = new_list_sounddata
        self._switch_plusbutton()
        self.scrolledwindow.Scroll(
            0, self.scrolledwindow.GetVirtualSize().GetHeight())

    def delete_sounddata(self, sounddata):

        if len(self.list_sounddata) == 1:
            sounddata = SoundDataBGM(
                self.scrolledwindow, self, self.CATEGORY + '1', (0, 0))
            self.list_sounddata.clear()
            self.list_sounddata.append(sounddata)
        else:
            for sounddata_ in self.list_sounddata:
                if sounddata_ is sounddata:
                    self.list_sounddata.remove(sounddata)
                    break

        self.scrolledwindow.Destroy()
        self.scrolledwindow = wx.ScrolledWindow(
            self, -1, style=wx.HSCROLL | wx.VERTICAL, pos=(0, 0), size=(self.WIDTH, self.HEIGHT))
        i = 0
        list_sounddata_ = []

        for sounddata_ in self.list_sounddata:
            title = sounddata_.get_title()
            sourcepath = sounddata_.get_sourcepath()
            pos_sounddata = (0, self.HEIGHT_SOUNDDATA * i)
            sounddata = SoundDataBGM(
                self.scrolledwindow, self, title, pos_sounddata)
            sounddata.set_sourcepath(sourcepath)
            list_sounddata_.append(sounddata)
            i = i + 1

        count = len(list_sounddata_)
        totalheight = self.HEIGHT_SOUNDDATA * count
        self.scrolledwindow.SetScrollbars(
            0, self.HEIGHT_SOUNDDATA, 0, int(totalheight / self.HEIGHT_SOUNDDATA))
        self.list_sounddata = list_sounddata_
        self._switch_plusbutton()

    def _get_index(self, title):
        index = title.replace(self.CATEGORY, '')
        if self._check_int(index):
            return int(index)
        else:
            return None

    def _check_int(self, s):
        try:
            int(s)
            return True
        except ValueError:
            return False

    def _switch_plusbutton(self):
        for sounddata in self.list_sounddata:
            sounddata.hide_addbutton()
        self.list_sounddata[-1].show_addbutton()

    def check_duplicatetitle(self, newtitle):
        for sounddata in self.list_sounddata:
            category, nowtitle = sounddata.get_title().split('.')
            if nowtitle == newtitle:
                return False
        return True

    def _get_maxindex(self):
        maxindex = 0
        for sounddata in self.list_sounddata:
            category, index = sounddata.get_title().split('.')
            if self._check_int(index):
                index_ = int(index)
                if maxindex < index_:
                    maxindex = index_
        return maxindex
