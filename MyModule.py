login_list=["alexa", "user1" ]
parool_list=["qweRt56>", "User1pass#" ]

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

def log(login: str) -> bool:
    """Kasutaja sisestab oma sisselogimise
    :param str login: Sisend kasutajalt 
    :rtype: bool tagastab tõeväärsuses formaadis tulemus
    """
    if login in login_list:
        v1=True
    else:
        v1=False
    return v1

def par(parool: str) -> bool:
    """Kasutaja sisestab oma salasõna
    :param str parool: Sisend kasutajalt 
    :rtype: bool tagastab tõeväärsuses formaadis tulemus
    """
    if parool in parool_list:
        v2=True
    else:
        v2=False
    return v2

def login_parool(login: str, parool: str) -> bool:
    """Kasutajanime ja sobiva parooli kontrollimine
    Kasutaja sisestab kasutajanime ja parooli
    :param str login: Sisend kasutajalt 
    :param str parool: Sisend kasutajalt
    :rtype: bool tagastab tõeväärsuses formaadis tulemus
    """
    if login in login_list:
        i = login_list.index(login)
        v3=parool_list[i] == parool
    else:
        v3=False
    return v3


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




