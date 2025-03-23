from math import fabs
from MyModule import *
import random
print("Tere tulemast!")
while 1:
        vastus=str(input("Kas olete registreeritud? ")).lower()
        if vastus=="jah" or vastus=="ei": break
        else:
            print("Ответ должен быть только да или нет!")
v=vas(vastus)
if v:
    while 1:
        login=str(input("Введите свой логин: "))
        if log(login): 
            break
        else:
          print("Seda kasutajanime ei ole nimekirjas!")
          login_list.append(login)
    while 1:
        parool=str(input("Введите свой пароль: "))
        if par(parool) and login_parool(login, parool): break
        else:
            print("Пароль не подходит!")
        parool_list.append(parool)
    print("Вы вошли в систему!")
else:
    while 1:
        login=str(input("Введите свой логин: "))
        if log(login): 
             print("See kasutajanimi on juba hõivatud, sisesta teine!")
        else: break
    login_list.append(login)
    while 1:
        vastus1=str(input("Сгенирировать пароль? ")).lower()
        if vastus=="jah" or vastus=="ei": break
        else:
            print("Ответ должен быть только да или нет!")
    v=vas2(vastus1)
    if v:
        str0=".,:;!_*-+()/#¤%&"
        str1 = '0123456789'
        str2 = 'qwertyuiopasdfghjklzxcvbnm'
        str3 = str2.upper()
        str4 = str0+str1+str2+str3
        ls = list(str4)
        password = ''.join([random.choice(ls) for x in range(8)])
        parool_list.append(password)
        print(f"Ваш пароль {password}")
        print("Вы зарегистрировались!")
    else:
        while 1:
            parool1=str(input("Введите свой пароль: "))
            if len(parool1)<8:
                vh=par1(parool1)
                parool_list.append(vh)
            else:
                print("Пароль должен состоять как минимум из 8 символов! ")
        print("Вы зарегистрированы")
       
