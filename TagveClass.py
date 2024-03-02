from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import test

"""
<html>
<body>
<h1> Hoşgeldin </h1>
</body>
</html>
"""

driver = webdriver.Chrome()
driver.get("file:///C:/Users/..............html")
baslik = driver.find_elements(By.TAG_NAME,"h1")

for e in baslik:
    print(e.text)

icerik = driver.find_elements(By.CLASS_NAME,"icerik")
for a in icerik:
    print(a.text)


