from distutils.core import setup
import py2exe
import os
import sys

file = r'C:\\Development\\project_files\\minecraft_soundreplacer\\minecraft_soundreplacer.py'
icon = r'C:\\Development\\project_files\\minecraft_soundreplacer\\image\\icon_frame.ico'

source_dir = 'C:\\Development\\project_files\\minecraft_soundreplacer\\build\\source'
sys.path.append(source_dir)

options = {
    'packages': ['source'],
    'bundle_files': 1,
    'compressed': False,
    'optimize': 2,
    'dist_dir': 'dist'
}

setup(
    windows=[{"script": file, "icon_resources": [(1, icon)]}],
    options = {'py2exe': options}
)
