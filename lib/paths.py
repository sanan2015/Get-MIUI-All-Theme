import os
import sys

def isdir(path):
	return os.path.isdir(path)

def isfile(path):
	return os.path.isfile(path)

def deletefile(path):
	if isfile(path):
		os.remove(path)

# makedirs

def movefile(path1,path2):
	deletefile(path2)
	if isfile(path1):
		os.rename(path1,path2)

def getabspath(path):
	return os.path.abspath(path)

def getdirname(path):
	return os.path.dirname(path)

def getname(path):
	return os.path.splitext(path)[0].replace(getdirname(path) + "\\","")

def getextension(path):
	return os.path.splitext(path)[1].replace(".","")

def makedirs(path):
	os.makedirs(path)

def startpath():
	return sys.path[0]