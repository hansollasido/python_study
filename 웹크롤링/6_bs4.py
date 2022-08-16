import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/index"
res = requests.get(url)
res.raise_for_status()


soup = BeautifulSoup(res.text,"lxml") # res.text를 lxml통해서 beautiful soup 객체로 만듦

#print(soup.title)
#print(soup.title.get_text()) # text만 가져옴
#print(soup.a) # soup 객체에서 처음 발견되는 a 객체르 반환
#print(soup.a.attrs) # attrs는 속성임
#print(soup.a["href"]) 
#print(soup.find("a",attrs={"class":"Nbtn_upload"})) # 찾을 수 있음
#class = "Nbtn_upload"인 a element 를 찾아줘
#print(soup.find(attrs={"class":"Nbtn_upload"})) # class="Nbtn_upload"인 어떤 element를 찾아줘

#print(soup.find("li",  attrs={"class":"rank01"}))
rank1 = soup.find("li",  attrs={"class":"rank01"})
#print(rank1.a.get_text())
print(rank1.next_sibling.next_sibling) # 형제 노드 
#rank2 = rank1.next_sibling.next_sibling
#rank3 = rank2.next_sibling.next_sibling
#print(rank3.a.get_text())
#rank2 = rank3.previous_sibling.previous_sibling
#print(rank2.a.get_text())

#print(rank1.parent) # 부모 노드

#rank2 = rank1.find_next_sibling("li") # 형제 노드 중에서 다음항목이 li인 것만 반환
#print(rank2.a.get_text())
#rank3 = rank2.find_next_sibling("li") 
#print(rank3.a.get_text()) 

#print(rank1.find_next_siblings("li")) # li 형제 노드들을 가져옴

webtoon = soup.find("a", text="화산귀환-46화")
print(webtoon)