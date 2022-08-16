import requests
res=requests.get("https://google.com")
#res=requests.get("https://nadocoding.tistory.com")

print("응답코드 : ",res.status_code) # 200 이면 정상 # 200아니면 권한이 없어 웹 스크래핑 할 수 없음

if res.status_code == requests.codes.ok:
    print("정상입니다.")
else :
    print("문제가 생겼습니다. [에러코드 ", res.status_code, "]")

res.raise_for_status() # raise_for_status는 문제가 생기면 바로 에러를 출력
print("웹 스크래핑을 진행합니다.")

print(len(res.text))
print(res.text)

with open("mygoogle.html", "w", encoding="utf-8") as f:
    f.write(res.text)
# 파일로 만들 수 있음
