class SubstitutionCipher:

    def __init__(self, key):

        self.upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.key = key

    def encrypt(self, text):

        result = ""

        for ch in text:

            if ch.isupper():
                index = self.upper.index(ch)
                result += self.key[index]
            else:
                result += ch

        return result

    def decrypt(self, text):

        result = ""

        for ch in text:

            if ch.isupper():
                index = self.key.index(ch)
                result += self.upper[index]
            else:
                result += ch

        return result


key = "QWERTYUIOPASDFGHJKLZXCVBNM"

c = SubstitutionCipher(key)

msg = "HELLO"

enc = c.encrypt(msg)

print("Encrypted:", enc)

print("Decrypted:", c.decrypt(enc))