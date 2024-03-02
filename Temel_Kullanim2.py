from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

surucu = webdriver.Chrome() # Chrome açar
surucu.get("https://www.python.org/") # Belirtilen siteye gider
assert "Python" in surucu.title 
# element = surucu.find_element_by_name() # Eskiden böyle kullanılıyordu
element = surucu.find_element(By.NAME,"q") # Yeni kullanımı arama butunonu bulma
element.send_keys("Python") # Arama bölümüne Python yaz
time.sleep(3) # 3 saniye bekle
element.send_keys(Keys.RETURN) # Enter
# element.clear() # Arama bölümünün içini temizler.
time.sleep(3) # 3 saniye bekle
surucu.close() # Tarayıcıyı tamamen kapat

