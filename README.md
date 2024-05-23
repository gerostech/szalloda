

# Szállodai szobafoglaló alkalmazás

Általános elvárások<br />
Pythonban készítsétek a vizsgafeladatot<br />
Csináljatok egy "adatok.txt"-t, amiben töltsétek ki a neveteket, szakotokat és neptun kódotokat<br />
Kész projektet osszátok meg a saját github repositorytokba PUBLIC-ra és a repository URL-jét kell emailben elküldeni a boga.aron@gde.hu címre.<br />
Határidő: 2024.05.10.<br />
Hogy biztos legyen, az elküldés előtt tegyétek meg a következőket:<br />
egy browser incognito ablakában nézzétek meg az elküldendő github repositoryt (látható, fent van az utolsó commit is)<br />
ezt a repositoryt clone-ozzátok ki Pycharmban, és nézzétek meg, hogy futtatható-e (én is így fogom csinálni, el kell tudjon indulni, hogy tudjam értékelni)<br />
<br />
A feladat során egy egyszerű szálloda szobafoglalási rendszert kell megvalósítani Pythonban. A rendszernek képesnek kell lennie szobák kezelésére,
foglalások kezelésére, létrehozására és lemondására, valamint a foglalások listázására.<br />
<br />
A Feladat:<br />

Osztályok Létrehozása

Hozz létre egy Szoba absztrakt osztályt, amely alapvető attribútumokat definiál (ár, szobaszám). (5 pont)<br />
Hozz létre az Szoba osztályból EgyagyasSzoba és KetagyasSzoba származtatott osztályokat, amelyek különböző attributumai vannak, és az áruk is különböző.(5 pont)<br />
Hozz létre egy Szalloda osztályt, ami ezekből a Szobákból áll, és van saját attributuma is (név pl.) (10 pont)<br />
Hozz létre egy Foglalás osztályt, amelybe a Szálloda szobáinak foglalását tároljuk (elég itt, ha egy foglalás csak egy napra szól) (10 pont)<br />

Foglalások Kezelése

Implementálj egy metódust, ami lehetővé teszi szobák foglalását dátum alapján, visszaadja annak árát. (15 pont)<br />
Implementálj egy metódust, ami lehetővé teszi a foglalás lemondását. (5 pont)<br />
Implementálj egy metódust, ami listázza az összes foglalást. (5 pont)<br />

Felhasználói Interfész és adatvalidáció

Készíts egy egyszerű felhasználói interfészt, ahol a felhasználó kiválaszthatja a kívánt műveletet (pl. foglalás, lemondás, listázás). (20 pont)<br />
A foglalás létrehozásakor ellenőrizd, hogy a dátum érvényes (jövőbeni) és a szoba elérhető-e akkor. (10 pont)<br />
Biztosítsd, hogy a lemondások csak létező foglalásokra lehetségesek. (5 pont)<br />
Töltsd fel az futtatás után a rendszert 1 szállodával, 3 szobával és 5 foglalással, mielőtt a felhasználói adatbekérés megjelenik. (10 pont)<br />
