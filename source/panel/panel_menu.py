from source.panel.panel_sounddata import PanelSoundData
from source.vanilla_resourcepack import VanillaResourcePack


class PanelMenu(PanelSoundData):

    def __init__(self, soundwindow):
        path_soundfiles = VanillaResourcePack().get_pathlist('menu')
        super().__init__(soundwindow, path_soundfiles)

    def get_pngfilepath(self, path_ogg=None):
        return './image/stone.png'