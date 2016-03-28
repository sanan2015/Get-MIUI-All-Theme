import os

def title(str):
	os.system("@echo off")
	os.system("title=" + str)

def pause(str):
	print(str)
	os.system("pause > nul")

def size(cols,lines):
	os.system("mode con cols=" + str(cols) + " lines=" + str(lines))