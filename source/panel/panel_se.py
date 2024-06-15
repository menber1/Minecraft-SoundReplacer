from source.panel.panel_bgm import PanelBGM


class PanelSE(PanelBGM):

    CATEGORY = 'se.'
    # PATH_ICON = './image/dummy.png' 20230215

    def __init__(self, soundwindow):
        super().__init__(soundwindow)
