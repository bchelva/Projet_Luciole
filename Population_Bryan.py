# Question 26
import random


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


class Population:
    def __init__(self):
        self.lucioleList = []

    def ajouteLuciole(self, luciole):
        self.lucioleList.append(luciole)

    def simulePopulationNbPas(self, nbPas):
        for luciole in self.lucioleList:
            luciole.simuleLucioleNbPas(nbPas)



# Question 27
import random


class Luciole:
    def __init__(self, energie=None, delta=None):
        if energie is None:
            self.energie = int(100 * random.random()) + 1
        else:
            self.energie = energie

        if delta is None:
            self.delta = int(10 * random.random()) + 1
        else:
            self.delta = delta

    @staticmethod
    def creerLuciole():
        return Luciole()

    def simuleLucioleNbPas(self, nbPas):
        for i in range(nbPas):
            self.energie = self.energie + self.delta
            print("Au pas de temps {0}, la luciole a une énergie de {1}".format(i + 1, self.energie))

    def getEnergie(self):
        return self.energie

    def setEnergie(self, energie):
        self.energie = energie

    def getDelta(self):
        return self.delta

    def setDelta(self, delta):
        self.delta = delta


class Population:
    def __init__(self, lucioleList=None):
        if lucioleList is None:
            self.lucioleList = []
        else:
            self.lucioleList = lucioleList

    def ajouteLuciole(self, luciole):
        self.lucioleList.append(luciole)

    def simulePopulationNbPas(self, nbPas):
        for luciole in self.lucioleList:
            luciole.simuleLucioleNbPas(nbPas)

    def getLucioleList(self):
        return self.lucioleList

    def setLucioleList(self, lucioleList):
        self.lucioleList = lucioleList
