from selenium import *
from selenium import webdriver

# 1) get 

"""
Ulaşılmak istenen web sitesinin adresi yazılır.

driver.get()

driver.get("https://www.toyota.com.tr/")

"""
# 2) title
"""
Web sitesinin başlığını görmek için. 
"""

# 3) back
"""
Sayfalar arası geçişte kullanılır.
"""

# 4) refresh
"""
sayfa yenileme
"""
# 5) close
"""
sekme kapatma
"""
# 6) quit
"""
Tarayıcı kapatma
"""

# Pencere boyutlandırma

# 1) maximize_window = Açılan pencereyi tam boyut yapar
""" # driver.maximize_window() """

#2)set_window_size = Açılan pencereyi boyutlandırmanı sağlar.
""" # driver.set_window_size(800,600) """

# 3) save_screenshot = Açılan pencerenin ekran görüntüsünü alır.
"""
# driver.save_screenshot("a.png")
# driver.save_screenshot("C:/Users/........./Desktop")"""