import math
import wx


class WrapStaticText(wx.StaticText):

    def __init__(self, parent, text, pos):
        wx.StaticText.__init__(self, parent, -1, text, pos=pos)

        self.parent = parent
        self.text = text

        width, height = self.get_nowsize()
        self.SetSize(width, height)

        self.SetBackgroundColour(wx.WHITE)
        self.font = wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL,
                            wx.FONTWEIGHT_NORMAL, False,  "console")
        self.SetFont(self.font)

    def resize(self, size):

        width, height = self.get_nowsize()
        self.SetSize((width, height))

        textwidth, textheight = self.GetTextExtent(self.text)

        if textwidth <= width:
            self.SetLabel(self.text)
            return

        rowcount = math.ceil(textwidth / width)

        dc = wx.ScreenDC()
        dc.SetFont(self.font)
        text_widths = dc.GetPartialTextExtents(self.text)

        startindex = 0
        lines = []
        margin = 0
        for row in range(1, rowcount + 1):
            line, startindex, margin, text_widths = self.get_line(
                self.text, startindex, width, row, text_widths, margin)
            lines.append(line)

        worpping_text = ''
        for line in lines:
            worpping_text = worpping_text + line + '\n'
        worpping_text = worpping_text.rstrip('\n')
        self.SetLabel(worpping_text)
        self.Refresh()

    def get_line(self, text, startindex, linewidth, row, text_widths, margin):

        if 1 < row:
            for i in range(startindex, len(text_widths)):
                text_widths[i] += margin

        linewidth = linewidth * row

        worpindex = startindex
        for w in text_widths[startindex:]:
            if w < linewidth:
                worpindex = worpindex + 1
            else:
                break

        if worpindex < len(text_widths):
            margin = linewidth - text_widths[worpindex - 1]
        else:
            margin = 0

        return text[startindex:worpindex], worpindex, margin, text_widths

    def set_label(self, text):
        self.text = text
        self.resize(self.get_nowsize())

    def get_nowsize(self):
        size = self.parent.GetSize()
        width = size[0] - 250
        height = size[1] - 22
        return (width, height)

    def get_text(self):
        return self.text
