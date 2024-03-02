class DosyaFonksiyonlari:

    def __init__(self, metin):
        self.metin = metin
        DosyaFonksiyonlari.dosyayaYaz(self)

    def dosyayaYaz(self):
        dosya = open("AmazonListe.txt", "a", encoding="utf-8")
        dosya.write(self.metin)
        dosya.close()
