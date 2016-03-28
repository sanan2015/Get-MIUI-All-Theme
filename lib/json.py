import json
from collections import OrderedDict

from lib import paths

def data():
	return OrderedDict()

def loads(str):
	return json.loads(str)

def dumps(data):
	return json.dumps(data,indent="	",ensure_ascii=False)

def loadfile(path):
	if paths.isfile(path):
		file = open(path,encoding="utf-8")
		text = file.read()
		file.close()
		return loads(text)
	return data()

def savefile(data,path):
	if not paths.isdir(paths.getdirname(path)):
		paths.makedirs(paths.getdirname(path))
	file = open(path,"w",encoding="utf-8")
	file.write(dumps(data))
	file.close()