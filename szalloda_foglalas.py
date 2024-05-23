from datetime import datetime

# Osztályok Létrehozása

class Szoba:
    def __init__(self, szobaszam, ar):
        self.szobaszam = szobaszam
        self.ar = ar

class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam, bath):
        super().__init__(szobaszam, 70000)
        self.bath = bath

class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam, extra):
        super().__init__(szobaszam, 90000)
        self.extra = extra

class Foglalas:
    def __init__(self, szoba, datum):
        self.szoba = szoba
        self.datum = datum

class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []
        self.fgs_ok = []

# Foglalások Kezelése

    def add_szoba(self, szoba):
        self.szobak.append(szoba)

    # def fgs(self, szobaszam, datum):
    #     for szoba in self.szobak:
    #         if szoba.szobaszam == szobaszam:
    #             fgs = Foglalas(szoba, datum)
    #             self.fgs_ok.append(fgs)
    #             return szoba.ar
    #     return None
    
    def fgs(self, szobaszam, datum):
        for fgs in self.fgs_ok:
            if fgs.szoba.szobaszam == szobaszam and fgs.datum == datum:
                print("\nA szoba már foglalt ezen a napon. \nVálasszon másik szobát vagy másik dátumot!")
                return
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                self.fgs_ok.append(Foglalas(szoba, datum))
                print("Sikeres foglalás!")
                return szoba.ar
        print("\nA megadott szobaszám nem létezik a szállodában.")

    def lmond(self, szobaszam, datum):
        for fgs in self.fgs_ok:
            if fgs.szoba.szobaszam == szobaszam and fgs.datum == datum:
                self.fgs_ok.remove(fgs)
                return True
        return False
    
    def list_fgs_ok(self):
        for fgs in self.fgs_ok:
            print(f"Szoba: {fgs.szoba.szobaszam}, Időpont: {fgs.datum.strftime('%Y-%m-%d')}")

    def ment_foglalasok(self):
        with open("foglalasok.txt", "w") as f:
            for foglalas in self.fgs_ok:
                f.write(f"{foglalas.szoba.szobaszam};"
                        f"{foglalas.datum.strftime('%Y')};"
                        f"{foglalas.datum.strftime('%m')};"
                        f"{foglalas.datum.strftime('%d')}\n")

# Szalloda létrehozása
hotel = Szalloda("GDE Hotel")

# Szobák hozzáadása
hotel.add_szoba(EgyagyasSzoba("101","Kád"))
hotel.add_szoba(EgyagyasSzoba("102","Zuhany"))
hotel.add_szoba(KetagyasSzoba("201","Jacuzzi"))
hotel.add_szoba(KetagyasSzoba("202","Panoramás kilátás"))

try:
  with open('foglalasok.txt') as input_file:
    for line in input_file:
       # Rendszer feltöltés: Foglalások hozzáadása
       hotel.fgs(line.split(";")[0], datetime(int(line.split(";")[1]), int(line.split(";")[2]), int(line.split(";")[3])))

except:
  print('Hiba a file olvasásakor!')
  exit(1)



# Felhasználói interfész
while True:

    print("\nVálassz műveletet:")
    print("1. Szoba foglalása")
    print("2. Foglalás lemondása")
    print("3. Foglalások listázása")
    print("4. Szobák listázása")
    print("5. Kilépés")
    case = input("Művelet kiválasztása (1/2/3/4/5): ")

    if case == "1":
        szobaszam = input("\nAdd meg a foglalandó szoba számát: ")
        datum = input("Add meg a foglalás dátumát (ÉÉÉÉ-HH-NN, jelenleg csak egy napra lehetséges a foglalás): ")
        try:
            datum = datetime.strptime(datum, "%Y-%m-%d")
            if datum < datetime.now():
                print("\nHibás dátum! A foglalás csak jövőbeni időpontra lehetséges.")
            else:
                ar = hotel.fgs(szobaszam, datum)
                if ar:
                    print(f"A foglalás sikeres! Az ár: {ar} Ft")
                else:
                    print("\nHibás szobaszám!")
        except ValueError:
            print("\nHibás dátum formátum!")
        hotel.ment_foglalasok()
    elif case == "2":
        szobaszam = input("\nAdd meg a lemondandó foglalás szoba számát: ")
        datum = input("Add meg a lemondandó foglalás dátumát (ÉÉÉÉ-HH-NN): ")
        try:
            datum = datetime.strptime(datum, "%Y-%m-%d")
            siker = hotel.lmond(szobaszam, datum)
            if siker:
                print("\nA foglalás sikeresen lemondva.")
            else:
                print("\nNincs ilyen foglalás.")
            hotel.ment_foglalasok()
        except ValueError:
            print("\nHibás dátum formátum!")
    elif case == "3":
        hotel.list_fgs_ok()
    elif case == "4":
            print("Szobák száma:")
            print(len(hotel.szobak))
            print("Egyágyas szobák:")
            for szoba in hotel.szobak:
                if isinstance(szoba, EgyagyasSzoba):
                    print(f"Szobaszám: {szoba.szobaszam}, Ár: {szoba.ar} Ft, (Fürdő: {szoba.bath})")
            print("\nKétágyas szobák:")
            for szoba in hotel.szobak:
                if isinstance(szoba, KetagyasSzoba):
                    print(f"Szobaszám: {szoba.szobaszam}, Ár: {szoba.ar} Ft, (Extra: {szoba.extra})")
    elif case == "5":
        break
    else:
        print("\nHibás választás!")