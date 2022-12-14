import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=675554"
res = requests.get(url)
res.raise_for_status()


soup = BeautifulSoup(res.text,"lxml") 

#cartoons = soup.find_all("td", attrs={"class":"title"})
#title = cartoons[0].a.get_text() # 모든 제목에 해당하는 정보를 찍을 수 있게 됨
#link = cartoons[0].a["href"]
#print(title)
#print("https://comic.naver.com"+link)
# terminal에서 ctrl+왼쪽클릭 하면 바로 링크로 갈 수 있음


# 만화 제목 + 링크 구하기
#for cartoon in cartoons:
    #title = cartoon.a.get_text()
    #link = "https://comic.naver.com"+cartoon.a["href"]
    #print(title, link)


# 평점 구하기
total_rates = 0
cartoons = soup.find_all("div", attrs={"class":"rating_type"})
for cartoon in cartoons:
    rate = cartoon.find("strong").get_text()
    print(rate)
    total_rates += float(rate)

print("전체 점수 : ", total_rates)
print('평균 점수 : ', total_rates / len(cartoons))