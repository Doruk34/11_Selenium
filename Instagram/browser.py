from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class Tarayici:
    def __init__(self, kullanici_adi, sifre):
        self.kullanici_adi = kullanici_adi
        self.sifre = sifre
        self.tarayici = webdriver.Chrome()
        self.giris_onay = False

    def giris_yap(self):
        self.tarayici.get("https://www.instagram.com/accounts/login/")
        kullanici_adi_alani = self.tarayici.find_element(By.NAME,"username")
        kullanici_adi_alani.send_keys(self.kullanici_adi)
        sifre_alani = self.tarayici.find_element(By.NAME,"password")
        sifre_alani.send_keys(self.sifre)
        sifre_alani.send_keys(Keys.ENTER)
        time.sleep(5)
        if self.tarayici.current_url != "https://www.instagram.com/accounts/login/":
            print("Giriş Başarılı olarak yapıldı ...")
            self.giris_onay = True
        else:
            print("Giriş yapılamadı")
        try:
            time.sleep(7)
            self.tarayici.find_element(By.XPATH,"/html/body/div[3]/div/div/div[3]/button[2]").click()
        except Exception as e:
            print(e)

    def kullaniciyi_takip_et(self, hedef_kullanici):
        if self.giris_onay == True:
            self.tarayici.get("https://www.instagram.com/" + hedef_kullanici)
            time.sleep(5)
            if self.tarayici.find_element(By.XPATH,"//*[@id=\"react-root\"]/section/main/div/header/section/div[1]/div[1]/span/span[1]/button").text == "Follow":
                self.tarayici.find_element(By.XPATH,"//*[@id=\"react-root\"]/section/main/div/header/section/div[1]/div[1]/span/span[1]/button").click()
                print("Takip edilen kullanıcı: " + hedef_kullanici)
            else:
                print("Kullanıcı takip edilemedi...")
        else:
            print("Giriş yapılamadı... Bu fonksiyonu çalıştıramıyorum...")

    def kullaniciyi_takipten_cik(self, hedef_kullanici):
        if self.giris_onay == True:
            self.tarayici.get("https://www.instagram.com/" + hedef_kullanici)
            time.sleep(5)
            if self.tarayici.find_element(By.XPATH,"//*[@id=\"react-root\"]/section/main/div/header/section/div[1]/div[1]/span/span[1]/button").text == "Following":
                self.tarayici.find_element(By.XPATH,"//*[@id=\"react-root\"]/section/main/div/header/section/div[1]/div[1]/span/span[1]/button").click()
                time.sleep(5)
                self.tarayici.find_element(By.XPATH,"/html/body/div[3]/div/div/div[3]/button[1]").click()
                print("Takipten vazgeçilen kullanıcı: " + hedef_kullanici)
            else:
                print("Kullanıcı takip edilmiyor...")
        else:
            print("Giriş yapılamadı... Bu fonksiyonu çalıştıramıyorum...")

    def foto_begen(self, link):
        if self.giris_onay == True:
            self.tarayici.get(link)
            try:
                begen_butonu = self.tarayici.find_element(By.XPATH,"//button[./span[@aria-label=\"Like\"]]").click()
                print("Fotoğraf beğenildi... Link:" + link)
            except Exception as e:
                print("Bu fotoğraf beğenilmiş...")

    def foto_begenmeyi_birak(self, link):
        if self.giris_onay == True:
            self.tarayici.get(link)
            try:
                begen_butonu = self.tarayici.find_element(By.XPATH,"//button[./span[@aria-label=\"Unlike\"]]").click()
                print("Fotoğraf beğenmekten vazgeçildi ... Link:" + link)
            except Exception as e:
                print("Bu fotoğraf beğenilmemiş...")

    def begeni_bombasi(self, hedef_kullanici):
        if self.giris_onay == True:
            self.tarayici.get("https://www.instagram.com/" + hedef_kullanici)
            self.sayfayi_asagi_yuvarla()
            liste = self.tarayici.find_elements(By.XPATH,"//div[contains(@class, 'v1Nh3 kIKUG  _bz0w')]/a")
            liste2 =[]
            for x in liste:
                liste2.append(x.get_attribute("href"))
                print("Listeye Eklendi: " + x.get_attribute("href"))
            for x in liste2:
                self.foto_begen(link=x)

    def sayfayi_asagi_yuvarla(self):
        BEKLEME_SURESI = 0.5

        # Sayfanın yüksekliğini al
        son_yukseklik = self.tarayici.execute_script("return document.body.scrollHeight")

        while True:
            # Sayfanın en altına in
            self.tarayici.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Sayfanın yüklenmesini bekle
            time.sleep(BEKLEME_SURESI)

            # Yeni sayfa yüksekliğini hesapla ve son sayfa yüksekliği ile karşılaştır
            yeni_yukseklik = self.tarayici.execute_script("return document.body.scrollHeight")
            if yeni_yukseklik == son_yukseklik:
                break
            son_yukseklik = yeni_yukseklik
