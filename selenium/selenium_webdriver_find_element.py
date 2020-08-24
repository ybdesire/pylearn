# reference: https://www.cnblogs.com/lweiser/p/11045023.html
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait 

browser=webdriver.Chrome()

browser.implicitly_wait(10)

browser.get('http://data.aiweibang.com/rank/account?t=1')


divs = browser.find_elements_by_xpath('//div[@class="numberPublic"]')
for d in divs:
    print(d.text)

browser.close()