import random

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


class RandomCipher(SubstitutionCipher):

    def __init__(self):

        letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

        random.shuffle(letters)

        key = "".join(letters)

        print("Random Key:", key)

        super().__init__(key)


cipher = RandomCipher()

print(cipher.encrypt("HELLO"))