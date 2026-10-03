import unittest
from datetime import datetime

from Modul_23.parkoloautomata_hazi.parkoloautomata import oradijas_jegy_bekerese, napidijas_jegy_bekerese
from parkoloautomata import OradijasJegy, NapiJegy
from unittest.mock import patch

class TestOradijasJegy(unittest.TestCase):
    def test_jegy(self):
        belepes = datetime(2026, 9, 30, 10,0)
        kilepes = datetime(2026, 9, 30, 11,0)
        jegy = OradijasJegy(1, "ABC-123", belepes, kilepes)
        self.assertEqual(jegy.ar_szamitasa(),500)

    def test_egy_perc(self):
        belepes = datetime(2026, 9, 30, 10,0)
        kilepes = datetime(2026, 9, 30, 10,1)
        jegy = OradijasJegy(1, "ABC-123", belepes, kilepes)
        self.assertEqual(jegy.ar_szamitasa(),500)

    def test_nyolc_es_fel_ora(self):
        belepes = datetime(2026, 9, 30, 10,0)
        kilepes = datetime(2026, 9, 30, 18,30)
        jegy = OradijasJegy(1, "ABC-123", belepes, kilepes)
        self.assertEqual(jegy.ar_szamitasa(),2500)

    def test_egy_es_negyed_ora(self):
        belepes = datetime(2026, 9, 30, 10,0)
        kilepes = datetime(2026, 9, 30, 11,15)
        jegy = OradijasJegy(1, "ABC-123", belepes, kilepes)
        self.assertEqual(jegy.ar_szamitasa(),800)

    def test_het_ora(self):
        belepes = datetime(2026, 9, 30, 10,0)
        kilepes = datetime(2026, 9, 30, 17,0)
        jegy = OradijasJegy(1, "ABC-123", belepes, kilepes)
        self.assertEqual(jegy.ar_szamitasa(),2300)

    def test_nyolc_ora(self):
        belepes = datetime(2026, 9, 30, 10,0)
        kilepes = datetime(2026, 9, 30, 18,0)
        jegy = OradijasJegy(1, "ABC-123", belepes, kilepes)
        self.assertEqual(jegy.ar_szamitasa(),2500)

class TestNapiJegy(unittest.TestCase):

    def test_egy_ora(self):
        belepes = datetime(2026, 9, 30, 10,0)
        kilepes = datetime(2026, 9, 30, 11,0)
        jegy = NapiJegy(1, "ABC-123", belepes, kilepes)
        self.assertEqual(jegy.ar_szamitasa(),2500)

    def test_huszonnegy_ora_alatt(self):
        belepes = datetime(2026, 9, 30, 10,0)
        kilepes = datetime(2026, 10, 1, 9,59)
        jegy = NapiJegy(1, "ABC-123", belepes, kilepes)
        self.assertEqual(jegy.ar_szamitasa(),2500)

    def test_pontosan_huszonnegy_ora(self):
        belepes = datetime(2026, 9, 30, 10, 0)
        kilepes = datetime(2026, 10, 1, 10, 0)
        jegy = NapiJegy(1, "ABC-123", belepes, kilepes)
        self.assertEqual(jegy.ar_szamitasa(), 2500)

    def test_ket_nap(self):
        belepes = datetime(2026, 9, 30, 10, 0)
        kilepes = datetime(2026, 10, 2, 10, 0)
        jegy = NapiJegy(1, "ABC-123", belepes, kilepes)
        self.assertEqual(jegy.ar_szamitasa(), 2500)

    def test_parkolohely(self):
        belepes = datetime(2026, 9, 30, 10, 0)
        kilepes = datetime(2026, 10, 2, 10, 0)
        jegy = NapiJegy(25, "ABC-123", belepes, kilepes)
        self.assertEqual(jegy.hely, 25)

    def test_rendszam(self):
        belepes = datetime(2026, 9, 30, 10, 0)
        kilepes = datetime(2026, 10, 2, 10, 0)
        jegy = NapiJegy(25, "ABC-123", belepes, kilepes)
        self.assertEqual(jegy.rendszam, "ABC-123")

class TestBemenet(unittest.TestCase):
    def test_oradijas_jegy_bekerese(self):
        with patch("builtins.input", side_effect=["25", "ABC-123", "2026-09-30 10:00", "2026-09-30 11:00"]):
            jegy = oradijas_jegy_bekerese()
            self.assertEqual(jegy.hely, 25)
            self.assertEqual(jegy.rendszam, "ABC-123")
            self.assertEqual(jegy.belepes_ido, datetime(2026, 9, 30, 10, 0))
            self.assertEqual(jegy.kilepes_ido, datetime(2026, 9, 30, 11, 0))

    def test_napidijas_jegy_bekerese(self):
        with patch("builtins.input", side_effect=["25", "ABC-123", "2026-09-30 10:00", "2026-09-30 11:00"]):
            jegy = napidijas_jegy_bekerese()
            self.assertEqual(jegy.hely, 25)
            self.assertEqual(jegy.rendszam, "ABC-123")
            self.assertEqual(jegy.belepes_ido, datetime(2026, 9, 30, 10, 0))
            self.assertEqual(jegy.kilepes_ido, datetime(2026, 9, 30, 19, 0))