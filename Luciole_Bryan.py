# Partie 2
# Question 21
class Luciole:
    SEUIL = 10

    def __init__(self, energie, delta):
        self.energie = energie
        self.delta = delta

    def __repr__(self):
        return f"Luciole(energie={self.energie}, delta={self.delta})"


# Question 22
class Luciole:
    SEUIL = 10

    def __init__(self, energie, delta):
        self.__energie = energie
        self.__delta = delta

    def getEnergie(self):
        return self.__energie

    def setEnergie(self, energie):
        self.__energie = energie

    def getDelta(self):
        return self.__delta

    def setDelta(self, delta):
        self.__delta = delta


# Question 23
class Luciole:
    SEUIL = 100

    def __init__(self, energie, delta):
        self.__energie = energie
        self.__delta = delta

    def getEnergie(self):
        return self.__energie

    def setEnergie(self, energie):
        self.__energie = energie

    def getDelta(self):
        return self.__delta

    def setDelta(self, delta):
        self.__delta = delta

    def symboliseLuciole(self):
        if self.__energie >= Luciole.SEUIL:
            return '*'
        else:
            return '.'

    def afficheLuciole(self):
        print(f"Energie : {self.__energie}")
        print(f"Delta : {self.__delta}")

    def incrementeLuciole(self):
        self.__energie += self.__delta
        if self.__energie >= Luciole.SEUIL:
            self.__energie = 0


# Question 24
import random


class Luciole:
    SEUIL = 10

    def __init__(self, energy, delta):
        self.__energy = energy
        self.__delta = delta

    # getters
    def getEnergy(self):
        return self.__energy

    def getDelta(self):
        return self.__delta

    # setters
    def setEnergy(self, energy):
        self.__energy = energy

    def setDelta(self, delta):
        self.__delta = delta

    def symboliseLuciole(self):
        if self.__energy >= self.SEUIL:
            return '*'
        else:
            return '.'

    def afficheLuciole(self):
        print(self.symboliseLuciole(), end=" ")

    def incrementeLuciole(self):
        self.__energy += self.__delta

    @staticmethod
    def creerLuciole():
        energy = random.randint(1, 20)
        delta = random.randint(-1, 1)
        return Luciole(energy, delta)


# Question 25
class Luciole:
    def __init__(self):
        self.energie = int(100 * random.random()) + 1
        self.delta = int(10 * random.random()) + 1

    @staticmethod
    def creerLuciole():
        return Luciole()

    def simuleLucioleNbPas(self, nbPas):
        for i in range(nbPas):
            self.energie = self.energie + self.delta
            print("Au pas de temps {0}, la luciole a une énergie de {1}".format(i + 1, self.energie))


