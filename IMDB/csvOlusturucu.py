import csv

class CsvOlusturucu:
    def csvOlustur(self):
        with open('imdbtop250.csv', mode='a') as csv_dosya:
            alan_adlari = ['film_adi', 'film_aciklamasi', 'film_linki']
            yazici = csv.DictWriter(csv_dosya, fieldnames=alan_adlari)
            yazici.writeheader()
            csv_dosya.close()

    def csvSatirYaz(self, film_adi, film_aciklamasi, film_linki):
        with open('imdbtop250.csv', mode='a') as csv_dosya:
            alan_adlari = ['film_adi', 'film_aciklamasi', 'film_linki']
            yazici = csv.DictWriter(csv_dosya, fieldnames=alan_adlari)
            yazici.writerow({'film_adi': film_adi, 'film_aciklamasi': film_aciklamasi, 'film_linki': film_linki})
            csv_dosya.close()
