import shutil
import os
import time
import subprocess

'''
Execution environment python 3.10

'''

os.system('minecraft_soundreplacer_exe.bat')

time.sleep(15)

os.makedirs('./dist/minecraft_soundreplacer/image_user')
os.makedirs('./dist/minecraft_soundreplacer/temp')

path_project = 'C:/...Path to project directory.../minecraft_soundreplacer/url.csv'
path_dist = './dist/minecraft_soundreplacer/url.csv'

shutil.copy(path_project, path_dist)

path_project = 'C:/...Path to project directory.../minecraft_soundreplacer/ffmpeg-5.1.2-essentials_build'
path_dist = './dist/minecraft_soundreplacer/ffmpeg-5.1.2-essentials_build'

shutil.copytree(path_project, path_dist)

path_project = 'C:/...Path to project directory.../minecraft_soundreplacer/Vanilla_Resource_Pack_1.19.0'
path_dist = './dist/minecraft_soundreplacer/Vanilla_Resource_Pack_1.19.0'

shutil.copytree(path_project, path_dist)

path_project = 'C:/...Path to project directory.../minecraft_soundreplacer/Vanilla_Resource_Pack_1.19_JE'
path_dist = './dist/minecraft_soundreplacer/Vanilla_Resource_Pack_1.19_JE'

shutil.copytree(path_project, path_dist)

path_project = 'C:/...Path to project directory.../minecraft_soundreplacer/image'
path_dist = './dist/minecraft_soundreplacer/image'

shutil.copytree(path_project, path_dist)

path_project = 'C:/...Path to project directory.../minecraft_soundreplacer/config.ini'
path_dist = './dist/minecraft_soundreplacer/config.ini'

shutil.copyfile(path_project, path_dist)

shutil.copy(path_project, path_dist)

print('complate building !')
