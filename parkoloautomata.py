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