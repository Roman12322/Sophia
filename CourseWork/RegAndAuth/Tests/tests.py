import unittest
from CourseWork.RegAndAuth.shiphr import msg_and_key, create_vigenere_table, create_vigenere_table_1, cipher_encryption


class ShiphrTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_encr1(self):
        key = msg_and_key('привет мир', 'ПОКА')
        result = cipher_encryption('привет мир', key)
        self.assertEqual('юютвфа ция', result)

    def test_encr2(self):
        key = msg_and_key('Я люблю программирование', 'питон')
        result = cipher_encryption('Я люблю программирование', key)
        self.assertEqual('О урпшн чвьряиюъхяцфоъчн', result)

    def test_encr3(self):
        key = msg_and_key('Обожаю ТУСУР, самый лучший ВУЗ', '')
        result = cipher_encryption('Обожаю ТУСУР, самый лучший ВУЗ', key)
        self.assertEqual('', result)

    def test_encr4(self):
        key = msg_and_key('', 'Обожаю ТУСУР, самый лучший ВУЗ')
        result = cipher_encryption('', key)
        self.assertEqual('', result)

    def test_encr5(self):
        key = msg_and_key('', '')
        result = cipher_encryption('', key)
        self.assertEqual('', result)

    def test_encr6(self):
        key = msg_and_key('+79996189231', 'ПИТОН')
        result = cipher_encryption('+79996189231', key)
        self.assertEqual('+79996189231', result)
