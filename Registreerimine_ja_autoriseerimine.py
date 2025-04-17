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
            login = str(input("Sisesta oma kasutajanimi: "))
            if log(login):
                print("See kasutajanimi on juba hõivatud, sisesta teine!")
            else:
                break
        while True:
            vastus1 = str(input("Genereerida parool?: ")).lower()
            if vastus1 in vastus_list:
                break
            print("Vastus peab olema ainult 'jah' või 'ei'!")
        v1 = vas1(vastus1)
        if v1: 
            parool = uus_parool()
            print(f"Sinu parool: {parool}")
        else: 
                while True:
                    parool = str(input("Sisesta oma parool: "))
                    if check_parool(parool):
                        break
                    print("Parool peab olema vähemalt 8 tähemärki pikk ning sisaldama numbreid, väikeseid ja suuri tähti ning erimärke!")
        lisa_kasutaja(login, parool)
        print("Sa oled registreeritud!")
        while 1:
            vastus = str(input("Kas sa tahad sisse logida: ")).lower()
            if vastus in vastus_list and vastus=="jah":
                while True:
                    login = str(input("Sisesta oma kasutajanimi: "))
                    if log(login):
                        break
                    else:
                        print("Seda kasutajanime ei ole nimekirjas!")
                while 1:
                    parool = str(input("Sisesta oma parool: "))
                    if login_parool(login, parool):
                        print("Sa oled süsteemi sisse loginud!")
                    else:
                        print("Parool ei sobi!")
                        print("Proovi uuesti.")
            elif vastus in vastus_list and vastus=="ei":
                break
            else:
                print("Vastus peab olema ainult 'jah' või 'ei'!")
else: 
        while True:
            login = str(input("Sisesta oma kasutajanimi: "))
            if log("login_parool.txt", login):break
        while True:
            parool = str(input("Sisesta oma parool: "))
            if login_parool("login_parool.txt", login, parool):
                break
