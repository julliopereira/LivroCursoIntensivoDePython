from random import randint

x = randint(1, 6)

class Die():
    def __init__(self,slides=6):
        self.slides = slides

    def rool_die(self):
        count = 1
        while count <= self.slides:
            x = randint(1, 6)
            print(x)
            count += 1

rolar = Die()