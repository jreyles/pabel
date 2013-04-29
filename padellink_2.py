import os,subprocess,popen2,shlex

#Running it the subprocess way. Succeeds the POPEN2 module. Requires more code but returns PaDEL text output.
cwd=os.getcwd()
working_dir=raw_input("Please enter the working directory of PaDEL:")
os.chdir(working_dir)
file_location=raw_input("Please enter the directory for the location of the file:")
command_line='java -jar PaDEL-Descriptor.jar -dir ' + file_location+ ' -file test.csv -3d -fingerprints -removesalt -standardizenitro -log -retainorder'
args=command_line.split(' ')
padel=subprocess.Popen(args,stdin=subprocess.PIPE,stdout=subprocess.PIPE)
stdout,stderr=padel.communicate()
print stdout.rstrip()
os.chdir(cwd)

#Things to add:
#Editting the .csv for adding class and compound name(looking into SDF) database offline 

'''
Ignore everything in this section:
#Running it the OS way. Fastest way, but doesn't return PaDEL text output. 
cwd=os.getcwd()
os.chdir('C:\Padel')	#Need to change to the directory that the PaDEL-Descriptor.jar file is located in. 
os.system('java -jar PaDEL-Descriptor.jar -dir C:\Padel\Test -file test.csv -3d -fingerprints -removesalt -standardizenitro -log -retainorder')
os.chdir(cwd)

#Running it the popen2 way. Deprecated module but returns PaDEL text output.
cwd=os.getcwd()
os.chdir('C:\Padel')
cmdout,cmdin = popen2.popen2('java -jar PaDEL-Descriptor.jar -dir C:\Padel\Test -file test.csv -3d -fingerprints -removesalt -standardizenitro -log -retainorder')
for line in cmdout: print line,
os.chdir(cwd)

#OpenBabel Link

obConversion=openbabel.OBConversion()
obConversion.OpenInAndOutFiles("CID_54671008(2D).sdf","CID_54671008(3D).sdf")
obConversion.SetInAndOutFormats('sdf','sdf')
obConversion.AddOption("gen3D",obConversion.GENOPTIONS)
obConversion.Convert()
obConversion.CloseOutFile()
'''	