import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

# URL 이동
url = "https://seekingalpha.com/earnings/earnings-call-transcripts"
dr = webdriver.Chrome()
dr.get(url)
# headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'}


# res = requests.get(dr.page, headers=headers)
# res.raise_for_status()
soup = BeautifulSoup(dr.page_source, "lxml")
time.sleep(2)

ect = soup.find("div",attrs={'class':'pqD bqGM'})
a = ect.find("article")
b = a.find("div",attrs={"class":"vsA bpA"})
c = b.find("a",attrs={"class":"vsE"})
print("제목 : "+c.text+"\n")
print("링크 : https://seekingalpha.com"+c['href'])

ect2 = ect.find_all("article",attrs={"class":"wdA rsA bpA bqW bqBH unA bqL bqCA unA bqL bqCA unE unE wdB"})
print(len(ect2))
# with open("etc.html", "w", encoding="utf8") as f:
#     f.write(soup.prettify())