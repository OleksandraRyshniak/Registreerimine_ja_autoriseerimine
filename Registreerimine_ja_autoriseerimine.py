from MyModule import *
import random
vastus_list=["jah","ei"]
print("Tere tulemast!")
while True:
    vastus = str(input("Kas olete registreeritud?: ")).lower()
    if vastus in vastus_list:
        break
    print("Vastus peab olema ainult 'jah' või 'ei'!")
v = vas(vastus)
if v:
        while True:
            login = str(input("Sisesta oma kasutajanimi: ")).strip()
            if log("login_parool.txt",login):
                print("See kasutajanimi on juba hõivatud, sisesta teine!")
            else:
                break
        while True:
            email=str(input("Sisesta oma email: ")).strip()
            if email_("login_parool.txt",email):
                print("See email on juba hõivatud, sisesta teine!")
            else:
                break
        while True:
            vastus1 = str(input("Genereerida parool?: ")).lower()
            if vastus1 in vastus_list:
                break
            print("Vastus peab olema ainult 'jah' või 'ei'!")
        v1 = vas1(vastus1)
        if v1: 
            parool = uus_parool1()
            print(f"Sinu parool: {parool}")
        else: 
            while True:
                parool = str(input("Sisesta oma parool: ")).strip()
                if check_parool1(parool):
                    break
                print("Parool peab olema vähemalt 8 tähemärki pikk ning sisaldama numbreid, väikeseid ja suuri tähti ning erimärke!")
        uus_kasutaja={'nimi': login, 'parool': parool, 'email': email}
        lisa_kasutaja("login_parool.txt", uus_kasutaja)
        print("Sa oled registreeritud!")
        reg_message(login, email)
else: 
    while True:
        login = str(input("Sisesta oma kasutajanimi: ")).strip()
        if login.isalpha():break
        else:
            print("Vastus peab olema ainult tihti!")
    email=str(input("Sisesta oma email: ")).strip()
    parool = str(input("Sisesta oma parool: ")).strip()
    login_parool_email("login_parool.txt", login, parool, email)
        