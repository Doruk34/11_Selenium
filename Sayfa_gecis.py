from selenium import webdriver
import time
surucu = webdriver.Chrome()
url = "https://www.toyota.com.tr/"
surucu.get(url)
print(surucu.title)

if "Toyota Modellerini Keşfedin | Toyota Türkiye" in surucu.title:
    surucu.save_screenshot("ekran1.png")
    print("İşlem Başarılı")
else:
    print("Aranılan İçerik Bulunamadı")

surucu.get("https://www.toyota.com.tr/ikinci-el")
surucu.forward()
surucu.back()

time.sleep(3)