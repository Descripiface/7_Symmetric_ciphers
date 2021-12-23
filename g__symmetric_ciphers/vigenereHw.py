cryptMode = input("[E]ncrypt|[D]ecrypt: ").upper()
if cryptMode not in ['E', 'D']:
    print("Error: mode is not Found!")
    raise SystemExit

startMessage = input("Write the message: ").upper()
numberKeys = int(input("How much keys: "))

listKeys = []
for index in range(numberKeys):
    listKeys.append(input("Write the keyWord[" + str(index) + "]: ").upper())


def encryptDecrypt(mode, message, keys):
    for key in listKeys:
        final = ""
        key *= len(message) // len(key) + 1  # Подгоняем длину ключа под длину сообщения
        for index, symbol in enumerate(message):
            if mode == 'E':  # Или шифруем или дешифруем
                temp = ord(symbol) + ord(key[index])
            else:
                temp = ord(symbol) - ord(key[index])
            final += chr(temp % 26 + ord('A'))
        message = final
    return final


print("Final message:", encryptDecrypt(cryptMode, startMessage, listKeys))
