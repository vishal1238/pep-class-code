class CaesarCipher:

    def encrypt(self, text, shift):

        result = ""

        for ch in text:

            if ch.isupper():
                result += chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))

            elif ch.islower():
                result += chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))

            else:
                result += ch

        return result


cipher = CaesarCipher()

text = input("Enter message: ")

encrypted = cipher.encrypt(text, 3)

print("Encrypted:", encrypted)