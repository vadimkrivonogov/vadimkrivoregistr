from Module import *
palgad=[1200,1200,1200,1200,1200]
inimesed=["A","B","C","D","E"]
print(Kustutamine(palgad,inimesed))

#1-Добавить еще несколько человек и зарплат,
palgad=[1200,2500,750,395,1200]
inimesed=["A","B","C","D","E"]
print(uued_palgad(inimesed, palgad))

#10-Keskmine() - Среднюю зарплату и человека
palgad=[1200,1200,1200,1200,1200]
inimesed=["A","B","C","D","E"]
print(Keskmine(palgad,inimesed))

#регистрация и авторизация
ll=[]
p=[]
while True:
    print("Registreerimine - 1")
    print("autoriseerimine - 2")
    print("Välja - 3")
    print("muuta kasutajanime - 4")
    print("muuta salasõna - 5")
    print("Kui sa tahad vadata teie salasõna - 6")
    valik=input("Kirjuta number, mis teeb su tegevuse: ")
    if valik=="1":
         print("Registreerimine")
         login,psword=kasutajaandmed(ll,p)
         print(f"Teie login ({login}) ja password ({psword})")
    elif valik=="2":
        print("autoriseerimine")
        logg,pas_=aut(ll,p)
    elif valik=="3":
        print("Nägemist")
        break
    elif valik=="4":
        vananimi=input("Kirjuta teie vana nimi: ")
        uusnimi=input("Kirjuta uue nimi, mida sa sooid: ")
        uss_login(ll,vananimi,uusnimi)
    elif valik=="5":
        login=input("Krjuta teie login: ")
        vanasalasõna=input("Kirjuta teie vana salasõna: ")
        uussalasõna=input("Kirjuta uus salasõna: ")
        uss_salasõna(ll,p,login,vanasalasõna,uussalasõna)
    elif valik=="6":
        nimiii=input("Kirjuta teie login, kellel sa tahad vadata salasõna: ")
        nimii(ll,p,nimiii)
    print(ll,p)
