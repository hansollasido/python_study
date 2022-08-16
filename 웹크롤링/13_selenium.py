# 인터넷에 chrome://version 입력하면 chrome 버젼을 알 수 있음
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

browser = webdriver.Chrome() # 현재 폴더에 있는 chromedriver
# 같은 경로에 있으면 ""안에 값 안넣어도 됨

# 1. 네이버 이동
browser.get("https://www.naver.com/")

# 2. 로그인 버튼 클릭
elem = browser.find_element_by_class_name("link_login")
elem.click()

# 3. id, pw 입력
browser.find_element_by_id("id").send_keys("naver_id")
browser.find_element_by_id("pw").send_keys("password")

time.sleep(3)

# 4. 로그인 버튼 클릭
browser.find_element_by_id("log.login").click()

# 5. id를 새로 입력
#browser.find_element_by_id("id").send_keys("my_id")
browser.find_element_by_id("id").clear()
browser.find_element_by_id("id").send_keys("my_id")

# 6. html 정보 출력
print(browser.page_source)

# 7. 브라우저 종료
#browser.close() # 현재 탭만 종료
browser.quit() # 브라우져 종료

#>>> elem = browser.find_element_by_class_name("link_login")
#elem.click()
##>>> browser.back()
#>>> browser.forward()
#>>> browser.refresh()
#>>> browser.back()
#>>> elem = browser.find_element_by_id("query")

#>>> from selenium.webdriver.common.keys import Keys # Keys를 받아감
#>>> elem.send_keys("나도코딩")  # 나도 코딩을 친 것과 같이 입력됨
#>>> elem.send_keys(Keys.ENTER) # ENTER을 누른 것과 같이 됨
#>>> elem = browser.find_element_by_tag_name("a")
#>>> elem = browser.find_elements_by_tag_name("a")

#>>> for e in elem:
#...     e.get_attribute("href")    

#>>> browser.get("http://daum.net")
#>>> elem = browser.find_element_by_name("q")
#>>> elem

# xpath를 통해서 click() 하면 됨
#>>> elem = browser.find_element_by_xpath("//*[@id='nx_search_form']/fieldset/button/i") 
#>>> elem.click() 
# browser.quit()를 하면 브라우져를 닫음