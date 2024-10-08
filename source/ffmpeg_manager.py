import os
import shutil
import subprocess

class FFmpegManager():

    PATH_FFMPEG = './ffmpeg-7.0.1-essentials_build/bin/ffmpeg'
    PATH_BATFILE = 'ffmpeg_converter.bat'

    def __init__(self):
        pass

    def create_batfile(self):
        if os.path.exists(self.PATH_BATFILE):
            os.remove(self.PATH_BATFILE)

        return open(self.PATH_BATFILE, 'wt', encoding='utf-8')


    def write_batfile(self, batfile, newsource, oggfile, mono=False):

        # 元々、oggファイルであった場合は、ffmpeg変換を回避できる。
        # ffmpeg_comverter.batには、echoだけを出力。ファイルが空の場合、subprosessが失敗するため
        if os.path.splitext(newsource)[1] == '.ogg' and mono == False:
            shutil.copy(newsource, oggfile)
            command = 'echo : ' + oggfile + ' : bypass the ogg conversion process....'
            batfile.write(command)
            return

        newsource = '"' + newsource + '"'  # パス内スペースを想定
        oggfile = '"' + oggfile + '"'
        ffmpeg_ = '"' + self.PATH_FFMPEG + '"'

        if mono == True:
            command = 'chcp 65001' + '\n' + ffmpeg_ + ' -i ' + newsource + ' -ac 1 ' + oggfile + '\n'  # -ac 1 モノラル変換指定 chcp 65001 UTF-8指定　日本語パス対応
        else:
            command = 'chcp 65001' + '\n' + ffmpeg_ + ' -i ' + newsource + ' ' + oggfile + '\n'

        batfile.write(command)
        return

    def close_batfile(self, batfile):
        batfile.close()

    def run_batfile(self):
        subprocess.run(self.PATH_BATFILE)


