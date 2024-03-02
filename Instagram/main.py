import browser

bot = browser.Tarayici(kullanici_adi="kullanici_adi", sifre="sifre")
bot.giris_yap()
# bot.kullaniciyi_takip_et(hedef_kullanici="turkey_home")
bot.begeni_bombasi(hedef_kullanici="turkey_home")
# bot.foto_begen(link="")
# bot.foto_begenmeyi_birak(link="")
txt = input("Bekleme ...")
