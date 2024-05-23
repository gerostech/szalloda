

# Szállodai szobafoglaló alkalmazás

Általános elvárások
Pythonban készítsétek a vizsgafeladatot
Csináljatok egy "adatok.txt"-t, amiben töltsétek ki a neveteket, szakotokat és neptun kódotokat
Kész projektet osszátok meg a saját github repositorytokba PUBLIC-ra és a repository URL-jét kell emailben elküldeni a boga.aron@gde.hu címre.
Határidő: 2024.05.10.
Hogy biztos legyen, az elküldés előtt tegyétek meg a következőket:
egy browser incognito ablakában nézzétek meg az elküldendő github repositoryt (látható, fent van az utolsó commit is)
ezt a repositoryt clone-ozzátok ki Pycharmban, és nézzétek meg, hogy futtatható-e (én is így fogom csinálni, el kell tudjon indulni, hogy tudjam értékelni)

A feladat során egy egyszerű szálloda szobafoglalási rendszert kell megvalósítani Pythonban. A rendszernek képesnek kell lennie szobák kezelésére,
foglalások kezelésére, létrehozására és lemondására, valamint a foglalások listázására.

A Feladat:

Osztályok Létrehozása

Hozz létre egy Szoba absztrakt osztályt, amely alapvető attribútumokat definiál (ár, szobaszám). (5 pont)
Hozz létre az Szoba osztályból EgyagyasSzoba és KetagyasSzoba származtatott osztályokat, amelyek különböző attributumai vannak, és az áruk is különböző.(5 pont)
Hozz létre egy Szalloda osztályt, ami ezekből a Szobákból áll, és van saját attributuma is (név pl.) (10 pont)
Hozz létre egy Foglalás osztályt, amelybe a Szálloda szobáinak foglalását tároljuk (elég itt, ha egy foglalás csak egy napra szól) (10 pont)

Foglalások Kezelése

Implementálj egy metódust, ami lehetővé teszi szobák foglalását dátum alapján, visszaadja annak árát. (15 pont)
Implementálj egy metódust, ami lehetővé teszi a foglalás lemondását. (5 pont)
Implementálj egy metódust, ami listázza az összes foglalást. (5 pont)

Felhasználói Interfész és adatvalidáció

Készíts egy egyszerű felhasználói interfészt, ahol a felhasználó kiválaszthatja a kívánt műveletet (pl. foglalás, lemondás, listázás). (20 pont)
A foglalás létrehozásakor ellenőrizd, hogy a dátum érvényes (jövőbeni) és a szoba elérhető-e akkor. (10 pont)
Biztosítsd, hogy a lemondások csak létező foglalásokra lehetségesek. (5 pont)
Töltsd fel az futtatás után a rendszert 1 szállodával, 3 szobával és 5 foglalással, mielőtt a felhasználói adatbekérés megjelenik. (10 pont)”
