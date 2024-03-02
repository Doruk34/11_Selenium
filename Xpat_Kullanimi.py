from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# ChromeDriver'ı yükleme
webdriver_service = Service(ChromeDriverManager().install())

# Web sürücüyü başlatma
surucu = webdriver.Chrome(service = webdriver_service)
# driver_path = r"chromedriver.exe"
# surucu = webdriver.Chrome(driver_path)
surucu.get("https://www.python.org/")
arama = surucu.find_element(By.XPATH,"//*[@id=\"id-search-field\"]")
arama.send_keys("Merhaba Dünya")
# arama.send_keys(Keys.RETURN)
buton = surucu.find_element(By.XPATH,'//*[@id="submit"]').click() # Butonu bul tıkla
time.sleep(2)
surucu.close()
