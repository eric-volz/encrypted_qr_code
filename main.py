from QR_Code import QR_Code
from AES_Crypto import AESCipher

if "__main__" == __name__:
    print("Möchtest du deinen Text in einem QR-Code Verschlüsseln oder möchtest diesen entschlüsseln?")
    print("1: Verschlüsseln | 2: Entschlüsseln")
    number = input("Nummer Eingeben: ")
    if number == "1":
        text = input("Gebe hier dein zu Verschlüsselndes Geheimnis ein: ")
        key = input("Wie lautet dein Verschlüsselungs Passwort?: ")
        filename = input("Wie soll der QR-Code heißen?: ")

        aes = AESCipher(key)
        secret = aes.encrypt(text)
        print(secret)

        img = QR_Code.save_to_qr_code(secret)
        img.save(filename + ".png")
    elif number == "2":
        secret = input("Gebe hier dein zu Secret ein: ")
        key = input("Wie lautet dein Entschlüsselungs Passwort?: ")

        aes = AESCipher(key)
        text = aes.decrypt(secret)
        print(text)
    else:
        print("Das eingegebene Zeichen steht nicht zur Auswahl!")




