from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Webdriver'ı başlat
driver = webdriver.Chrome()

# Python.org sitesine git
driver.get("https://www.python.org/")

# ID ile arama bölümünü bul ve yazı gönder
arama_bolumu = driver.find_element(By.ID, "id-search-field")
arama_bolumu.send_keys("İlk Deneme")
arama_bolumu.send_keys(Keys.RETURN)

# Implicit Wait kullanarak 5 saniye bekleyin
time.sleep(5)

# Sayfayı tekrar yükleyin
driver.get("https://www.python.org/")

# ID ile arama bölümünü tekrar bul ve temizle
arama_bolumu = driver.find_element(By.ID, "id-search-field")
arama_bolumu.clear()

# Name ile arama bölümünü bul, temizleyin ve yazı gönder
arama_bolumu2 = driver.find_element(By.NAME, "q")
arama_bolumu2.send_keys("İkinci Deneme")
arama_bolumu2.send_keys(Keys.RETURN)

# Explicit Wait kullanarak 2 saniye bekleyin
wait = WebDriverWait(driver, 2)
wait.until(EC.visibility_of_element_located((By.ID, "id-search-field")))

# Kullanıcıya sonuçları görmesi için 5 saniye bekleyin
time.sleep(5)

# Webdriver'ı kapat
driver.quit()
