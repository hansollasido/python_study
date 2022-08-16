from xml.etree.ElementPath import xpath_tokenizer
import requests
from bs4 import BeautifulSoup
# header 정보를 통해 구글에서는 제공하는 정보가 다름

headers={"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
"Accept-Language":"ko-KR,ko" # 한국어 페이지로 제공함
}


# 스크롤 내릴 때마다 로딩이 되어 영화가 보여줌 -> 나머지 영화에 대해서는 보여주지 않음

url = "https://play.google.com/store/search?q=%EC%9D%B8%EA%B8%B0%EC%98%81%ED%99%94&c=movies"
res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")

movies = soup.find_all("div", attrs={"class":"VfPpkd-EScbFb-JIbuQc UVEnyf"})


#print(len(movies))
#print(movies[0].prettify())


#with open("movie.html", "w", encoding="utf8") as f:
    #f.write(res.text)
 #   f.write(soup.prettify()) # html 문서를 예쁘게 출력


for movie in movies:
    title = movie.find("div", attrs={"class":"Epkrse"}).get_text()
    print(title)