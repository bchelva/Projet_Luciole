# Partie 1
SEUIL = 5

class Luciole:
    def __init__(self, delta):
        self.energy = 0
        self.delta = delta

    def update(self):
        self.energy += self.delta
        if self.energy > SEUIL:
            print("Flash lumineux!")
            self.energy = 0

luciole = Luciole(2)
for i in range(10):
    luciole.update()
    print(f"Pas de temps {i}, niveau d'énergie : {luciole.energy}")

# Question 1
import random

def main():
    lucioleEnergie = random.uniform(0, 100)
    print(lucioleEnergie)
    if lucioleEnergie > 0 and lucioleEnergie < 100:
        print("La valeur de lucioleEnergie est comprise entre 0 et 100.")
    else:
        print("La valeur de lucioleEnergie n'est pas comprise entre 0 et 100.")

if __name__ == "__main__":
    main()


# Question 2
def symboliseLuciole(niveauEnergie):
    if niveauEnergie > SEUIL:
        return '*'
    else:
        return '.'

# Question 3
def afficheLuciole(niveauEnergie, verbeux):
    symbol = symboliseLuciole(niveauEnergie)
    if verbeux:
        print(symbol, niveauEnergie)
    else:
        print(symbol)


# Question 3
def afficheLuciole(niveauEnergie, verbeux):
    symbol = symboliseLuciole(niveauEnergie)
    if verbeux:
        print(symbol, niveauEnergie)
    else:
        print(symbol)


# Question 4
def main():
    lucioleEnergie = random.uniform(0., 100.)
    verbeux = False
    while lucioleEnergie >= 0.:
        afficheLuciole(lucioleEnergie, verbeux)
        lucioleEnergie = float(input("Entrez un nouveau niveau d'énergie : "))

if __name__ == '__main__':
    main()


# Question 5
def main():
    lucioleEnergie = random.uniform(0., 100.)
    verbeux = False
    while lucioleEnergie >= 0.:
        afficheLuciole(lucioleEnergie, verbeux)
        lucioleEnergie = float(input("Entrez un nouveau niveau d'énergie : "))

if __name__ == '__main__':
    main()


# Question 6
def incrementeLuciole(niveauEnergie, deltaEnergie):
    return niveauEnergie + deltaEnergie


# Question 7
def main():
    lucioleEnergie = random.uniform(0., 100.)
    deltaEnergie = random.uniform(0., 100.)
    nombrePas = 5

    for i in range(nombrePas):
        lucioleEnergie = incrementeLuciole(lucioleEnergie, deltaEnergie)
        afficheLuciole(lucioleEnergie, verbeux=True)


# Question 8
import random

def simuleLucioleNbPas(nbPas, verbeux=False):
    lucioleEnergie = random.uniform(0., 100.)
    deltaEnergie = random.uniform(0., 100.)
    for i in range(nbPas):
        lucioleEnergie = incrementeLuciole(lucioleEnergie, deltaEnergie)
        afficheLuciole(lucioleEnergie, verbeux)

def main():
    simuleLucioleNbPas(10, True)


# Question 9
import random

def symboliseLuciole(niveauEnergie):
    if niveauEnergie >= 50:
        return '*'
    else:
        return '.'

def afficheLuciole(niveauEnergie, verbeux):
    symbole = symboliseLuciole(niveauEnergie)
    if verbeux:
        print(symbole + ' ' + str(niveauEnergie))
    else:
        print(symbole)

def incrementeLuciole(niveauEnergie, deltaEnergie):
    niveauEnergie += deltaEnergie
    if niveauEnergie > 100:
        niveauEnergie = 0
    return niveauEnergie

def simuleLucioleNbPas(nbPas):
    niveauEnergie = random.uniform(0, 100)
    deltaEnergie = random.uniform(-10, 10)
    for i in range(nbPas):
        afficheLuciole(niveauEnergie, True)
        niveauEnergie = incrementeLuciole(niveauEnergie, deltaEnergie)

def simuleLucioleNbFlashs():
    niveauEnergie = random.uniform(0, 100)
    deltaEnergie = random.uniform(-10, 10)
    nbFlashs = 0
    while nbFlashs < 3:
        afficheLuciole(niveauEnergie, True)
        niveauEnergie = incrementeLuciole(niveauEnergie, deltaEnergie)
        if symboliseLuciole(niveauEnergie) == '*':
            nbFlashs += 1

if __name__ == '__main__':
    # Test de simuleLucioleNbPas
    nbPas = 10
    print('Simulation de la luciole pendant ' + str(nbPas) + ' pas de temps:')
    simuleLucioleNbPas(nbPas)

    # Test de simuleLucioleNbFlashs
    print('\nSimulation de la luciole jusqu\'à ce qu\'elle émette 3 flashes:')
    simuleLucioleNbFlashs()


# Question 10
import random

def creerLuciole():
    niveauEnergie = random.uniform(0, 100)
    deltaEnergie = random.uniform(0, 100)
    return [niveauEnergie, deltaEnergie]


# Question 11
import random

def incrementeLuciole(luciole):
    luciole[0] = luciole[0] + luciole[1]
    if luciole[0] > 1:
        luciole[0] = 0
        luciole[1] = random.uniform(0, 0.1)
    return luciole


# Question 12
import random

def creerPopulation(nbLucioles):
    population = []
    for i in range(nbLucioles):
        luciole = [random.random(), random.random()]
        population.append(luciole)
    return population


# Question 13
import random

def creerLuciole():
    return [random.uniform(0, 1), random.uniform(0, 1)]

def creerPopulation(nbLucioles):
    population = []
    for i in range(nbLucioles):
        population.append(creerLuciole())
    return population

def main():
    population = creerPopulation(5)
    for i in range(len(population)):
        for j in range(i + 1, len(population)):
            assert population[i] is not population[j], "Les lucioles sont identiques"
        assert population[i][0] != population[j][0], "Le niveau d'énergie est identique pour deux lucioles"
    print("Les lucioles sont bien différentes")

if __name__ == "__main__":
    main()



# Question 14
def prairieVide(nbLignes, nbColonnes):
    prairie = []
    for i in range(nbLignes):
        ligne = [-1] * nbColonnes
        prairie.append(ligne)
    return prairie


# Question 15
def affichePrairie(prairie, population):
    nbLignes = len(prairie)
    nbColonnes = len(prairie[0])

    for i in range(nbLignes):
        for j in range(nbColonnes):
            if prairie[i][j] == -1:
                print(" ", end="")
            elif population[prairie[i][j]].emetFlash:
                print("*", end="")
            else:
                print(".", end="")
        print("")

    print("#" * (nbColonnes + 2))


# Question 16
def main():
    nb_lignes = 5
    nb_colonnes = 5
    nb_lucioles = 5

    prairie = prairieVide(nb_lignes, nb_colonnes)
    population = creerPopulation(nb_lucioles)

    # Placer aléatoirement les lucioles sur la prairie
    for luciole in population:
        ligne = random.randint(0, nb_lignes - 1)
        colonne = random.randint(0, nb_colonnes - 1)
        while prairie[ligne][colonne] != -1:
            ligne = random.randint(0, nb_lignes - 1)
            colonne = random.randint(0, nb_colonnes - 1)
        prairie[ligne][colonne] = luciole.numero
        luciole.position = (ligne, colonne)

    affichePrairie(prairie, population)


if __name__ == "__main__":
    main()



# Question 17
import random

def prairieLucioles(nbLignes, nbColonnes, population):
    prairie = [[-1 for j in range(nbColonnes)] for i in range(nbLignes)]
    for luciole in population:
        ligne = random.randint(0, nbLignes-1)
        colonne = random.randint(0, nbColonnes-1)
        while prairie[ligne][colonne] != -1:
            ligne = random.randint(0, nbLignes-1)
            colonne = random.randint(0, nbColonnes-1)
        prairie[ligne][colonne] = luciole.numero
    return prairie


# Question 18
def main():
    nbLignes = 5
    nbColonnes = 5
    nbLucioles = 10
    population = creerPopulation(nbLucioles)
    prairie = prairieLucioles(nbLignes, nbColonnes, population)
    affichePrairie(prairie, population)

if __name__ == "__main__":
    main()


# Question 19
import random

def simulationPrairie(prairie, population, nbPas):
    for i in range(nbPas):
        for luciole in population:
            # mise à jour de la position de la luciole
            x, y = luciole.position
            x += random.choice([-1, 0, 1])
            y += random.choice([-1, 0, 1])
            luciole.position = (x, y)

            # mise à jour de l'état de la luciole
            luciole.etat = not luciole.etat
            luciole.energie -= 1

            # mise à jour de la prairie
            prairie[x][y] = luciole.numero

        # affichage de la prairie à chaque pas de temps
        affichePrairie(prairie, population)


# Question 20
def simulationPrairie(prairie, population, nbPas):
    for i in range(nbPas):
        for j in range(len(population)):
            luciole = population[j]
            if luciole["energie"] <= 0:
                prairie[luciole["position"][0]][luciole["position"][1]] = -1
                luciole["position"] = [randint(0, len(prairie) - 1), randint(0, len(prairie[0]) - 1)]
                while prairie[luciole["position"][0]][luciole["position"][1]] != -1:
                    luciole["position"] = [randint(0, len(prairie) - 1), randint(0, len(prairie[0]) - 1)]
                prairie[luciole["position"][0]][luciole["position"][1]] = luciole["numero"]
                luciole["energie"] = luciole["energieInitiale"]
            else:
                luciole["energie"] -= 1
        affichePrairie(prairie, population)
        sleep(1)


