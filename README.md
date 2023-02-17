
//////////////////////////////////////////////////////////////////////

Minecraft-SoundReplacer  

//////////////////////////////////////////////////////////////////////

Version : 0.7b

License : GNU GENERAL PUBLIC LICENSE Version 3
 
Libraries used : ffmpeg-5.1.2-essentials_build (GPLv3) 

FFmpeg source code for the version used : /ffmpeg-snapshot.tar.bz2



//////////////////////////////////////////////////////////////////////

Build Steps 

//////////////////////////////////////////////////////////////////////

1. path rewriting : /build/soundreplacer.spec

	'C:\\...Path to project directory...\\soundreplacer.py'
	
	icon=['C:\\...Path to project directory...\\image\\icon_frame.ico'],
	
2. path rewriting : /build/soundreplacer_exe.bat

	pyinstaller C:\...Path to project directory...\soundreplacer.py --noconsole --icon=C:\...Path to project directory...\image\icon_frame.ico --clean
	
	If pyinstaller is not installed, pip install.
	
3. path rewriting : /build/create_exe.py

	path_project = 'C:/...Path to project directory.../minecraft_soundreplacer/url.csv'

	path_project = 'C:/...Path to project directory.../ffmpeg-5.1.2-essentials_build'

	path_project = 'C:/...Path to project directory.../Vanilla_Resource_Pack_1.19.0'

	path_project = 'C:/...Path to project directory.../Vanilla_Resource_Pack_1.19_JE'

	path_project = 'C:/...Path to project directory.../image'

	path_project = 'C:/...Path to project directory.../config.ini'
	
4. run create_exe.py 

	Running with python 3.10.
