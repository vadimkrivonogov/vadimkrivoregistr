from random import *


def Soorteerimine(inimesed, palgad):
    v = int(input("Palk 1-kahened,2-kasvad?"))
    if v == 1:
        n = len(palgad)
        for j in range(0, n - 1):
            for k in range(j + 1, n):
                if palgad[j] < palgad[k]:
                    abi = palgad[j]
                    palgad[j] = palgad[k]
                    palgad[k] = abi
                    abi = inimesed[j]
                    inimesed[j] = inimesed[k]
                    inimesed[k] = abi
    elif v == 2:
        n = len(palgad)
        for j in range(n - 1):
            for k in range(j + 1, n):
                if palgad[j] > palgad[k]:
                    abi = palgad[j]
                    palgad[j] = palgad[k]
                    palgad[k] = abi
                    abi = inimesed[j]
                    inimesed[j] = inimesed[k]
                    inimesed[k] = abi
    print("Имена работников", inimesed)
    print("Зарплаты работников:", palgad)


def Kustutamine(palgad: list, inimesed: list):
    nimi = input("sisesta nimi: ")
    if nimi in inimesed:
        n = inimesed.count(nimi)
        for j in range(n):
            ind = inimesed.index(nimi)
            inimesed.pop(ind)
            palgad.pop(ind)
    return inimesed, palgad


# 1-Добавить еще несколько человек и зарплат(кол-во говорит пользователь),
def uued_palgad(inimesed, palgad):
    nimi = input("Kirjuta nimi: ")
    palk = int(input("Kirjuta palk: "))
    palgad.append(palk)
    inimesed.append(nimi)
    return inimesed, palgad


# praktiline töö 10
def Keskmine(palgad, inimesed):
    keskminee = sum(palgad) / len(palgad)
    max_index = palgad.index(keskminee)
    nimi = inimesed[max_index]
    return keskminee, nimi


"""
def keskmine(palgad,inimesed):
    keskminee=sum(palgad)/len(palgad)
    ind=palgad.index(keskminee)
    nimi=inimesed[ind]  
    return keskminee
"""


# Registreerimine ja autoriseerimine
def kasutajaandmed(ll: list, p: list):
    """siin toimub registreerimine
    """
    print("Kas sa tahad oma andmet või random")
    a = input("Mida te soovite: ")
    if a == "oma":
        login = input("Kirjutage teie nimi: ")
    print("Kas sa tahad oma andmet või random")
    a = input("Mida te soovite: ")
    if a == "oma":
        login = input("Kirjutage teie nimi: ")
        psword = input("Kirjutage teie salasõna max 12 värtused: ")
        n = len(psword)
        while n < 12:
            psword = input("Teie salasõna on lühike. Palun kirjuta veel: ")
            n = len(psword)
    elif a == "random":
        login = input("Kirjutage teie nimi: ")
        str0 = ".,:;!_*-+()/#¤%&"
        str1 = '0123456789'
        str2 = 'qwertyuiopasdfghjklzxcvbnm'
        str3 = str2.upper()
        # print(str3) # 'QWERTYUIOPASDFGHJKLZXCVBNM'
        str4 = str0 + str1 + str2 + str3
        # print(str4)
        ls = list(str4)
        # print(ls)
        shuffle(ls)
        # print(ls)
        # Извлекаем из списка 12 произвольных значений
        psword = ''.join([choice(ls) for x in range(12)])
    ll.append(login)
    p.append(psword)
    return login, psword


def aut(ll: list, p: list):
    """siin on autoriseerimine
    """
    print("Kirjutage teie login j salasõna")
    logg = input("Login: ")
    pas_ = input("Salasõna: ")
    if logg in ll and pas_ in p:
        print("Tere tulemast!")
    else:
        print("Ebaõiged andmed")
    return logg, pas_


def uss_login(ll: list, vanamini: list, uusnimi: list):
    """Siin saab oma nimi kustutada.
    """
    if vanamini in ll:
        index = ll.index(vanamini)
        ll[index] = uusnimi
        print("Sinu nimi on muudetud.")
    else:
        print("Viga!")


def uss_salasõna(ll, p, login, vanasalasõna, uussalasõna):
    """Siin saab oma parooli kustutada.
    """
    if login in ll and vanasalasõna in p:
        index = ll.index(login)
        p[index] = uussalasõna
        print("salasõna on muudetud")
    else:
        print("Viga!")


def nimii(ll, p, nimiii):
    """Siin saab vaadata oma vana parooli.
    """
    if nimiii in ll:
        index = ll.index(nimiii)
        print(f"Teie vana salasõna on:", p[index])
    else:
        print("Viga!")

