import os
import subprocess
from distutils.core import setup
import py2exe
import time


# building python 3.10.10 and cx_Freeze

subprocess.call(['python', 'setup.py', 'build'])

os.makedirs('build\\minecraft_soundreplacer\\image_user')
os.makedirs('build\\minecraft_soundreplacer\\temp')

print('complate building !')




