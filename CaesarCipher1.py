# Caesar Cipher using SubstitutionCipher
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


class CaesarCipher(SubstitutionCipher):

    def __init__(self, shift):

        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        key = ""

        for i in range(26):
            key += letters[(i + shift) % 26]

        super().__init__(key)


cipher = CaesarCipher(3)

print(cipher.encrypt("HELLO"))