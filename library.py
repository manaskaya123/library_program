# kütüphane programı
import sqlite3

baglanti = sqlite3.connect("kutuphane.db")  # kütüphane adında bir database oluşturduk.
komut = baglanti.cursor()  # komut değişkeni atıyoruz.

komut.execute(
    "create table if not exists kitaplik(kitapno INT, kitapadi TEXT,yazar TEXT, yayinevi TEXT,tur TEXT)")  # kitaplık tablosu oluştu.
baglanti.commit()  # tablo oluşturma tamamlandı.

komut.execute(
    "create table if not exists uyeler(uyeno INT, uyeadi TEXT,uyesoyadi TEXT,telefonno TEXT)")  # Üyeler tablosu oluştu.
baglanti.commit()  # tablo oluşturma tamamlandı.

komut.execute(
    "create table if not exists emanet(uyeno INT, kitapno INT,verilistarihi TEXT,teslimtarihi TEXT, aciklama TEXT)")  # Emanet tablosu oluştu.
baglanti.commit()  # tablo oluşturma tamamlandı.

while True:
    ######## KİTAP LİSTELEME FONKSİYONU  ###########
    def kitaplistele():  # listeleme fonksiyonu
        komut.execute("select * from kitaplik")  # kitaplıktaki tüm verileri seç
        kitaplistesi = komut.fetchall()  # seçilen verileri fetchall komutuyla kitaplistesi değişkenine atıyoruz.
        print("Kitap Listesi: ")
        for i in kitaplistesi:  # liste değişkeninin içindekileri ekrana yazdırıyoruz.
            print(i)


    ######### KİTAP EKLEME FONKSİYONU  ###############
    def kitapekle(kitapno, kitapadi, yazar, yayinevi, tur):
        komut.execute("insert into kitaplik values(@p1, @p2, @p3, @p4, @p5)", (kitapno, kitapadi, yazar, yayinevi, tur))
        baglanti.commit()  # kitap ekleme fonksiyonu tamamlandı.


    ######### KİTAP SİLME FONKSİYONU ######
    def kitapsil(kitapadi):  # kitapadına göre silsin.
        komut.execute("delete from kitaplik where kitapadi=@p1",
                      (kitapadi,))  # virgülün anlamı kitapadının bulunduğu listeyi sil
        # kitaplıktan kitap adına göre sil, (kitapadi,) virgüllü yazdık çünkü liste şeklinde bize lazım.
        baglanti.commit()  # silme fonksiyonu tamamlandı.


    def uyelistele():
        komut.execute("select * from uyeler")  # üyelerdeki tüm verileri seç
        uyelistesi = komut.fetchall()  # seçilen verileri fetchall komutuyla liste değişkenine atıyoruz.
        print("Üyelerin Listesi: ")
        for i in uyelistesi:  # üyelistesi değişkeninin içindekileri ekrana yazdırıyoruz.
            print(i)


    def uyeekle(uyeno, uyeadi, uyesoyadi, telefonno):
        komut.execute("insert into uyeler values(@p1, @p2, @p3, @p4)", (uyeno, uyeadi, uyesoyadi, telefonno))
        baglanti.commit()  # üye ekleme fonksiyonu tamamlandı.


    def uyesil(uyeadi):  # kitapadına göre silsin.
        komut.execute("delete from uyeler where uyeadi=@p1",
                      (uyeadi,))  # virgülün anlamı kitapadının bulunduğu listeyi sil


    def emanetlistele():
        komut.execute("select * from emanet")  # emanetteki tüm verileri seç
        emanetlistesi = komut.fetchall()  # seçilen verileri fetchall komutuyla liste değişkenine atıyoruz.
        print("Emanet Listesi: ")
        for i in emanetlistesi:  # emanetliste değişkeninin içindekileri ekrana yazdırıyoruz.
            print(i)


    def emanetekle(uyeno, kitapno, verilistarihi, teslimtarihi="boş", aciklama="boş"):
        komut.execute("insert into emanet values(@p1, @p2, @p3, @p4, @p5)",
                      (uyeno, kitapno, verilistarihi, teslimtarihi, aciklama))
        baglanti.commit()  # emanet ekleme fonksiyonu tamamlandı.


    def emanetsil(kitapno):  # kitap nosuna göre silsin.
        komut.execute("delete from emanet where kitapno=@p1",
                      (kitapno,))  # virgülün anlamı kitapadının bulunduğu listeyi sil


    print("""Kütüphaneye hoşgeldiniz.
   1-Kitap listele
   2-Kitap ekle
   3-Kitap sil
   4-Üye listele
   5-Üye ekle
   6-Üye sil
   7-Emanet listele
   8-Emanet ekle
   9-Emanet sil
   q-Çıkış """)

    secim = input("Seçiminizi yapınız:")
    if secim == "q":
        break

    elif secim == "1":
        kitaplistele()
    elif secim == "2":
        try:
            kitapno = int(input("Kitap no giriniz: "))
            kitapadi = input("Kitap adı giriniz: ")
            yazar = input("Yazar adı giriniz: ")
            yayinevi = input("Yayın evi adını giriniz: ")
            tur = input("Kitap türünü giriniz: ")
            kitapekle(kitapno, kitapadi, yazar, yayinevi, tur)
        except ValueError:
            print("tamsayı giriniz")

    elif secim == "3":
        kitapadi = input(("Silinecek kitap adını giriniz:"))
        kitapsil(kitapadi)
    elif secim == "4":
        uyelistele()
    # uyeno INT, uyeadi TEXT,uyesoyadi TEXT,telefonno TEXT)
    elif secim == "5":
        try:
            uyeno = int(input("Üye no giriniz: "))
            uyeadi = input("Üye adı giriniz: ")
            uyesoyadi = (input("Üye soyadı giriniz: "))
            telefonno = (input("telefon no giriniz: "))
            uyeekle(uyeno, uyeadi, uyesoyadi, telefonno)
        except ValueError:
            print("Tamsayı giriniz")
    elif secim == "6":
        uyeadi = input(("Silinecek üyenin adını giriniz:"))
        uyesil(uyeadi)

    elif secim == "7":
        emanetlistele()
    # uyeno INT, kitapno INT,verilistarihi TEXT,teslimtarihi TEXT, aciklama TEXT
    elif secim == "8":
        try:
            uyeno = int(input("Üye no giriniz: "))
            kitapno = int(input("Kitap no giriniz: "))
            verilistarihi = (input("Veriliş tarihini giriniz: "))
            teslimtarihi = input("Teslim tarihini giriniz: ")
            aciklama = input("Açıklama ekleyebilirsiniz.")
            emanetekle(uyeno, kitapno, verilistarihi, teslimtarihi, aciklama)
        except ValueError:
            print("Tamsayı giriniz.")

    elif secim == "9":
        try:
            kitapno = input(("Teslim edilen kitap nosunu giriniz:"))
            emanetsil(kitapno)
        except ValueError:
            print("Tamsayı giriniz.")

    elif secim != ("1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" or "q"):
        print("Yanlış tercih")
baglanti.close()