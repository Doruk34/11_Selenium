from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class Tarayici:
    def __init__(self,kullanici_adi,sifre,takip,mesaj):
        self.kullanici_adi=kullanici_adi
        self.sifre=sifre
        self.takip=takip
        self.mesaj=mesaj
        self.tarayici=webdriver.Chrome()
    
    def GirisYap(self):
        self.tarayici.get("https://www.facebook.com/?locale=tr_TR/")
        kullanici_adi_alani=self.tarayici.find_element(By.XPATH,'//*[@id="email"]')
        kullanici_adi_alani.send_keys(self.kullanici_adi)
        sifre_alani=self.tarayici.find_element(By.XPATH,'//*[@id="pass"]')
        sifre_alani.send_keys(self.sifre)
        sifre_alani.send_keys(Keys.RETURN)
        #giris_butonu=self.tarayici.find_element(By.XPATH,'//*[@id="loginbutton"]').click()
        time.sleep(5)
    

    def KullaniciTakipEt(self):
        self.tarayici.get("https://www.facebook.com/" + self.takip)
        time.sleep(5)
        arkadas_ekle=self.tarayici.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div/div[4]/div/div/div[1]/div/div/div/div[1]/div[2]/span/span')
        arkadas_ekle.click()
        delay = 3 # seconds
        #ekleme hatası için
        time.sleep(7)
        try:
            uyarı_tamam = WebDriverWait(self.tarayici, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="facebook"]/body/div[6]/div[1]/div/div[2]/div/div/div/div/div/div/div[3]/div/div/div/div/div/div/div/div[1]/div/span/span')))
            uyarı_tamam.click()
        except TimeoutException:
            print("Zaman Aşımı")
    
        # uyarı_tamam=self.tarayici.find_element(By.XPATH,'//*[@id="facebook"]/body/div[6]/div[1]/div/div[2]/div/div/div/div/div/div/div[3]/div/div/div/div/div/div/div/div[1]/div/span/span')
        # uyarı_tamam.click()
        time.sleep(2)
        try:
            mesaj_gonder = WebDriverWait(self.tarayici, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div[1]/div[4]/div/div/div[2]/div/div/div/div[1]/div[2]/span/span')))
            mesaj_gonder.click()
        except TimeoutException:
            print("Zaman Aşımı")
        # mesaj_gonder=self.tarayici.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div[1]/div[4]/div/div/div[2]/div/div/div/div[1]/div[2]/span/span')
        # mesaj_gonder.click()
        time.sleep(2)
        try:
            mesaj_icerik = WebDriverWait(self.tarayici, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[5]/div[1]/div[1]/div[1]/div/div/div/div/div/div/div/div[2]/div[2]/div/div/div[4]/div[2]/div/div/div[1]/p')))
            # mesaj_icerik.click()
            mesaj_icerik.send_keys(self.mesaj)
            mesaj_icerik.send_keys(Keys.RETURN)
        except TimeoutException:
            print("Zaman Aşımı")
        # mesaj_icerik=self.tarayici.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[5]/div[1]/div[1]/div[1]/div/div/div/div/div/div/div/div[2]/div[2]/div/div/div[4]/div[2]/div/div/div[1]/p')
        # mesaj_icerik.send_keys(self.mesaj)
        time.sleep(2)
        
     
        
        
    
            