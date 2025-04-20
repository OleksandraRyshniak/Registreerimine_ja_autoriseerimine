import random
import smtplib
from email.message import EmailMessage
import ssl
from tkinter import filedialog

def vas(vastus: str) -> bool:
    """Vastus ei või jah
    Kui kasutaja sisestab jah, tagastab funktsioon True
    Kui kasutaja sisestab ei, tagastab funktsioon False
    :param str vastus: Sisend kasutajalt 
    :rtype: bool tagastab tõeväärsuses formaadis tulemus
    """
    if vastus=="ei":
        v=True
    else:
        v=False
    return v

#REGISTREERIMINE
def log(fail:str, login: str) -> bool:
    """Kasutaja sisestab oma sisselogimise
    :param str login: Sisend kasutajalt 
    :rtype: bool tagastab tõeväärsuses formaadis tulemus
    """
    v1=False
    f=open (fail,'r', encoding="utf-8-sig")
    sonad=[]
    for rida in f:
        sonad.append(eval(rida.strip()))
    f.close()
    for kirje in sonad:
        if kirje['nimi'].lower() == login.lower():
            v1=True
    return v1

def email_(fail:str, email:str)->bool:
    """
    """
    v1=False
    f=open (fail,'r', encoding="utf-8-sig")
    sonad=[]
    for rida in f:
        sonad.append(eval(rida.strip()))
    f.close()
    for kirje in sonad:
        if kirje['email'].lower() == email.lower():
            v1=True
    return v1

def uus_parool1():
        """Uue salasõna genereerimine
        """
        symbols = ".,:;!_*-+()/#¤%&"
        numbers = "0123456789"
        sletters = "qwertyuiopasdfghjklzxcvbnm"
        bletters = sletters.upper()  
        kõik = symbols + numbers + sletters + bletters
        password_list=list(kõik)
        random.shuffle(password_list)
        uus_parool=""
        for i in range (8):
            uus_parool+=random.choice(password_list)
        return uus_parool

def check_parool1(parool:str):
    """Kasutaja sisestatud salasõna kontrollimine
    kasutaja sisestab salasõna
    :parem str parool: Sisend kasutajalt 
    :rtype: bool tagastab tõeväärsuses formaadis tulemus
    """
    symbols = ".,:;!_*-+()/#¤%&"
    ta_number=False
    ta_sletters=False
    ta_bletters=False
    ta_symbols=False
    for i in parool:
        if i.isdigit(): 
            ta_number = True
        if i.islower():  
            ta_sletters = True
        if i.isupper():  
            ta_bletters = True
        if i in symbols:  
            ta_symbols = True
    if len(parool)<8:
        return False
    if ta_number and ta_sletters and ta_sletters and ta_symbols:
        v5=True
    else:
        v5=False
    return v5

def vas1(vastus1: str) -> bool:
    """Vastus jah või ei
    Kui kasutaja sisestab jah, tagastab funktsioon True
    Kui kasutaja sisestab ei, tagastab funktsioon False
    :param str vastus: Sisend kasutajalt 
    :rtype: bool tagastab tõeväärsuses formaadis tulemus
    """
    if vastus1=="jah":
        v4=True
    else:
        v4=False
    return v4

def lisa_kasutaja(fail: str, uus_kasutaja:str):
    """Lisab nimekirjadesse sisselogimise ja parooli.
    Kasutaja sisestab kasutajanime ja parooli
    :param str login: Sisend kasutajalt 
    :param str parool: Sisend kasutajalt
    :rtype: bool tagastab tõeväärsuses formaadis tulemus
    """
    with open(fail, 'a', encoding="utf-8-sig") as fail:
        fail.write(str(uus_kasutaja)+'\n')
    print("Kasutaja on lisatud!")

def reg_message(login:str, email:str):
    """
    """
    kellele=email
    teema="Tere" + " " + login + "!"
    sisu=" "
    smtp_server='smtp.gmail.com'
    smtp_port=587
    kellelt="oleksandraryshniak@gmail.com"
    salasõna=input("Salasõna: ")
    msg=EmailMessage()
    msg['Subject']=teema
    msg['From']=kellelt
    msg['To']=kellele
    sisu="""
    <!DOCTYPE html>
    <head>
    </head>
        <body>
            <h2>Registreerimine</h2>
            <p>Sa oled sisse logitud!</p>
        </body>
    </html>
    """
    msg.set_content(sisu, subtype='html')
    try:
        with smtplib.SMTP(smtp_server,smtp_port) as server:
            server.starttls(context=ssl.create_default_context())
            server.login(kellelt,salasõna)
            server.send_message(msg)
        print("Kiri saadetud!")
    except Exception as e:
        print("Viga: ",e)


#AUTORISEERIMINE
def login_parool_email(fail:str, login:str, parool: str, email:str):
    """Kasutajanime ja sobiva parooli kontrollimine
    Kasutaja sisestab kasutajanime ja parooli
    :param str login: Sisend kasutajalt 
    :param str parool: Sisend kasutajalt
    :rtype: bool tagastab tõeväärsuses formaadis tulemus
    """
    f=open (fail,'r', encoding="utf-8-sig")
    sonad=[]
    for rida in f:
        sonad.append(eval(rida.strip()))
    f.close()
    for kirje in sonad:
        if kirje['nimi'] == login: break
    f=open (fail,'r', encoding="utf-8-sig")
    sonad=[]
    for rida in f:
        sonad.append(eval(rida.strip()))
    f.close()
    for kirje in sonad:
        if kirje['email'] == email: break
    f=open(fail, 'r', encoding="utf-8-sig")
    sonad = []
    for rida in f:
            sonad.append(eval(rida.strip()))
    f.close()
    for kirje in sonad:
        if kirje['parool'] == parool and kirje['nimi'] == login and kirje['email'] == email:
            print("Sa oled süsteemi sisse loginud!") 
            autoriseerimine(login, email)
            break
    else:
        print("Seda sõna ei ole sõnaraamatus!")
        while True:
            muuta=str(input("Kas soovite oma parooli muuta?")).strip().lower()
            if muuta=="jah":
                while 1:
                    v = str(input("Genereerida parool?: ")).lower().strip()
                    if v=="jah":
                        uus_parool("login_parool.txt", login, email)
                        muuta_message(login, email)
                        break
                    elif v=="ei":
                        while 1:
                            parool = str(input("Sisesta oma parool: "))
                            if check_parool("login_parool.txt", login, email,parool): 
                                muuta_message(login, email)
                                break
                            else:
                                print("Parool peab olema vähemalt 8 tähemärki pikk ning sisaldama numbreid, väikeseid ja suuri tähti ning erimärke!")
                        break
                    else:
                        print("Vastus peab olema ainult jah või ei!")
                break
            else:
                print("Sa ei ole sisse logitud proovi hiljem uuesti.")
                break

def uus_parool(fail:str, login:str,email:str ):
        """Uue salasõna genereerimine
        """
        symbols = ".,:;!_*-+()/#¤%&"
        numbers = "0123456789"
        sletters = "qwertyuiopasdfghjklzxcvbnm"
        bletters = sletters.upper()  
        kõik = symbols + numbers + sletters + bletters
        password_list=list(kõik)
        random.shuffle(password_list)
        uus_parool=""
        with open(fail, 'r', encoding="utf-8-sig") as f:
            sonad=[]
            for rida in f:
                sonad.append(eval(rida.strip()))
            indeks=-1
            i=0
            while i<len(sonad):
                kirje=sonad[i]
                if login in [kirje["nimi"]]:
                    indeks=i
                    break
                i+=1
        for m in range (8):
            uus_parool+=random.choice(password_list)
        sonad[i]={'nimi':login, 'parool': uus_parool, 'email': email}
        with open(fail, 'w', encoding="utf-8-sig") as f :
            for kirje in sonad:
                f.write(str(kirje)+'\n')
        print("Sõna on muudatud!")
        print(f"Sinu uus parool on: {uus_parool}")

def check_parool(fail:str, login:str,email:str, parool)->bool:
    """Kasutaja sisestatud salasõna kontrollimine
    kasutaja sisestab salasõna
    :parem str parool: Sisend kasutajalt 
    :rtype: bool tagastab tõeväärsuses formaadis tulemus
    """
    symbols = ".,:;!_*-+()/#¤%&"
    ta_number=False
    ta_sletters=False
    ta_bletters=False
    ta_symbols=False
    for i in parool:
        if i.isdigit(): 
            ta_number = True
        if i.islower():  
            ta_sletters = True
        if i.isupper():  
            ta_bletters = True
        if i in symbols:  
            ta_symbols = True
    if ta_number and ta_bletters and ta_sletters and ta_symbols and len(parool)>=8 :
        with open(fail, 'r', encoding="utf-8-sig") as f:
            sonad=[]
            for rida in f:
                sonad.append(eval(rida.strip()))
            indeks=-1
            i=0
            while i<len(sonad):
                kirje=sonad[i]
                if login in [kirje["nimi"]]:
                    indeks=i
                    break
                i+=1
        sonad[i]={'nimi':login, 'parool': parool, 'email': email}
        with open(fail, 'w', encoding="utf-8-sig") as f :
            for kirje in sonad:
                f.write(str(kirje)+'\n')
        print("Sõna on muudatud!")
        k=True
    else:
        k=False
    return k
        
def autoriseerimine(login:str, email:str):
    kellele=email
    teema="Tere" + " " + login + "!"
    sisu=" "
    smtp_server='smtp.gmail.com'
    smtp_port=587
    kellelt="oleksandraryshniak@gmail.com"
    salasõna=input("Salasõna: ")
    msg=EmailMessage()
    msg['Subject']=teema
    msg['From']=kellelt
    msg['To']=kellele
    sisu="""
    <!DOCTYPE html>
    <head>
    </head>
        <body>
            <h2>Autoriseerimine</h2>
            <p>Sa oled sisse loginud!</p>
        </body>
    </html>
    """
    msg.set_content(sisu, subtype='html')
    try:
        with smtplib.SMTP(smtp_server,smtp_port) as server:
            server.starttls(context=ssl.create_default_context())
            server.login(kellelt,salasõna)
            server.send_message(msg)
        print("Kiri saadetud!")
    except Exception as e:
        print("Viga: ",e)

def muuta_message(login:str, email:str):
    kellele=email
    teema="Tere" + " " + login + "!"
    sisu=" "
    smtp_server='smtp.gmail.com'
    smtp_port=587
    kellelt="oleksandraryshniak@gmail.com"
    salasõna=input("Salasõna: ")
    msg=EmailMessage()
    msg['Subject']=teema
    msg['From']=kellelt
    msg['To']=kellele
    sisu="""
    <!DOCTYPE html>
    <head>
    </head>
        <body>
            <h2>Autoriseerimine</h2>
            <p>Sa muutsid oma parooli</p>
        </body>
    </html>
    """
    msg.set_content(sisu, subtype='html')
    try:
        with smtplib.SMTP(smtp_server,smtp_port) as server:
            server.starttls(context=ssl.create_default_context())
            server.login(kellelt,salasõna)
            server.send_message(msg)
        print("Kiri saadetud!")
    except Exception as e:
        print("Viga: ",e)





