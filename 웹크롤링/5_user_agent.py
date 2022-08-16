import requests
url = "https://nadocoding.tistory.com"

headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"}
# User-Agent가 없으면 가끔가다 안돌아가짐

res=requests.get(url,  headers = headers)

res.raise_for_status() # raise_for_status는 문제가 생기면 바로 에러를 출력

with open("nadocoding.html", "w", encoding="utf-8") as f:
    f.write(res.text)
# 파일로 만들 수 있음
