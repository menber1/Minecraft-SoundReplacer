import configparser
import os
import subprocess

# building python 3.11.4 and cx_Freeze
subprocess.call(['python', 'setup.py', 'build'])
os.makedirs('build\\minecraft_soundreplacer\\image_user')
os.makedirs('build\\minecraft_soundreplacer\\temp')
print('complate building !')
