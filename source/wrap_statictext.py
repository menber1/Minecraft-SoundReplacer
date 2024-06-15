import math
import os
import subprocess

import wx

from source.message import Message


class WrapStaticText(wx.StaticText):

    def __init__(self, parent, text, pos):
        wx.StaticText.__init__(self, parent, -1, text, pos=pos)

        self.parent = parent
        self.text = text

        width, height = self.get_nowsize()
        self.SetSize(width, height)

        self.SetBackgroundColour(wx.WHITE)
        self.font = wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "console")
        self.SetFont(self.font)
        self.Bind(wx.EVT_LEFT_DCLICK, self.doubleclick)

    def doubleclick(self, event):
        if self.text == '':
            return
        elif os.path.exists(self.text):
            path = os.path.dirname(self.text)
            path = os.path.normpath(path)
            subprocess.Popen(['explorer', path])
        else:
            Message().show(self, 'ファイルが見つかりません。再設定してください。')

    def resize(self, size):

        # parentのサイズからオフセットを引き自身のサイズとする。
        width, height = self.get_nowsize()
        self.SetSize((width, height))

        # 文字列全体のpx幅を取得。
        textwidth, textheight = self.GetTextExtent(self.text)
        # 自身のpx幅よりも、文字列px幅が小さければ1行表示
        if textwidth <= width:
            self.SetLabel(self.text)
            return

        # 現在の自身の幅で表示する場合、何行になるか計算
        rowcount = math.ceil(textwidth / width)

        # 一文字px幅を文字列分加算したリストを取得。[10,20,30,....]
        dc = wx.ScreenDC()
        dc.SetFont(self.font)
        text_widths = dc.GetPartialTextExtents(self.text)

        # 1行ずつ、文字列のどこからどこまでを取得するか
        # 取得した一行分の文字列と、次に取得すべき開始位置を取得。
        startindex = 0
        lines = []
        margin = 0
        for row in range(1, rowcount + 1):
            line, startindex, margin, text_widths = self.get_line(self.text, startindex, width, row, text_widths,
                                                                  margin)
            lines.append(line)

        # 各行に改行で連結し表示。
        worpping_text = ''
        for line in lines:
            worpping_text = worpping_text + line + '\n'
        worpping_text = worpping_text.rstrip('\n')
        self.SetLabel(worpping_text)
        self.Refresh()

    def get_line(self, text, startindex, linewidth, row, text_widths, margin):

        # 残された余白を各px幅に加算し、開始pxをずらす。
        if 1 < row:
            for i in range(startindex, len(text_widths)):
                text_widths[i] += margin

        # 次の行までの最終px幅
        linewidth = linewidth * row
        # 文字列のpx幅が加算されていくリストから行幅を超えるまで調べる
        worpindex = startindex
        for w in text_widths[startindex:]:
            if w < linewidth:
                worpindex = worpindex + 1
            else:
                break;

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
