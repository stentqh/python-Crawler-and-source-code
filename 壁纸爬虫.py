import requests
from bs4 import BeautifulSoup
url = "https://www.tt98.com"
req = requests.get(url)
soup = BeautifulSoup(req.text,"lxml")
# soup.find_all("a")
tupian = soup.find_all("li")
# len (soup.find("ul"))查看li标签有几个
# soup.find_all("ul")[0]看第一个
soup.find_all("ul")[5].find_all("li") # 去看ul里第五个标签里的li标签
for li in soup.find_all("ul")[5].find_all("li"):
	dy_url = "https://www.tt98.com" + li.a.get("href")
	reg = requests.get(dy_url)
	soup1 = BeautifulSoup(reg.text,"lxml")
	dy_url1 = soup1.find("div", attrs = {"class":"photo"}).a.img.get("src")
	req = requests.get(dy_url1)
	name = dy_url1.split("/")[-1]
	with open(name,"wb") as f:
		f.write(req.content)