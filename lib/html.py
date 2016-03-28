from lib import paths
import requests
from bs4 import BeautifulSoup
from urllib import request

def gethtml(url):
	r = requests.get(url)
	if r.encoding == "UTF-8":
		r.encoding = "urf-8"
	else:
		r.encoding = "gbk"
	return str(r.text)

def soup(s):
	return BeautifulSoup(str(s), "html.parser")

def getsoup(url):
	return soup(gethtml(url))

# 获取指定长度的字符串
def getstr(s,l):
	s1 = "="
	for x in range(1,l):
		s1 += s
	return s1

# 进度条
def report_hook(count, block_size, total_size):
	p = (100.0 * count * block_size/ total_size)
	print("\r正在下载: [ " + getstr("=",int(p / 2)) + " ] " + '%02d%%'%p,end="")

def download(url,file,cover = False):
	if not paths.isdir(paths.getdirname(file)):
		paths.makedirs(paths.getdirname(file))
	if cover:
		if paths.isfile(file):
			paths.deletefile(file)
	if paths.isfile(file):
		print("\r已经下载: [ ================================================== ] 100%")
	else:
		try:
			try:
				paths.deletefile(file + ".temp")
				request.urlretrieve(url,file + ".temp",reporthook=report_hook)
				paths.movefile(file + ".temp",file)
			except Exception as e:
				print("\r正在下载: [ ================有其他程序正在下载================ ]     ",end="")
		except Exception as e:
			paths.deletefile(file + ".temp")
			print("\r正在下载: [ ===============下载失败已经删除文件=============== ]     ",end="")
	if paths.isfile(file):
		return True
	else:
		return False