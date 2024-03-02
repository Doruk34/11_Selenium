"""
Link_Text = Aranan içeriğin tamamının uyuşması durumunda kullanılır.

Partial_Link_Text = Aranan içeriğin belirli bir bölümü uyuşuyor ise arama yapar.

"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://www.python.org/")
driver.find_element(By.PARTIAL_LINK_TEXT,"Succes").click()
time.sleep(5)
driver.find_element(By.LINK_TEXT,"Help").click()
time.sleep(5)
driver.close()