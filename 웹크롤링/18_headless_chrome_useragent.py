from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.81 Safari/537.36")
browser = webdriver.Chrome(options = options)
browser.maximize_window()
url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent"

browser.get(url)

# Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.81 Safari/537.36
detected_value = browser.find_element_by_id("detected_value")
print(detected_value.text)
browser.quit()
# 이렇게 해서 돌리면
# Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/98.0.4758.81 Safari/537.36
# headlessChrome으로 나와서 문제가 됨

# selenium with python에 서칭하면 자세히 나와있음 