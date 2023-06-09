import configparser
import os
import subprocess

# building python 3.11.4 and cx_Freeze

# inisilize config.ini ----------------------------------
config = configparser.RawConfigParser()
config.read('./config.ini', 'utf-8')

config.set('export', 'edition', 'JE')
config.set('export', 'zip_compression', 'True')
config.set('export', 'select_version', '')
config.set('export', 'savefolder', '')
config.set('packformat', 'list_packformat', '1.16,6|1.17,7|1.18,8|1.19,9|1.19.3,12|1.19.4,13|1.20,15')
config.set('window', 'size_start', '700,538')
config.set('window', 'size_sound', '1000,525')
config.set('linkbutton', 'musicfolder', '')
config.set('music', 'record', '11,13,5,blocks,cat,chirp,far,mall,mellohi,otherside,pigstep,relic,stal,strad,wait,ward')
config.set('music', 'menu', 'menu1,menu2,menu3,menu4')
config.set('music', 'game', 'a_familiar_room,aerie,ancestry,an_ordinary_day,bromeliad,calm1,calm2,calm3,'
                            'comforting_memories,crescent_dunes,echo_in_the_wind,firebugs,floating_dream,hal1,hal2,'
                            'hal3,hal4,infinite_amethyst,labyrinthine,left_to_bloom,nuance1,nuance2,one_more_day,'
                            'piano1,piano2,piano3,stand_tall,wending')
config.set('music', 'creative', 'creative1,creative2,creative3,creative4,creative5,creative6')
config.set('music', 'end', 'boss,credits,end')
config.set('music', 'nether', 'chrysopoeia,nether1,nether2,nether3,nether4,rubedo,so_below')
config.set('music', 'water', 'axolotl,dragon_fish,shuniji')
config.set('music', 'note', 'banjo,bass,bd,bell,bit,cow_bell,didgeridoo,flute,guitar,harp,hat,icechime,'
                            'iron_xylophone,pling,snare,xylobone')

with open('./config.ini', 'w', encoding='utf-8') as file:
    config.write(file)

# run setup.py --------------------------------------------
subprocess.call(['python', 'setup.py', 'build'])

# make blank directory ------------------------------------
os.makedirs('build\\minecraft_soundreplacer\\image_user')
os.makedirs('build\\minecraft_soundreplacer\\temp')

print('complate building !')




