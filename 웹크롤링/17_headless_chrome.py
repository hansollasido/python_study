from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless= True 
options.add_argument("window-size=1920x1080")

# 웹브라우져를 띄우지 않아도 데이터를 가져옴

browser = webdriver.Chrome(options=options)
#browser.maximize_window()

url= "https://play.google.com/store/search?q=%EC%9D%B8%EA%B8%B0%EC%98%81%ED%99%94&c=movies"
browser.get(url)


# 지정한 위치로 스크롤 내리기
# 모니터(해상도) 높이인 1080 위치로 스크롤 내리기
#browser.execute_script("window.scrollTo(0,2080)") # 1080은 해상도 정보

# 화면 가장 아래로 스크롤 내리기
#browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
import time
interval = 2 # 2초에 한번씩 스크롤을 내림

# 현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script("return document.body.scrollHeight")
# 반복 수행
while True:
    # 스크롤을 가장 아래로 내림
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    # 페이지 로딩 대기
    time.sleep(interval)
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height:
        break
    prev_height= curr_height

print("스크롤 완료")

# screenshot 강행
browser.get_screenshot_as_file("google_movie.png")

import requests
from bs4 import BeautifulSoup
# header 정보를 통해 구글에서는 제공하는 정보가 다름

# 스크롤 내릴 때마다 로딩이 되어 영화가 보여줌 -> 나머지 영화에 대해서는 보여주지 않음


#res = requests.get(url, headers=headers)
#res.raise_for_status()

soup = BeautifulSoup(browser.page_source,"lxml")

#list를 활용하여 element를 가져올 수 있음
movies = soup.find_all("div", attrs={"class":"VfPpkd-EScbFb-JIbuQc UVEnyf"})


print(len(movies))
#print(movies[0].prettify())


#with open("movie.html", "w", encoding="utf8") as f:
    #f.write(res.text)
 #   f.write(soup.prettify()) # html 문서를 예쁘게 출력


for movie in movies:
    title = movie.find("div", attrs={"class":"Epkrse"}).get_text()
    #print(title)

    original_price = movie.find("span", attrs={"class":"SUZt4c P8AFK"})
    if original_price:
        original_price = original_price.get_text()
    else:
        #print(title, "할인되지 않은 영화 제외")
        continue

    # 할인된 가격
    price = movie.find("span",attrs={"class":"VfPpfd VixbEe"}).get_text()
    link = movie.find("a", attrs={"class":"Si6A0c ZD8Cqc"})["href"]
    # https://play.google.com + link

    print(f"제목 : {title}")
    print(f"할인 전 금액 : {original_price}")
    print(f"할인 후 금액 : {price}")
    print("링크 : ", "https://play.google.com" + link)
    print("-"*100)