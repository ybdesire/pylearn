# reference: https://www.cnblogs.com/lweiser/p/11045023.html
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait 

browser=webdriver.Chrome()

browser.implicitly_wait(10)

browser.get('http://www.95598.cn/member/login.shtml')

elem = browser.find_element_by_class_name("rank_acount_info")
elem.click()
elem = browser.find_element_by_id("account")
elem.send_keys("1234")
elem = browser.find_element_by_id("password")
elem.send_keys("1234")



#browser.close()