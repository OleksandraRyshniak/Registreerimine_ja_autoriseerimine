import random

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
            print("Sisselogimine sobib.")
            v1=True
    print("Sellist sisselogimist ei ole")
    return v1


def par(fail:str,login:str, parool: str) -> bool:
    """Kasutaja sisestab oma salasõna
    :param str parool: Sisend kasutajalt 
    :rtype: bool tagastab tõeväärsuses formaadis tulemus
    """
    with open (fail,'r', encoding="utf-8-sig") as f:
        sonad=[]
    for rida in f:
            sonad.append(eval(rida.strip()))
    for kirje in sonad:
        if kirje['parool'].lower==parool.lower():
            v2=True
        else:
            v2=False
    return v2

def login_parool(fail:str, login:str, parool: str) -> any:
    """Kasutajanime ja sobiva parooli kontrollimine
    Kasutaja sisestab kasutajanime ja parooli
    :param str login: Sisend kasutajalt 
    :param str parool: Sisend kasutajalt
    :rtype: bool tagastab tõeväärsuses formaadis tulemus
    """
    h=("Seda sõna ei ole sõnaraamatus!")
    f=open(fail, 'r', encoding="utf-8-sig")
    sonad = []
    for rida in f:
            sonad.append(eval(rida.strip()))
    f.close()
    for kirje in sonad:
        if kirje['parool'].lower() == parool.lower() and kirje['nimi'].lower() == login.lower():
            h=("Sa oled süsteemi sisse loginud!") 
    return h


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

def uus_parool():
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

def check_parool(parool):
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

def lisa_kasutaja(login: str, parool: str):
    """Lisab nimekirjadesse sisselogimise ja parooli.
    Kasutaja sisestab kasutajanime ja parooli
    :param str login: Sisend kasutajalt 
    :param str parool: Sisend kasutajalt
    :rtype: bool tagastab tõeväärsuses formaadis tulemus
    """
    login_list.append(login)
    parool_list.append(parool)




