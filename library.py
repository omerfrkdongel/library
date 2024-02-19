import sys

class Kitap:
    def __init__(self, isim, yazar, sayfa_sayisi):
        self.isim = isim
        self.yazar = yazar
        self.sayfa_sayisi = sayfa_sayisi

class Kutuphane:
    def __init__(self):
        self.kitaplar = []

    def kitap_ekle(self, kitap):
        self.kitaplar.append(kitap)
        print("Kitap kütüphaneye eklendi.")

    def kitap_listele(self):
        if not self.kitaplar:
            print("Kütüphane şu anda boş.")
        else:
            print("Kütüphanedeki Kitaplar:")
            for index, kitap in enumerate(self.kitaplar, 1):
                print(f"{index}. Kitap: {kitap.isim} - Yazar: {kitap.yazar} - Sayfa Sayısı: {kitap.sayfa_sayisi}")

def main():
    kutuphane = Kutuphane()

    while True:
        print("\nKütüphane Uygulaması")
        print("1. Kitap Ekle")
        print("2. Kitapları Listele")
        print("3. Çıkış")

        secim = input("Seçiminizi yapın: ")

        if secim == "1":
            isim = input("Kitap İsmi: ")
            yazar = input("Kitap Yazarı: ")
            sayfa_sayisi = input("Kitap Sayfa Sayısı: ")

            kitap = Kitap(isim, yazar, sayfa_sayisi)
            kutuphane.kitap_ekle(kitap)
        elif secim == "2":
            kutuphane.kitap_listele()
        elif secim.lower() == "q" or secim.lower() == "3":
            print("Programdan çıkılıyor...")
            sys.exit()
        else:
            print("Geçersiz bir seçim yaptınız. Lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()