import shutil
import os
import time
import subprocess
from distutils.core import setup
import py2exe

# EXEファイルを生成　※python 3.10 で実行すること。


# py2exe setup.pyと同じディレクトリでなければ、パッケージを読み込まないため
# sourceフォルダをコピー、exe作成後削除
path_project = 'C:/Development/project_files/minecraft_soundreplacer/source'
path_dist = './source'
shutil.copytree(path_project, path_dist)
print('copy : package sorce')

os.makedirs('./dist/image_user')
os.makedirs('./dist/temp')
print('make dir : temp, image_user')

path_project = 'C:/Development/project_files/minecraft_soundreplacer/url.csv'
path_dist = './dist/url.csv'
shutil.copy(path_project, path_dist)
print('copy : url.csv')

path_project = 'C:/Development/project_files/minecraft_soundreplacer/ffmpeg-7.0.1-essentials_build'
path_dist = './dist/ffmpeg-7.0.1-essentials_build'
shutil.copytree(path_project, path_dist)
print('copy : ffmpeg package')

path_project = '/関連データ/Vanilla_Resource_Pack_1.21.0'
path_dist = './dist/Vanilla_Resource_Pack_1.21.0'
shutil.copytree(path_project, path_dist)
print('copy : minecraft Vanilla pacakage BE')

path_project = '/関連データ/Vanilla_Resource_Pack_1.21_JE'
path_dist = './dist/Vanilla_Resource_Pack_1.21_JE'
shutil.copytree(path_project, path_dist)
print('copy : Minecraft Vanilla package JE')

path_project = 'C:/Development/project_files/minecraft_soundreplacer/image'
path_dist = './dist/image'
shutil.copytree(path_project, path_dist)
print('copy : image dir')

path_project = 'C:/Development/project_files/minecraft_soundreplacer/config.ini'
path_dist = './dist/config.ini'
shutil.copyfile(path_project, path_dist)
print('copy : config.ini')

time.sleep(15)

subprocess.call(['python', 'setup.py', 'py2exe'])
print('run setup.py')

time.sleep(15)

os.rename('./dist', 'minecraft_soundreplacer_v')
shutil.rmtree('./build')
shutil.rmtree('./source')

print('complate building !!!!!!!!!!!!')




