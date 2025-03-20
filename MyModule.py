def vastus(login:str)->bool:
    """Kasutaja on registreeritud või registreerimata
    Kasutaja siseneb kontole, 
    peate sisselogimiseks sisestama oma kasutajatunnuse ja parooli.
    Kasutaja siseneb , soovid luua peab sisestama sisselogimise ja parooli.
    (parooli võib sisestada ise või arvuti genereerib selle)
    :param str login: Sisend kasutajalt on konto või soovid luua
    :rtype: bool tagastab tõeväärsuses formaadis tulemus
    """
    if login=="on konto": 
        v=True
    else: 
        v=False
    return vastus(v)


