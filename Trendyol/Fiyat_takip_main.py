import Fiyat_takip_browser

link=input("Lütfen Ürün Linkini Giriniz: ")
count=int(input("Kontrol Tekrar Sayısını Giriniz: "))
time=int(input("Tekrar Sayısını Saniye Cinsinden Yazınız: "))

Fiyat_takip_browser=Fiyat_takip_browser.browser(time=time,count=count,link=link)