import os
import subprocess
import webbrowser
import wx
import csv
from source.filedroptarget import FileDropTarget
from source.message import Message


class SoundData(wx.Panel):

    WIDTH = 945
    HEIGHT = 72

    def __init__(self, scrollwindow, panel_sounddata, path_ogg, pos_):
        wx.Panel.__init__(self, scrollwindow, pos=pos_,
                          size=(self.WIDTH, self.HEIGHT))

        self.SetBackgroundColour('WHITE')
        line = wx.Panel(self, pos=(15, self.HEIGHT-1),
                        size=(self.WIDTH - 10, 1))
        line.SetBackgroundColour('#969696')

        self.path_ogg = path_ogg
        self.path_sourcefile = ''
        self.flag_sound_run = False
        self.panel_sounddata = panel_sounddata
        self.flag_drag_and_drop = True

        path_pngfile = self.panel_sounddata.get_pngfilepath(path_ogg)
        self.icon = wx.StaticBitmap(
            self, -1, wx.Bitmap(path_pngfile), pos=(5, 2), size=(64, 64))

        title = self.get_soundtitle()
        self.statictext_recordtitle = wx.StaticText(
            self, -1, title, pos=(self.HEIGHT + 10, 10))

        self.button_run_record = wx.BitmapButton(
            self, -1, wx.Bitmap('./image/button_music.png'), pos=(self.HEIGHT + 10, 40), size=(16, 16))
        self.button_run_record.SetBitmapPressed(
            wx.Bitmap('./image/button_music_on.png'))
        self.button_run_record.SetBitmapFocus(
            wx.Bitmap('./image/button_music_hover.png'))
        self.button_run_record.SetToolTip('元音源再生')
        self.button_run_record.Bind(wx.EVT_BUTTON, self.click_run_record)

        self.button_clear = wx.BitmapButton(
            self, -1, wx.Bitmap('./image/button_cancel.png'), pos=(self.HEIGHT + 30, 40), size=(16, 16))
        self.button_clear.SetBitmapPressed(
            wx.Bitmap('./image/button_cancel_on.png'))
        self.button_clear.SetBitmapFocus(
            wx.Bitmap('./image/button_cancel_hover.png'))
        self.button_clear.SetToolTip('設定消去')
        self.button_clear.Bind(wx.EVT_BUTTON, self.click_clearbutton)

        self.button_select = wx.BitmapButton(
            self, -1, wx.Bitmap('./image/button_folder.png'), pos=(self.HEIGHT + 50, 40), size=(16, 16))
        self.button_select.SetBitmapPressed(
            wx.Bitmap('./image/button_folder_on.png'))
        self.button_select.SetBitmapFocus(
            wx.Bitmap('./image/button_folder_hover.png'))
        self.button_select.SetToolTip('フォルダ選択')
        self.button_select.Bind(wx.EVT_BUTTON, self.click_selectbutton)

        self.button_run_soundfile = wx.BitmapButton(
            self, -1, wx.Bitmap('./image/button_sound.png'), pos=(self.HEIGHT + 70, 40), size=(16, 16))
        self.button_run_soundfile.SetBitmapPressed(
            wx.Bitmap('./image/button_sound_on.png'))
        self.button_run_soundfile.SetBitmapFocus(
            wx.Bitmap('./image/button_sound_hover.png'))
        self.button_run_soundfile.SetToolTip('ファイル再生')
        self.button_run_soundfile.Bind(wx.EVT_BUTTON, self.click_run_soundfile)

        varticalline = wx.Panel(self, -1, pos=(200, 10), size=(1, 53))
        varticalline.SetBackgroundColour('#969696')

        path_replacesound = ''
        self.statictext_replacesound = wx.StaticText(
            self, -1, path_replacesound, pos=(self.HEIGHT + 140, 10), size=(740, 50))

        self.SetDropTarget(FileDropTarget(self, self.statictext_replacesound))

    def get_oggfilepath(self):
        return self.path_ogg

    def get_soundtitle(self):
        basename = os.path.basename(self.path_ogg)
        name, ext = os.path.splitext(basename)
        return name

    def get_pngfilepath(self, path_sourcefile=None):
        return ''

    def click_clearbutton(self, event):
        self.statictext_replacesound.SetLabel('')
        self.path_sourcefile = ''

    def click_selectbutton(self, event):

        filter = " All file(*.*) | *.*|" \
                 " WAV (*.wav;*.WAV) | *.wav;*.WAV |" \
                 " WMA (*.wma;*.WMA) | *.wma;*.WMA |" \
                 " MP3 (*.mp3;*.MP3) | *.mp3;*.MP3 |" \
                 " AAC (*.aac;*.AAC) | *.aac;*.AAC |" \
                 " M4A (*.m4a;*.M4A) | *.m4a;*.M4A |" \
                 " FLAC (*.flac;*.FLAC) | *.flac;*.FLAC |" \
                 " Vorbis (*.ogg;*.OGG) | *.ogg;*.OGG"

        with wx.FileDialog(self.button_select, '音声ファイルを指定してください。', '', '', filter) as dialog:
            if dialog.ShowModal() == wx.ID_CANCEL:
                return

            path = dialog.GetPath()
            path = self.replace_escape(path)

            if self.check_ext(path):
                self.set_sourcepath(path)
            else:
                dialog = wx.MessageDialog(
                    self, 'サポートされない拡張子です。', 'メッセージ', style=wx.OK)
                dialog.ShowModal()
                dialog.Destroy()

    def click_run_record(self, event):

        if 'PanelNote' == self.get_parentpanel().__class__.__name__:
            path = '"' + self.path_ogg + '"'
            subprocess.run(path, shell=True)
        else:
            filename = os.path.splitext(os.path.basename(self.path_ogg))[0]
            with open('./url.csv', 'r', newline='') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)
                for row in reader:
                    if row[0] == filename:
                        webbrowser.open(row[2])
                        return

    def click_run_soundfile(self, event):

        if self.path_sourcefile == '':
            return
        if not os.path.exists(self.path_sourcefile):
            Message().show(self, '指定されたファイルが見つかりません。')
            return

        path = '"' + self.path_sourcefile + '"'
        subprocess.run(path, shell=True)

    def split_longpath(self, path):

        if len(path) <= 110:
            return path

        front = path[0:91]
        enpos = front.rfind('/')
        front = path[0:enpos]
        back = path.replace(front, '')

        if len(back) <= 110:
            return front + '\n' + back

        mid = back[0:91]
        enpos = mid.rfind('/')
        mid = back[0:enpos]
        back = back.replace(mid, '')

        return front + '\n' + mid + '\n' + back

    def set_sourcepath(self, sourcepath):
        self.path_sourcefile = sourcepath
        sourcepath_ = self.split_longpath(sourcepath)
        self.statictext_replacesound.SetLabel(sourcepath_)

        if os.path.isfile(self.path_sourcefile):
            self.statictext_replacesound.SetForegroundColour(wx.BLACK)
        else:
            self.statictext_replacesound.SetForegroundColour((130, 130, 130))
        self.statictext_replacesound.Refresh()

    def check_ext(self, path):
        name, ext = os.path.splitext(os.path.basename(path))
        ext = ext.lower()
        if ext in ['.wav', '.mp3', '.m4a', '.aac', '.flac', '.wma', '.ogg']:
            return True
        else:
            return False

    def get_source_and_ogg(self):
        return self.path_sourcefile, self.path_ogg

    def replace_escape(self, path):
        return path.replace('\\', '/')

    def switch_viewermode(self):
        self.button_select.Disable()
        self.button_clear.Disable()
        self.flag_drag_and_drop = False

    def get_flag_drag_and_drop(self):
        return self.flag_drag_and_drop

    def get_parentpanel(self):
        return self.panel_sounddata
