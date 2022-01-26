def msg_and_key(msg, key):
    if msg == '' or key == '':
        key_map = 'Error'
        return key_map
    else:
        key_map = ""
        j = 0
        for i in range(len(msg)):
            if 1040 <= ord(msg[i]) <= 1071:
                if j < len(key):
                    key_map += key[j].upper()
                    j += 1
                else:
                    j = 0
                    key_map += key[j].upper()
                    j += 1
            elif 1072 <= ord(msg[i]) <= 1103:
                if j < len(key):
                    key_map += key[j]
                    j += 1
                else:
                    j = 0
                    key_map += key[j]
                    j += 1
            else:
                key_map += " "
        return key_map

def create_vigenere_table():
    table = []
    for i in range(32):
        table.append([])
    for row in range(32):
        for column in range(32):
            if (row + 1040) + column > 1071:
                table[row].append(chr((row + 1040) + column - 32))
            else:
                table[row].append(chr((row + 1040) + column))
    return table

def create_vigenere_table_1():
    table = []
    for i in range(32):
        table.append([])
    for row in range(32):
        for column in range(32):
            if (row + 1072) + column > 1103:
                table[row].append(chr((row + 1072) + column - 32))
            else:
                table[row].append(chr((row + 1072) + column))
    return table

def cipher_encryption(message, mapped_key):
    table = create_vigenere_table()
    table1 = create_vigenere_table_1()
    encrypted_text = ""
    if mapped_key == 'Error':
        return encrypted_text
    for i in range(len(message)):
        if 1071 >= ord(message[i]) >= 1040:
            row = ord(message[i]) - 1040
            column = ord(mapped_key[i]) - 1040
            encrypted_text += table[row][column]
        elif 1072 <= ord(message[i]) <= 1103:
            row = ord(message[i]) - 1072
            column = ord(mapped_key[i]) - 1072
            encrypted_text += table1[row][column]
        else:
            encrypted_text += message[i]
    return encrypted_text

