import random
import string
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# WhatsApp Web oturumu aç
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")

# Kullanıcıdan WhatsApp'ı oturum açmasını isteyin
input("Lütfen WhatsApp Web'e oturum açın ve Enter tuşuna basın...")

# Sayfanın tamamen yüklenmesini bekleyin
wait = WebDriverWait(driver, 30)
wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")

# XPATH öğesini bulma işlemi için bekleme
try:
    wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="_3FRCZ copyable-text selectable-text"][@contenteditable="true"][@data-tab="3"]')))
except Exception as e:
    print(f"Sayfa yüklenirken hata oluştu: {str(e)}")
    driver.quit()
    exit()

def whatsapp_mesaji_gonder(telefon_numarasi, mesaj):
    try:
        # Belirtilen kişiyi ara
        arama_kutusu = driver.find_element_by_xpath('//div[@class="_3FRCZ copyable-text selectable-text"][@contenteditable="true"][@data-tab="3"]')
        arama_kutusu.clear()
        arama_kutusu.send_keys(telefon_numarasi)
        arama_kutusu.send_keys(Keys.ENTER)

        # Mesaj gönder
        time.sleep(2)  # Kullanıcı arama sonuçlarına odaklanmak için biraz daha bekleyin
        mesaj_kutusu = driver.find_element(By.XPATH,'//div[@class="_3uMse"][@contenteditable="true"][@data-tab="1"]')
        mesaj_kutusu.send_keys(mesaj)
        mesaj_kutusu.send_keys(Keys.ENTER)

        print(f"Mesaj '{mesaj}' {telefon_numarasi} numarasına gönderildi.")

    except Exception as e:
        print(f"Mesaj gönderme sırasında hata oluştu: {str(e)}")

# İlk mesajı gönderdikten sonra otomatik devam etmesi için döngüyü başlat
while True:
    try:
        # Telefon numarasını kullanıcıdan alın
        telefon_numarasi = input("Mesaj göndermek istediğiniz telefon numarasını girin: ")

        # Rastgele bir mesaj oluştur
        rastgele_mesaj = ''.join(random.choices(string.ascii_letters + string.digits, k=10))

        whatsapp_mesaji_gonder(telefon_numarasi, rastgele_mesaj)
        time.sleep(3)  # Bir sonraki mesajı göndermeden önce 3 saniye bekleyin

    except KeyboardInterrupt:
        print("İşlem kullanıcı tarafından sonlandırıldı.")
        break
