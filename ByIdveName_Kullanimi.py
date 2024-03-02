from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time 

driver = webdriver.Chrome()
driver.get("https://www.python.org/")
arama_bolumu = driver.find_element(By.ID,"id-search-field") # Id üzerinden arama yapar.
arama_bolumu.send_keys("İlk Deneme")
# buton=driver.find_element(By.ID,"submit").click() # Butona bul tıkla
arama_bolumu.send_keys(Keys.RETURN)
time.sleep(5)

arama_bolumu = driver.find_element(By.ID,"id-search-field") # Id üzerinden arama yapar.
arama_bolumu.clear()
time.sleep(2)

driver.get("https://www.python.org/")
arama_bolumu2 = driver.find_element(By.NAME,"q") # Name üzerinden arama yapar.
arama_bolumu2.send_keys("İkinci Deneme")
# arama_bolumu2.send_keys(Keys.RETURN) # Enter yap
time.sleep(2)
buton = driver.find_element(By.ID,"submit").click() # Butonu bul tıkla

time.sleep(2)
driver.quit()
