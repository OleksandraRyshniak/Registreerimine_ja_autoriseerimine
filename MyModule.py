login_list=["gh"]
parool_list=["9"]
import random
def vas(vastus:str)->bool:
    """Kas olete registreeritud?
    Kasutaja siseneb kontole
    :param str vastus: Sisend kasutajalt on konto või soovid luua
    :rtype: bool tagastab tõeväärsuses formaadis tulemus
    """
    if vastus=="jah": 
        v=True
    else: 
        v=False
    return v

def log(login:str)->bool:
    """Kas süsteemis on sisselogimine?
    Kasutaja sisestab kasutajanime.
    :param str login: Sisend kasutajalt oma kasuutajanimi.
    :rtype: bool tagastab tõeväärsuses formaadis tulemus
    """
    if login in login_list:
        l=True
    else:
        l=False
    return l

def par(parool: str)->bool:
    """Kas süsteemis on parool?
    Kasutaja sisestab parooli
    :param str login: Kasutaja sisestab oma parooli.
    :rtype: bool tagastab tõeväärsuses formaadis tulemus
    """
    if parool in parool_list:
        p=True
    else:
        p=False
    return p 

def login_parool(login: str, parool:str)->bool:
    """
    """
    if login in login_list:
        i=login_list.index(login)
        parool_list[i]==parool
        lp=True
    else:
        lp=False
    return lp

def vas2(vastus1:str)->bool:
    """
    """
    if vastus1=="jah":
        v1=True
    else:
        v1=False
    return v1

def par1(parool1:str)-> str:
    """
    """
    str_list = list(".,:;!_*-+()/#¤%&")
    par_list=list(parool1)
    password_ = ""
    for i in parool1:
        if i.isupper() or i.isidigit() or i in str_list:
            password_+=i
        if 8 => len(password_):
            v0=True
        else:
            v0=False
        return v0






