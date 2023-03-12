import configparser
import os
import subprocess

# building python 3.10.10 and cx_Freeze

# inisilize config.ini ----------------------------------
config = configparser.RawConfigParser()
config.read('./config.ini', 'utf-8')

config.set('export', 'edition', 'JE')
config.set('export', 'zip_compression', 'True')
config.set('export', 'select_version', '1.19.3')
config.set('export', 'savefolder', '')
config.set('packformat', 'list_packformat', '1.16,6|1.17,7|1.18,8|1.19,9|1.19.3,12')
config.set('window', 'size_start', '700,538')
config.set('window', 'size_sound', '1000,525')
config.set('linkbutton', 'musicfolder', '')

with open('./config.ini', 'w', encoding='utf-8') as file:
    config.write(file)

# run setup.py --------------------------------------------
subprocess.call(['python', 'setup.py', 'build'])

# make blank directory ------------------------------------
os.makedirs('build\\minecraft_soundreplacer\\image_user')
os.makedirs('build\\minecraft_soundreplacer\\temp')

print('complate building !')




