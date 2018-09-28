#!/usr/bin/env python
#-*-coding:utf-8-*-

class Admin:

    global menu_listesi
    menu_listesi = []
    menu_adi = "menu"

    def yeni_liste_olustur(menu_ad):
        dosya = open("C:/Users/user/Documents/Python/"+menu_ad+".txt", "w")
        print(menu_ad+".txt oluşturuldu...\n")
        dosya.close()

    def menu_ekle(menu_adi,fiyat):
        dosya = open("C:/Users/user/Documents/Python/menu.txt", "a")
        dosya.write("\n"+menu_adi.upper()+" "+str(fiyat))
        dosya.flush()
        dosya.close()
        print("menu ekleme tamam")


    def menu_listesi_getir(menu_adi,liste):
        dosya = open("C:/Users/user/Documents/Python/menu.txt", "r")
        index = 0
        for i in dosya:
            print(i+"\n")

    def menu_sil(menu_ad,menu_listesi):
        menu_listesi = []
        dosya = open("C:/Users/user/Documents/Python/menu.txt", "r")
        index = 0
        for i in dosya:
            print(str(index + 1) + " " + i + "\n")
            menu_listesi.append(i)
            index += 1
        sil_secim = int(input("silmek istediğiniz menüyü seçiniz : "))
        menu_listesi.pop(sil_secim - 1)
        print(menu_listesi)
        dosya.close()
        dosya = open("C:/Users/user/Documents/Python/menu.txt", "w")
        for i in menu_listesi:
            dosya.write(i)
        dosya.flush()
        dosya = open("C:/Users/user/Documents/Python/menu.txt", "r")
        print(dosya)
        dosya.close()


    def menu_guncelle():
        menu_listesi = []
        fiyat_listesi = []
        dosya = open("C:/Users/user/Documents/Python/menu.txt", "r")
        index = 0
        for i in dosya:
            print(str(index + 1) + " " + i + "\n")
            bol = i.split()
            menu_listesi.append(bol[0])
            fiyat_listesi.append(bol[1])
            index += 1
        dosya.close()
        guncellenecek_menu = int(input("Guncellemek istediğiniz menüyü seçiniz : "))
        fiyat = int(input("Guncellemek istediğiniz menü fiyatını giriniz : "))
        fiyat_listesi[guncellenecek_menu-1] = fiyat
        dosya = open("C:/Users/user/Documents/Python/menu.txt", "w")
        index = 0
        for i in menu_listesi:
            dosya.write(str(i)+" "+str(fiyat_listesi[index])+"\n")
            index +=1
        dosya.flush()
        dosya = open("C:/Users/user/Documents/Python/menu.txt", "r")
        print(dosya)
        dosya.close()
        print("menu guncellendi.")



    while(True):
        print("Hoşgeldiniz...\nLütfen bir seçim yapınız...\n"
              "1.Anamenü \n"
              "2.Menü Ekle\n"
              "3.Menü Sil \n"
              "4.Fiyat Güncelle \n"
              "5.Çıkış\n")
        #yeni_liste_olustur(menu_adi)
        secim = int(input("Bir seçim yapınız >> _"))
        if(secim==1):
            print("\n")
            menu_listesi_getir(menu_adi,menu_listesi)
            print("\n")
        elif(secim==2):
            menu_isim = str(input("Menü Adı Giriniz : "))
            menu_fiyat = int(input("Menü Fiyatı Giriniz : "))
            menu_ekle(menu_isim,menu_fiyat)
        elif(secim==4):
            menu_sil("menu",menu_listesi)
        elif(secim==5):
            menu_guncelle()
        else:
            print("Çıkış Yapıldı...\nHoşçakalın")
            break
            #exit(0)
