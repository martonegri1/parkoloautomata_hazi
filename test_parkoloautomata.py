import unittest
from datetime import datetime
from parkoloautomata import OradijasJegy

class TestOradijasJegy(unittest.TestCase):
    def test_jegy(self):
        belepes = datetime(2026, 9, 30, 10,0)
        kilepes = datetime(2026, 9, 30, 11,0)
        jegy = OradijasJegy(1, "ABC-123", belepes, kilepes)
        self.assertEqual(jegy.ar_szamitasa(),500)