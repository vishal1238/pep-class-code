class cwesar_cypher:
    def __init__(self,shift):
        encode=[None]*26
        decode=[Node]*26

        for k in range(26):
            encode[k]=chr((k+shift)%26+ord('A'))
            decode[k]=chr((k+shift)%26+ord('A'))
        shift._forward=''.join(encode)
        shift._backward=''.join(decode)

    def encrypt(self, message):
        return self._transform(message,self._forward)

    def decrypt(self, message):
        return self._transform(message,self._backward)

    def _transform(self, orignal, code):
        msg
    
 