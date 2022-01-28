import unittest
from CourseWork.RegAndAuth.shiphr import encrypt, decrypt


class ShiphrTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_encr1(self):
        result = encrypt('Привет, мир! Как дела?', 'хорошо')
        self.assertEqual('2ящрэА)НэчЗ%ФЩрщЧтъър^', result)

    def test_encr2(self):
        result = decrypt('2ящрэА)НэчЗ%ФЩрщЧтъър^','хорошо')
        self.assertEqual('Привет, мир! Как дела?', result)

    def test_encr3(self):
        result = encrypt('Я хочу пиццы. Вот мой номер +79996189231', 'хорошо')
        self.assertEqual('(НЕэОБФющДНИ_НТэЙНБэъНЕэБуАНл:</]+];<*_&', result)

    def test_encr4(self):
        result = decrypt('(НЕэОБФющДНИ_НТэЙНБэъНЕэБуАНл:</]+];<*_&', 'хорошо')
        self.assertEqual('Я хочу пиццы. Вот мой номер +79996189231', result)

    def test_encr5(self):
        result = encrypt('', 'key')
        self.assertEqual('Error', result)

    def test_encr6(self):
        result = encrypt('Hello world!!!!', '')
        self.assertEqual('Error', result)

    def test_encr7(self):
        result = encrypt('', '')
        self.assertEqual('Error', result)

    def test_encr8(self):
        result = decrypt('', '')
        self.assertEqual('Error', result)
