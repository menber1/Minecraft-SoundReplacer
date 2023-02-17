import os
import shutil
import subprocess


class FFmpegManager():

    path_root = os.getcwd()
    PATH_FFMPEG = os.path.join(
        path_root, 'ffmpeg-5.1.2-essentials_build/bin/ffmpeg')
    PATH_BATFILE = os.path.join(path_root, 'ffmpeg_converter.bat')

    def __init__(self):
        pass

    def create_batfile(self):
        if os.path.exists(self.PATH_BATFILE):
            os.remove(self.PATH_BATFILE)

        return open(self.PATH_BATFILE, 'wt', encoding='utf-8')

    def write_batfile(self, batfile, newsource, oggfile, mono=False):

        if os.path.splitext(newsource)[1] == '.ogg' and mono == False:
            shutil.copy(newsource, oggfile)
            return

        newsource = '"' + newsource + '"'
        oggfile = '"' + oggfile + '"'
        ffmpeg_ = os.path.join(os.getcwd(), self.PATH_FFMPEG)

        if mono == True:
            command = 'chcp 65001' + '\n' + ffmpeg_ + ' -i ' + newsource + \
                ' -ac 1 ' + oggfile + '\n'
        else:
            command = 'chcp 65001' + '\n' + ffmpeg_ + \
                ' -i ' + newsource + ' ' + oggfile + '\n'

        batfile.write(command)

    def close_batfile(self, batfile):
        batfile.close()

    def run_batfile(self):
        subprocess.run(self.PATH_BATFILE)
