'''
PaDEL-Descriptor Script
v 1.0 4/28/2013
Program takes a user-defined input of the PaDEL directory. The script then launches PaDEL and processes the SDF & MOL files.

'''

import os
import subprocess
import popen2
import shlex
'''
#Running it the OS way. Fastest way, but doesn't return PaDEL text output. 
cwd=os.getcwd()
os.chdir('/Users/zen/Downloads/PaDEL-Descriptor/')	#Need to change to the directory that the PaDEL-Descriptor.jar file is located in. 
os.system('java -jar PaDEL-Descriptor.jar -dir /Users/zen/Downloads/PaDEL-Descriptor/Test -file test.csv -3d -fingerprints -removesalt -standardizenitro -log -retainorder')
os.chdir(cwd)

#Running it the popen2 way. Deprecated module but returns PaDEL text output.
cwd=os.getcwd()
os.chdir('/Users/zen/Downloads/PaDEL-Descriptor')
cmdout,cmdin = popen2.popen2('java -jar PaDEL-Descriptor.jar -dir C:\Padel\Test -file test.csv -3d -fingerprints -removesalt -standardizenitro -log -retainorder')
for line in cmdout: print line,
os.chdir(cwd)
'''

#Input variables for user-defined entries.
#working_dir = input


#Running it the subprocess way. Succeeds the POPEN2 module. Requires more code but returns PaDEL text output.
cwd=os.getcwd()
os.chdir('/Users/zen/Downloads/PaDEL-Descriptor')
command_line='java -jar PaDEL-Descriptor.jar -dir /Users/zen/Downloads/PaDEL-Descriptor/Test/ -file test.csv -3d -fingerprints -removesalt -standardizenitro -log -retainorder'
args=command_line.split(' ')
padel=subprocess.Popen(args,stdin=subprocess.PIPE,stdout=subprocess.PIPE)
stdout,stderr=padel.communicate()
print stdout.rstrip()
os.chdir(cwd)

#Open Babel.jar
#Editting the .csv for adding class and compound name(looking into SDF)
#database offline 

