import unittest
from datetime import datetime
from parkoloautomata import OradijasJegy

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

