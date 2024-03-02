import main
import time

takip=input("Takip Edilmek İstenen Kişinin Kullanıcı Adını Yazınız: ")
mesaj_icerik=input("Mesajınızı Yazınız: ")


bot=main.Tarayici(kullanici_adi=".....@gmail.com",sifre="........)",takip=takip,mesaj=mesaj_icerik)
bot.GirisYap()

time.sleep(6)
bot.KullaniciTakipEt()
bekle=input("Beklemeeee")