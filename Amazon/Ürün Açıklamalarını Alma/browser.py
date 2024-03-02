from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import dosya

class Tarayici:
    def __init__(self, baglanti):
        surucu_yolu = "chromedriver"
        self.tarayici = webdriver.Chrome(surucu_yolu)
        self.baglanti = baglanti
        Tarayici.AmazonaGit(self)

    def AmazonaGit(self):
        self.tarayici.get(self.baglanti)
        Tarayici.AmazonSayfaListesi(self)

    def AmazonSayfaListesi(self):
        urun_isimleri = self.tarayici.find_elements(By.XPATH,"//h2[@data-attribute]")
        baglanti_listesi = []
        baslik = []
        for i in range(0, len(urun_isimleri), 1):
            urun_aciklama_baglantisi = self.tarayici.find_element(By.XPATH,"//a[@title=\"{}\"]".format(urun_isimleri[i].text))
            baglanti_listesi.append(urun_aciklama_baglantisi.get_attribute("href"))
            baslik.append(urun_isimleri[i].text)
        for i in range(0, len(urun_isimleri), 1):
            self.tarayici.get(baglanti_listesi[i])
            aciklama = self.tarayici.find_element(By.ID,'feature-bullets').text
            metin = ("\n\nBaşlık: {} \n-------------------------Açıklama-------------------------\n{}\n\n").format(baslik[i], aciklama)
            print(metin)
            dosya.DosyaFonksiyonlari(metin)
        self.tarayici.quit()
