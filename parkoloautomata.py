from datetime import datetime
from math import ceil

class ParkoloJegy:
    def __init__(self, hely, rendszam, belepes_ido, kilepes_ido):
        self.hely = hely
        self.rendszam = rendszam
        self.belepes_ido = belepes_ido
        self.kilepes_ido = kilepes_ido

class OradijasJegy(ParkoloJegy):

    def ar_szamitasa(self):
        eltelt_ido = self.kilepes_ido - self.belepes_ido
        masodpercek = eltelt_ido.total_seconds()
        percek = masodpercek / 60
        orak = ceil(percek / 60)
        ar = 500 + (orak - 1) * 300
        if ar > 2500:
            ar = 2500
        return ar

class NapiJegy(ParkoloJegy):

    def ar_szamitasa(self):
        return 2500

def oradijas_jegy_bekerese():
    print("\n- - - Óradíjas jegy vásárlása - - -")
    print("-----------------------------------")
    hely = int(input("Add meg a parkolóhely számát: "))
    rendszam = input("Add meg a rendszámot (BBB-NNN): ")
    belepes = datetime.strptime(input("Add meg a belépési időpontot (ÉÉÉÉ-HH-NN ÓÓ:PP): "), "%Y-%m-%d %H:%M")
    kilepes = datetime.strptime(input("Add meg a kilépési időpontot (ÉÉÉÉ-HH-NN ÓÓ:PP:): "), "%Y-%m-%d %H:%M")

    jegy = OradijasJegy(hely, rendszam, belepes, kilepes)

    print("Rögzítés sikeres!")
    print("Jegy típusa: Óradíjas jegy")
    print(f"Parkolóhely száma: {jegy.hely}")
    print(f"Rendszám: {jegy.rendszam}")
    print(f"Belepes: {jegy.belepes_ido}")
    print(f"Kilepes: {jegy.kilepes_ido}")
    print(f"Fizetendő összeg: {jegy.ar_szamitasa()} Ft")
    return jegy



def main():
    while True:
        print("\n- - - PARKOLÁS KEZELŐ - - -")
        print("---------------------------")
        print()
        print("1 - Óradíjas jegy vásárlása")
        print("2 - Napijegy vásárlása")
        print("0 - Kilépés")

        jegy_tipus = input("\nVálassz: ")

        if jegy_tipus == "1":
            jegy = oradijas_jegy_bekerese()

        elif jegy_tipus == "2":
            NapiJegy.ar_szamitasa()

        elif jegy_tipus == "0":
            print("Kilépés...")
            break
main()
