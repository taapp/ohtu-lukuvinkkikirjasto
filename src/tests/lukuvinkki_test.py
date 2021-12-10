import unittest

from entities.lukuvinkki import Lukuvinkki

class TestLukuvinkki(unittest.TestCase):
    def setUp(self):
        self.lukuvinkki = Lukuvinkki(self, "kirja", "Yön Timo", "Taneli Mäkelä",)

    def test_lukuvinkin_merkitseminen_luetuksi_toimii(self):
        self.lukuvinkki.merkitse_luetuksi()
        self.assertEqual(self.lukuvinkki.luettu, True)

    def test_lukuvinkki_luettu_tila_aluksi_oikein(self):
        self.assertEqual(self.lukuvinkki.luettu, False)