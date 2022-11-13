import random

class Encoder:
    def __init__(self, number):
        self.number = number

    def __cipher(self):
        self.number = self.number + random.randint(1, 1000)
        return self.number

    def get_cipher(self):
        print(self.__cipher())

ob = Encoder(1)
ob.get_cipher()