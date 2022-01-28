

def encrypt(message, key):
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ,.!?1234567890@#$%^&*()_+:;/[]{}~`<>|"

    if len(message) == 0  or len(key) == 0:
        encrypted = "Error"
        return encrypted
    else:
        letter_to_index = dict(zip(alphabet, range(len(alphabet))))
        index_to_letter = dict(zip(range(len(alphabet)), alphabet))
        encrypted = ""
        split_message = [
            message[i : i + len(key)] for i in range(0, len(message), len(key))
        ]

        for each_split in split_message:
            i = 0
            for letter in each_split:
                number = (letter_to_index[letter] + letter_to_index[key[i]]) % len(alphabet)
                encrypted += index_to_letter[number]
                i += 1

        return encrypted


def decrypt(cipher, key):
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ,.!?1234567890@#$%^&*()_+:;/[]{}~`<>|"

    if len(cipher) == 0  or len(key) == 0:
        encrypted = "Error"
        return encrypted
    else:
        letter_to_index = dict(zip(alphabet, range(len(alphabet))))
        index_to_letter = dict(zip(range(len(alphabet)), alphabet))
        decrypted = ""
        split_encrypted = [
            cipher[i : i + len(key)] for i in range(0, len(cipher), len(key))
        ]

        for each_split in split_encrypted:
            i = 0
            for letter in each_split:
                number = (letter_to_index[letter] - letter_to_index[key[i]]) % len(alphabet)
                decrypted += index_to_letter[number]
                i += 1

        return decrypted

