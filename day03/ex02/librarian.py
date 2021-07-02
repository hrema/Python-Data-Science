#!/Users/hrema/.brew/bin/python3

import os
import subprocess
import sys
import shutil

if __name__ == "__main__":
	if (os.environ['VIRTUAL_ENV'] != "/Users/hrema/Desktop/Python-Data-Science/day03/ex00/hrema"):
		raise RuntimeError("Wrong env")
	
	with open("install_modules", "w") as f:
		f.write("beautifulsoup4==4.9.3\n")
		f.write("pytest==6.2.4\n")
	
	subprocess.call(['python3', '-m', 'pip', 'install', '-r', 'install_modules'])
	os.remove("install_modules")

	with open('requirements.txt', 'w') as f:
		subprocess.Popen(['pip', 'freeze'], stdout=f)

	shutil.make_archive('hrema', 'zip', 'hrema')
