from selenium import webdriver
import time

surucu = webdriver.Chrome()
url = "https://www.toyota.com.tr/"

surucu.get(url)

print(surucu.title)

surucu.minimize_window() # Ekranı simgeler yani küçük ekran yapar.
surucu.maximize_window() # Ekranı full screen yapar.

surucu.save_screenshot("ekran.png")

# input("Program sonlandırmak için Enter tuşuna basın.") # Ekranda veri girilene kadar bekletir.

