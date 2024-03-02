from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csvOlusturucu

class Tarayici:
    def __init__(self):
        self.tarayici = webdriver.Chrome()
        csvOlusturucu.CsvOlusturucu.csvOlustur(self)
        Tarayici.ImdbyeGit(self)

    def ImdbyeGit(self):
        self.tarayici.get("https://www.imdb.com/chart/top")
        Tarayici.FilmleriListele(self)

    def FilmleriListele(self):
        for i in range(1, 251, 1):
            film_adi = self.tarayici.find_element(By.XPATH,"//*[@id=\"main\"]/div/span/div/div/div[3]/table/tbody/tr["+str(i)+"]/td[2]/a").get_attribute("innerHTML")
            url = self.tarayici.find_element(By.XPATH,"//*[@id=\"main\"]/div/span/div/div/div[3]/table/tbody/tr["+str(i)+"]/td[2]/a")
            Tarayici.VeriyiAl(self, film_adi, url.get_attribute("href"))

    def VeriyiAl(self, film_adi, url):
        self.tarayici.get(url)
        veri = self.tarayici.find_element(By.XPATH,"//*[@id=\"titleStoryLine\"]/div[1]/p/span")
        csvOlusturucu.CsvOlusturucu.csvSatirYaz(self, film_aciklamasi=veri.get_attribute("innerHTML"), film_linki=url, film_adi=film_adi)
        self.tarayici.get("https://www.imdb.com/chart/top")
