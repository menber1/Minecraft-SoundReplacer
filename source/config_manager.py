import configparser
import os


class ConfigManager:

    def __init__(self):
        if not os.path.exists('./config.ini'):
            self.create_configfile()

    # 'JE' or 'BE'
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

    # zip
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

    def set_packformat(self, version):
        packformat = 12

        if version == '1.16':
            packformat = 6
        elif version == '1.17':
            packformat = 7
        elif version == '1.18':
            packformat = 8
        elif version == '1.19':
            packformat = 9
        elif version == '1.19.3':
            packformat = 12

        config = configparser.RawConfigParser()
        config.read('./config.ini')
        config.set('export', 'pack_format', packformat)
        with open('./config.ini', 'w') as file:
            config.write(file)

    def get_packformat(self):
        config = configparser.RawConfigParser()
        config.read('./config.ini')
        number = config.get('export', 'pack_format')

        try:
            return int(number)
        except ValueError:
            print('ValueError: config.ini pack_formatの設定に不正値')
            return 9

    def get_version(self):
        packformat = self.get_packformat()
        if packformat == 6:
            return '1.16'
        elif packformat == 7:
            return '1.17'
        elif packformat == 8:
            return '1.18'
        elif packformat == 9:
            return '1.19'
        elif packformat == 12:
            return '1.19.3'
        else:
            return '1.19.3'
