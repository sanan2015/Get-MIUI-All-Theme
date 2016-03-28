from lib import cmd
from lib import html
from lib import paths
from lib import json
from lib import xml
from lib import zips

def isnext(soup):
	if len(soup.findAll("a", text=["下一页"])) > 0:
		return True
	else:
		return False
def getTheme(themeid):
	page = "http://m.zhuti.xiaomi.com" + themeid
	soup = html.getsoup(page)

	s = str(soup.find_all("div", class_="theme-tit")[0])
	title = s[s.rfind("tit\">") + 1 + 11:s.rfind("<s")]
	size = s[s.rfind("<span>")+6:s.rfind("</")-8]

	s = str(soup.find_all("div", class_="theme-infos")[0])
	defigner = s[s.rfind("设计师") + 4:s.rfind("<br") - 7]
	maker = s[s.rfind("制作者") + 4:s.rfind("</") - 5]

	s = str(soup.find_all("div", class_="theme-introduce")[0])
	# description = s[29:len(s) - 7]

	s = str(soup.find_all("div", class_="version-info")[0])
	update = s[s.rfind("info")+11:len(s) - 6].replace(":","-")

	s = str(soup.find_all("a", class_="btn-comments")[0])
	comment = s[s.rfind("<span>")+6:s.rfind("</span>")] + "条"

	downloadlink =  "http://zhuti.xiaomi.com" + themeid.replace("detail","download")

	s = str(soup.find_all("div", class_="star-rank")[0])
	score = s[s.rfind("rank")+6:s.rfind("><")-1] + "分(满分10分)"
	
	# price = ""


	print("　　名称: " + title)
	print("　　大小: " + size)
	# print("　设计师: " + defigner)
	# print("　制作者: " + maker)
	# print("　　介绍: " + description)
	# print("更新时间: " + update)
	# print("　　评论: " + comment)
	# print("下载地址: " + downloadlink)
	# print("　　评分: " + score)
	# print("　　售价: " + price)

	if html.download(downloadlink,paths.startpath() + "/MIUI主题商店爬虫/下载/" + title + " " + update + ".mtz"):
		# zips.unzip(paths.startpath() + "/MIUI主题商店爬虫/下载/" + title + " " + update + ".mtz",paths.startpath() + "/下载测试/" + title + " " + update)
		pass
	
	# print("")
	# cmd.pause("执行完成，按任意键继续...")
def getThemes(soup):
	soup1 = html.soup(str(soup.find_all("ul", class_="thumb-list")))
	soup2 = soup1.find_all("a")
	istheme = True
	for theme in soup2:
		if istheme:
			getTheme(theme["href"])
			istheme = False
		else:
			istheme = True
def main():
	cmd.title("MIUI主题商店爬虫")
	cmd.size(70,36)
	try:
		page = 100
		while True:
			soup = html.getsoup('http://zhuti.xiaomi.com/compound?page=' + str(page) + '&sort=New')
			if isnext(soup):
				getThemes(soup)
				page += 1
			else:
				break
	except Exception as e:
		print(e)
	cmd.pause("执行完成，按任意键继续...")
if __name__=='__main__':
	main()