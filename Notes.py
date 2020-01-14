#!/usr/bin/env python3
#Sondan istenilen satırı silmek - Delete the line you want from the end
def del_ask(line):
    if line == "all":
        file_1 = open('Notes.txt', 'w')
        file_1.close()
        print("All Deleted Successfully!")
    else:
        liste = []
        file_1 = open('Notes.txt', 'r')
        liste = file_1.readlines()
        file_1.close()
        line = int(line)
        del liste[-line:]
        file_1 = open('Notes.txt', 'w')
        for i in liste:
            file_1.write(i)
        file_1.close()

#Burdaki end_madde_del() fonksiyonu; Notes.txt dosyasına eklenen son maddeyi silmeye yarıyor (SON SATIRI-END LİNE DELETE)
def end_madde_del():
    books = open('Notes.txt', 'r')
    liste = []
    liste = books.readlines()
    del liste[-1]
    books = open('Notes.txt', 'w')
    for i in liste:
        books.write(i)
    books.close()

#numara ile alfabetik sıralaması- numerical and alphabetical order ;
def order_num():
    books = open('Notes.txt','r')
    num = 0
    liste = []
    liste = sorted(books.readlines())
    for i in liste :
        if i == '\n':
            continue
        num+=1
        print(num,i)
#Kullanıcı için bilgilendirici bir not- MENU;
menu = """
----------------------------------------------------------
|  DELETE ==> Deleting previous data                     |
|  READ ==> Notes.	                                     |
|  exit ==> Exit    	                                 |
|  menu ==> Again see command                            |
|  order ==> Data becomes numeric and alphabetical.      |
|  belirt ==> Delete the line you want from the end      |
----------------------------------------------------------
"""
print(menu)
while True:
    girdi = input('===> ')
    if len(girdi) == 0:
        print('Please do not go blank !')
        continue
    elif girdi == 'exit':
        print("Exiting...")
        break
    elif girdi == "menu":
        print(menu)
        continue
    elif girdi == 'READ' or girdi == 'read':
        books = open('Notes.txt', 'r')
        print(books.read())
        books.seek(0)
        books.close()
    elif girdi == "belirt":
        line = input("Delete the line you want from the end ('all' for all delete and 'exit' for exit) : ")
        if type(line) == str() and line != "all" and line != "exit" or bool(line) == False:
            print("Not understood")

        elif line == "exit":
            print("Exiting...")
            continue
        else:
            del_ask(line)

    elif girdi == 'DELETE' or girdi == 'delete':
        end_madde_del()
        print("Deleting.")
    elif girdi == "order":
        order_num()

    else:
        books = open('Notes.txt', 'a')
        books.write('\n'+girdi)
        books.close()
