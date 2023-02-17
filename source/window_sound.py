import os
import wx
from source.panel.panel_creative import PanelCreative
from source.panel.panel_end import PanelEnd
from source.panel.panel_game import PanelGame
from source.panel.panel_input import PanelInput
from source.panel.panel_menu import PanelMenu
from source.panel.panel_nether import PanelNether
from source.panel.panel_note import PanelNote
from source.panel.panel_bgm import PanelBGM
from source.panel.panel_records import PanelRecords
from source.panel.panel_se import PanelSE
from source.panel.panel_water import PanelWater


class SoundWindow(wx.Frame):

    WIDTH = 1000
    HEIGHT = 525

    def __init__(self, startwindow, newsourcelist=None, data_for_panelinput=None):
        wx.Frame.__init__(
            self, startwindow, -1, 'Minecraft SoundReplacer - SoundList', size=(self.WIDTH, self.HEIGHT))

        self.Bind(wx.EVT_CLOSE, self.close_frame)

        self.SetBackgroundColour(wx.WHITE)
        icon = wx.Icon('./image/icon_frame.ico')
        self.SetIcon(icon)
        x, y = startwindow.GetPosition()
        self.SetPosition((x + 50, y + 50))
        self.startwindow = startwindow

        element_array = ('records', 'menu', 'game', 'creative', 'end',
                         'nether', 'water', 'note', 'bgm ( original )', 'se ( original )')
        self.combobox = wx.ComboBox(self, wx.ID_ANY, choices=element_array,
                                    style=wx.CB_DROPDOWN | wx.CB_READONLY, pos=(15, 10), size=(200, 25))
        self.combobox.Select(0)
        self.combobox.Bind(wx.EVT_COMBOBOX, self.select_combobox)

        self.button_next = wx.Button(
            self, -1, 'next', pos=(225, 10), size=(80, 25))
        self.button_next.Bind(wx.EVT_BUTTON, self.click_next)

        self.panel_records = PanelRecords(self)
        self.panel_menu = PanelMenu(self)
        self.panel_game = PanelGame(self)
        self.panel_creative = PanelCreative(self)
        self.panel_end = PanelEnd(self)
        self.panel_nether = PanelNether(self)
        self.panel_water = PanelWater(self)
        self.panel_note = PanelNote(self)
        self.panel_bgm = PanelBGM(self)
        self.panel_se = PanelSE(self)
        self.panel_input = PanelInput(self, data_for_panelinput)

        self.switch_panel(self.panel_records)

        if newsourcelist != None:
            self.newsourcelist_in_panel_sounddata(newsourcelist)

    def close_frame(self, event):
        self.startwindow.destroy_soundwindow()

    def select_combobox(self, event):

        self.button_next.Show()
        name = self.combobox.GetStringSelection()

        if name == 'records':
            self.switch_panel(self.panel_records)
        elif name == 'menu':
            self.switch_panel(self.panel_menu)
        elif name == 'game':
            self.switch_panel(self.panel_game)
        elif name == 'creative':
            self.switch_panel(self.panel_creative)
        elif name == 'end':
            self.switch_panel(self.panel_end)
        elif name == 'nether':
            self.switch_panel(self.panel_nether)
        elif name == 'water':
            self.switch_panel(self.panel_water)
        elif name == 'note':
            self.switch_panel(self.panel_note)
        elif name == 'bgm ( original )':
            self.switch_panel(self.panel_bgm)
        elif name == 'se ( original )':
            self.switch_panel(self.panel_se)

    def click_next(self, event):
        self.button_next.Hide()
        self.switch_panel(self.panel_input)

    def switch_panel(self, panel):
        self.panel_menu.Hide()
        self.panel_end.Hide()
        self.panel_game.Hide()
        self.panel_water.Hide()
        self.panel_nether.Hide()
        self.panel_creative.Hide()
        self.panel_records.Hide()
        self.panel_note.Hide()
        self.panel_input.Hide()
        self.panel_bgm.Hide()
        self.panel_se.Hide()
        panel.Show()
        self.Update()

    def get_size(self):
        return self.WIDTH, self.HEIGHT

    def get_newsourcelist(self):
        all = []
        all.extend(self.panel_records.get_newsourcelist())
        all.extend(self.panel_menu.get_newsourcelist())
        all.extend(self.panel_game.get_newsourcelist())
        all.extend(self.panel_creative.get_newsourcelist())
        all.extend(self.panel_end.get_newsourcelist())
        all.extend(self.panel_nether.get_newsourcelist())
        all.extend(self.panel_water.get_newsourcelist())
        all.extend(self.panel_note.get_newsourcelist())
        all.extend(self.panel_bgm.get_newsourcelist())
        all.extend(self.panel_se.get_newsourcelist())
        return all

    def newsourcelist_in_panel_sounddata(self, list_source_and_ogg):
        list_source_and_ogg_bgm = []
        list_source_and_ogg_se = []
        list_source_and_ogg_others = []

        for source, ogg in list_source_and_ogg:
            panel_sounddata = self._get_panelsounddata(ogg)

            if self.panel_bgm is panel_sounddata:
                list_source_and_ogg_bgm.append([source, ogg])
            elif self.panel_se is panel_sounddata:
                list_source_and_ogg_se.append([source, ogg])
            else:
                list_source_and_ogg_others.append([source, ogg])

        if list_source_and_ogg_bgm != []:
            _list_source_and_ogg_bgm = sorted(
                list_source_and_ogg_bgm, key=lambda x: x[1])
            for source, ogg in _list_source_and_ogg_bgm:
                panel_sounddata = self._get_panelsounddata(ogg)
                panel_sounddata.create_sounddata(ogg, source)

        if list_source_and_ogg_se != []:
            _list_source_and_ogg_se = sorted(
                list_source_and_ogg_se, key=lambda x: x[1])
            for source, ogg in _list_source_and_ogg_se:
                panel_sounddata = self._get_panelsounddata(ogg)
                panel_sounddata.create_sounddata(ogg, source)

        if list_source_and_ogg_others != []:
            for source, ogg in list_source_and_ogg_others:
                panel_sounddata = self._get_panelsounddata(ogg)
                list_sounddata = panel_sounddata.get_sounddatalist()
                for sounddata in list_sounddata:
                    if sounddata.get_oggfilepath() == ogg:
                        sounddata.set_sourcepath(source)

    def _get_panelsounddata(self, path_ogg):

        category, index = os.path.splitext(path_ogg)

        if category == 'bgm' or category == 'se':
            oggdir = category
        else:
            oggdir = os.path.basename(os.path.dirname(path_ogg))

        if oggdir == 'menu':
            return self.panel_menu
        elif oggdir == 'game':
            return self.panel_game
        elif oggdir == 'records':
            return self.panel_records
        elif oggdir == 'creative':
            return self.panel_creative
        elif oggdir == 'end':
            return self.panel_end
        elif oggdir == 'nether':
            return self.panel_nether
        elif oggdir == 'water':
            return self.panel_water
        elif oggdir == 'note':
            return self.panel_note
        elif oggdir == 'bgm':
            return self.panel_bgm
        elif oggdir == 'se':
            return self.panel_se
        else:
            return False

    def switch_viewermode(self):

        self.button_next.Hide()
        self.panel_records.switch_viewermode()
        self.panel_menu.switch_viewermode()
        self.panel_game.switch_viewermode()
        self.panel_creative.switch_viewermode()
        self.panel_end.switch_viewermode()
        self.panel_nether.switch_viewermode()
        self.panel_water.switch_viewermode()
        self.panel_note.switch_viewermode()
        self.panel_bgm.switch_viewermode()
        self.panel_se.switch_viewermode()

    def get_startwindow(self):
        return self.startwindow

    def get_inputpanel(self):
        return self.panel_input