from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.page_load_strategy = 'eager'
# chrome_options.add_argument("--proxy-server=http://202.20.16.82:10152")

count = 1
while True:
    # for i in range(0, 2000):

    driver = webdriver.Chrome(
        executable_path='D:\GitHub\Spanish-university-majors-information-crawler\source\web\chromedriver.exe', options=chrome_options)

    driver.get('https://www.toutoupiao.com/Vote/58943?PageIndex=2')

    time.sleep(2)
    driver.find_element("id", "445847").click()
    print(time.strftime('%H:%M:%S', time.localtime()))
    print(count)
    count += 1
    time.sleep(2)
    driver.quit()
    time.sleep(1)
