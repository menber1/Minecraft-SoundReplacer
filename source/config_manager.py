import configparser
import os


class ConfigManager:

    def __init__(self):
        if not os.path.exists('./config.ini'):
            self.create_configfile()

    # 'JE' or 'BE'------------------------------------
    def set_minecraft_edition(self, edition):
        config = configparser.RawConfigParser()
        config.read('./config.ini')
        config.set('export', 'edition', edition)
        with open('./config.ini', 'w') as file:
            config.write(file)

    def get_minecraft_edition(self):
        config = configparser.RawConfigParser()
        config.read('./config.ini')
        return config.get('export', 'edition')

    # zip----------------------------------------------
    def set_zip_compression(self, flag):

        if flag == True:
            flag = 'True'
        else:
            flag = 'False'

        config = configparser.RawConfigParser()
        config.read('./config.ini')
        config.set('export', 'zip_compression', flag)
        with open('./config.ini', 'w') as file:
            config.write(file)

    def get_zip_compression(self):
        config = configparser.RawConfigParser()
        config.read('./config.ini')
        flag = config.get('export', 'zip_compression')
        if flag == 'True':
            return True
        else:
            return False

    # version-----------------------------------------------
    def get_packformat(self, version):
        config = configparser.RawConfigParser()
        config.read('./config.ini')
        packformat_csv = config.get('packformat', 'list_packformat')
        packformat_list = packformat_csv.split('|')

        for version_and_packformat in packformat_list:
            version_, packformat = version_and_packformat.split(',')
            if version_ == version:
                return int(packformat)

    def get_versionlist(self):
        config = configparser.RawConfigParser()
        config.read('./config.ini')
        packformat_csv = config.get('packformat', 'list_packformat')
        packformat_list = packformat_csv.split('|')

        versionlist = []
        for ver_and_pack in packformat_list:
            version, packformat = ver_and_pack.split(',')
            versionlist.append(version)
        return versionlist

    def get_select_version(self):
        config = configparser.RawConfigParser()
        config.read('./config.ini')
        version = config.get('export', 'select_version')
        if version == '':
            return '1.19.3'
        else:
            return version

    def set_select_version(self, version):
        config = configparser.RawConfigParser()
        config.read('./config.ini')
        config.set('export', 'select_version', version)
        with open('./config.ini', 'w') as file:
            config.write(file)

    # window size -------------------------------------------
    def get_size_startwindow(self):
        config = configparser.RawConfigParser()
        config.read('./config.ini')
        size = config.get('window', 'size_start')
        width, height = size.split(',')
        return (int(width), int(height))

    def set_size_startwindow(self, size):
        config = configparser.RawConfigParser()
        config.read('./config.ini')
        config.set('window', 'size_start', str(size[0]) + ',' + str(size[1]))
        with open('./config.ini', 'w') as file:
            config.write(file)

    def get_size_soundwindow(self):
        config = configparser.RawConfigParser()
        config.read('./config.ini')
        size = config.get('window', 'size_sound')
        width, height = size.split(',')
        return (int(width), int(height))

    def set_size_soundwindow(self, size):
        config = configparser.RawConfigParser()
        config.read('./config.ini')
        config.set('window', 'size_sound', str(size[0]) + ',' + str(size[1]))
        with open('./config.ini', 'w') as file:
            config.write(file)

    def get_path_musicfolder(self):
        config = configparser.RawConfigParser()
        config.read('./config.ini')
        path = config.get('linkbutton', 'musicfolder')
        return path

    def set_path_musicfolder(self, path):
        config = configparser.RawConfigParser()
        config.read('./config.ini')
        config.set('linkbutton', 'musicfolder', path)
        with open('./config.ini', 'w') as file:
            config.write(file)
