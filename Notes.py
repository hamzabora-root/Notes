#!/usr/bin/env python3
#Sondan istenilen satırı silmek
def del_ask(satir):
    if satir == "all":
        file_1 = open('Notes.txt', 'w')
        file_1.close()
        print("Hepsi Başarı ile Silindi")
    else:
        liste = []
        file_1 = open('Notes.txt', 'r')
        liste = file_1.readlines()
        file_1.close()
        satir = int(satir)
        del liste[-satir:]
        file_1 = open('Notes.txt', 'w')
        for i in liste:
            file_1.write(i)
        file_1.close()

#Burdaki end_madde_del() fonksiyonu; books.txt dosyasına eklenen son maddeyi silmeye yarıyor (SON SATIRI)
def end_madde_del():
    books = open('Notes.txt', 'r')
    liste = []
    liste = books.readlines()
    del liste[-1]
    books = open('Notes.txt', 'w')
    for i in liste:
        books.write(i)
    books.close()

#numara ile alfabetik sıralaması ;
def sirala():
    books = open('Notes.txt','r')
    num = 0
    liste = []
    liste = sorted(books.readlines())
    for i in liste :
        num+=1
        print(num,i)
#Kullanıcı için bilgilendirici bir not;
notlar = """
----------------------------------------------------------
|  DELETE ==> Bir önceki yanlış girdiğiniz girdiyi siler.|
|  READ ==> Kayıtlı girdilerinizi gösterir.	         |
|  exit ==> Çıkış.		                         |
|  menu ==> Tekrar komutları görmek için.                |
|  sırala ==> Verileri Alfabetik ve numaralı yapar.      |
|  belirt ==> İstenilen son satırı siler                 |
----------------------------------------------------------
"""
print(notlar)
while True:
    girdi = input('===> ')
    if len(girdi) == 0:
        print('Boş geçmeyiniz.')
        continue
    elif girdi == 'exit':
        print("Çıkılıyor...")
        break
    elif girdi == "menu":
        print(notlar)
        continue
    elif girdi == 'READ' or girdi == 'read':
        books = open('Notes.txt', 'r')
        print(books.read())
        books.seek(0)
        books.close()
    elif girdi == "belirt":
        satir = input("Sondan Kaçıncı Satır Belirtiniz(hepsini silmek için 'all' ve Çıkmak için 'exit') : ")
        if type(satir) == str() and satir != "all" and satir != "exit" or bool(satir) == False:
            print("Yanlış Girdi veya Boş geçtiniz")

        elif satir == "exit":
            print("Çıkılıyor...")
            continue
        else:
            del_ask(satir)

    elif girdi == 'DELETE' or girdi == 'delete':
        end_madde_del()
        print("Silindi.")
    elif girdi == "sırala":
        sirala()

    else:
        books = open('Notes.txt', 'a')
        books.write('\n'+girdi)
        books.close()