from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import dosya
class Tarayici:
    def __init__(self, link):
        self.tarayici = webdriver.Chrome()
        self.link = link
        Tarayici.AmazonaGit(self)

    def AmazonaGit(self):
        self.tarayici.get(self.link)
        Tarayici.AmazonSayfaListesi(self)

    def AmazonSayfaListesi(self):
        urun_fiyatları = self.tarayici.find_element(By.CLASS_NAME,'a-offscreen')
        urun_isimleri = self.tarayici.find_elements(By.XPATH,"//h2[@data-attribute]")
        for i in range(0, len(urun_fiyatları), 1):
            metin = "{} - Ürünün İsmi: {} - Ürünün Fiyatı: {} \n".format(i+1, urun_isimleri[i].text, urun_fiyatları[i].get_attribute("innerHTML"))
            print(metin)
            dosya.DosyaFonksiyonlari(metin)
        self.tarayici.quit()
