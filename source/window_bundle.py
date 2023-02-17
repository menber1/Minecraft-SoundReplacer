import wx

class WindowBundle(wx.Frame):

    WIDTH = 850
    HEIGHT = 200
    TOOLBAR_HEIGHT = 35

    def __init__(self, parent, bundle):
        wx.Frame.__init__(self, parent, title="select bundled folder", size=(
            self.WIDTH, self.HEIGHT))

        self.SetBackgroundColour(wx.WHITE)
        icon = wx.Icon('./image/icon_frame.ico')
        self.SetIcon(icon)

        self.soundwindow = parent

        x, y = self.soundwindow.GetPosition()
        self.SetPosition((x + 120, y + 410))

        self.toolbar = wx.Panel(self, pos=(0, 0), size=(
            self.WIDTH, self.TOOLBAR_HEIGHT))
        self.toolbar.SetBackgroundColour(wx.WHITE)

        self.button_add = wx.BitmapButton(
            self.toolbar, -1, wx.Bitmap('./image/button_folder.png'), pos=(15, 10), size=(16, 16))
        self.button_add.SetBitmapPressed(
            wx.Bitmap('./image/button_folder_on.png'))
        self.button_add.SetBitmapFocus(
            wx.Bitmap('./image/button_folder_hover.png'))
        self.button_add.SetToolTip('追加')
        self.button_add.Bind(wx.EVT_BUTTON, self.click_add)

        self.button_remove = wx.BitmapButton(
            self.toolbar, -1, wx.Bitmap('./image/button_cancel.png'), pos=(45, 10), size=(16, 16))
        self.button_remove.SetBitmapPressed(
            wx.Bitmap('./image/button_cancel_on.png'))
        self.button_remove.SetBitmapFocus(
            wx.Bitmap('./image/button_cancel_hover.png'))
        self.button_remove.SetToolTip('選択を除外する')
        self.button_remove.Bind(wx.EVT_BUTTON, self.click_remove)

        wx.StaticText(
            self.toolbar, -1, 'copy to : <JE>./assets/minecraft/...    <BE>./...', pos=(100, 10))

        self.panel_bottom = wx.Panel(self, pos=(0, 35), size=(
            self.WIDTH, self.HEIGHT - self.TOOLBAR_HEIGHT))
        self.panel_bottom.SetBackgroundColour(wx.WHITE)

        self.listbox = wx.ListBox(self.panel_bottom, -1, pos=(0, 0), size=(
            self.WIDTH, self.HEIGHT - self.TOOLBAR_HEIGHT), choices=bundle)

        self.Bind(wx.EVT_CLOSE, self.close_window)

        self.Show()

    def click_add(self, event):
        dlg = wx.DirDialog(self, "リソースパックに同梱するフォルダを選択",
                           style=wx.DD_DEFAULT_STYLE)
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            self.listbox.Append(path)
        dlg.Destroy()

    def click_remove(self, event):
        selected = self.listbox.GetSelection()
        if selected != wx.NOT_FOUND:
            self.listbox.Delete(selected)

    def close_window(self, event):
        self.soundwindow.get_inputpanel().set_adddirectory(self.listbox.GetItems())
        self.Destroy()
