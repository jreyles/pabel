#!/usr/bin/python
import openbabel,pybel,os
from pybel import *

#OpenBabel Link. NEED TO DOWNLOAD A 2D .SDF FILE FIRST TO CONVERT.

def main():
	cwd=os.getcwd()
	dir=raw_input("Please enter the location of your input file:")
	os.chdir(dir)
	#Enter the input file name, must end with .sdf
	inputfile=raw_input("Please enter the 2D file name:")
	#Name output file, must end with .sdf
	outputfile=raw_input("Please enter the 3D output file name:")
	obConversion=openbabel.OBConversion()
	print "Converting..."
	#Example 2D and 3D names: obConversion.OpenInAndOutFiles("CID_54671008(2D).sdf","CID_54671008(3D).sdf")
	obConversion.OpenInAndOutFiles(inputfile,outputfile)
	obConversion.SetInAndOutFormats('sdf','sdf')
	obConversion.AddOption("gen3D",obConversion.GENOPTIONS)
	obConversion.Convert()
	obConversion.CloseOutFile()
	os.chdir(cwd)
	return "Complete!"
	
if __name__=='__main__':
	main()
else: 
	print "Babellink.py loaded"
	main()