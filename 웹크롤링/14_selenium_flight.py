from selenium import webdriver
from selenium.webdriver.common.by import By # 기다리는데 필요하 import 함수들
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()

#browser.maximize_window() # 창 최대화

url = "https://m-flight.naver.com/"
browser.get(url)

# 가는 날 선택 클릭
browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]").click()

# 이번달 27일, 28일 선택
#browser.find_elements_by_link_text('27')[0].click() # [0] -> 이번달
#browser.find_elements_by_link_text('28')[0].click() # [0] -> 이번달

# xpath로 하기 
elem = browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[10]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[4]/td[6]/button")
#browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[10]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[4]/td[3]/button").click()
print(elem.text)

# Xpath가 나올때까지 기다려 달라는 것임
# browser를 최대 10초까지 기다림
try : 
    elem = WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((By.XPATH,""))) # 어떤 element가 나올 때까지 기다림
    # 성공했을 때 동작 수행
    print(elem.text)
finally: # 실패 했을 때는 브라우져를 끔
    browser.quit()


