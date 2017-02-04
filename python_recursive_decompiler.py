#!/usr/bin/python

#This application is used to decompile ANY AND ALL .pyc files in the directory 
#of your choosing. John Ciavarella 2012

import os
import commands
import glob
import subprocess

uncompyle='uncompyle2'

Uselect=raw_input("Would you like to use the current directory? [y or n]: ")

if Uselect == "y":
	for filename in glob.glob("*"):
		outputfile=filename+'_uncompiled'
		command1=[uncompyle, -o outputfile, filename]
	subprocess.call(command1)
