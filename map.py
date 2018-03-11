from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
from time import sleep

cords = open("final_cords.txt").read()
url = "https://www.darrinward.com/lat-long/"	
driver = webdriver.Chrome()
driver.get(url)
text = driver.find_element_by_id("geos")
text.clear()
text.send_keys(cords)
text.submit()
sleep(100)
driver.quit()