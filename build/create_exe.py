import shutil
import os
import time
import subprocess

'''
Execution environment python 3.10

'''

os.system('soundreplacer_exe.bat')

#os.system('"cd cd %~dp0"')
#subprocess.run(['pyinstaller', r'C:\...Path to project directory...\recordreplacer.py', '--noconsole'], shell=True)

time.sleep(15)

os.makedirs('./dist/soundreplacer/image_user')
os.makedirs('./dist/soundreplacer/temp')

path_project = 'C:/...Path to project directory.../minecraft_soundreplacer/url.csv'
path_dist = './dist/soundreplacer/url.csv'

shutil.copy(path_project, path_dist)

path_project = 'C:/...Path to project directory.../ffmpeg-5.1.2-essentials_build'
path_dist = './dist/soundreplacer/ffmpeg-5.1.2-essentials_build'

shutil.copytree(path_project, path_dist)

path_project = 'C:/...Path to project directory.../Vanilla_Resource_Pack_1.19.0'
path_dist = './dist/soundreplacer/Vanilla_Resource_Pack_1.19.0'

shutil.copytree(path_project, path_dist)

path_project = 'C:/...Path to project directory.../Vanilla_Resource_Pack_1.19_JE'
path_dist = './dist/soundreplacer/Vanilla_Resource_Pack_1.19_JE'

shutil.copytree(path_project, path_dist)

path_project = 'C:/...Path to project directory.../image'
path_dist = './dist/soundreplacer/image'

shutil.copytree(path_project, path_dist)

path_project = 'C:/...Path to project directory.../config.ini'
path_dist = './dist/soundreplacer/config.ini'

shutil.copyfile(path_project, path_dist)

print('complate building !')




