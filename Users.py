#!/usr/bin/env python
#-*-coding:utf-8-*-

class Users:

    def menu_ekle(m,f):
        dosya = open("C:/Users/user/Documents/Python/menu.txt", "a")
        dosya.write("\n"+m+" "+str(f))
        dosya.flush()
        dosya.close()

    def menu_listesi_getir():
        menu_listesi = {}
        dosya = open("C:/Users/user/Documents/Python/menu.txt", "r")
        index = 0
        for i in dosya:
            bol = i.split()
            menu_listesi[bol[0]] = bol[1]
            print((index+1),". ",str(i))
            index = index + 1
        print("\nÇıkış Yapmak İçin 0 seçiniz...")
        print("---------------------------------------")

    def menu_secim_fiyat(secimim):
        menu_listesi = {0:"Fiyat"}
        dosya = open("C:/Users/user/Documents/Python/menu.txt", "r")
        index = 1
        for i in dosya:
            bol = i.split()
            menu_listesi[index] = bol[1]
            index = index+1
        return int(menu_listesi[secimim])

    def menu_secim(secimim):
        menu_listesi = {0:"Menü"}
        dosya = open("C:/Users/user/Documents/Python/menu.txt", "r")
        index = 1
        for i in dosya:
            bol = i.split()
            menu_listesi[index] = bol[0]
            index = index+1
        return str(menu_listesi[secimim])

    def secim_menu_listem(listem):
        for i in listem:
            print(str(i)+" TL")

    print("Hoşgeldiniz...\nLütfen menü seçiniz...\n")

    toplam = 0
    secim_listem = {"Menü":"Fiyat"}
    while(True):
        print("-- Menü Listesi -- \n")
        menu_listesi_getir()
        secim = int(input("Menü numarası >> _"))
        if (secim==0):
            print(secim_listem)
            secim_menu_listem(secim_listem)
            exit()
        else:
            fiyat = menu_secim_fiyat(secim)
            toplam = toplam + int(fiyat)
            secim_listem[menu_secim(secim)] = fiyat
            print("Toplam : ",str(toplam))

