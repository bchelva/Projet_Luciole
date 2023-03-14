# Question 28
class Prairie:
    def __init__(self, matrice=None, population=None):
        if matrice is None:
            self.matrice = []
        else:
            self.matrice = matrice

        if population is None:
            self.population = population()
        else:
            self.population = population

    def ajouteLigne(self, ligne):
        self.matrice.append(ligne)

    def getMatrice(self):
        return self.matrice

    def setMatrice(self, matrice):
        self.matrice = matrice

    def getPopulation(self):
        return self.population

    def setPopulation(self, population):
        self.population = population


# Question 29
class Prairie:
    def __init__(self, matrice=None, population=None):
        if matrice is None:
            self.matrice = []
        else:
            self.matrice = matrice

        if population is None:
            self.population = population()
        else:
            self.population = population

    def ajouteLigne(self, ligne):
        self.matrice.append(ligne)

    def getMatrice(self):
        return self.matrice

    def setMatrice(self, matrice):
        self.matrice = matrice

    def getPopulation(self):
        return self.population

    def setPopulation(self, population):
        self.population = population

    @staticmethod
    def creerPrairieVide(nbLignes, nbColonnes):
        matrice = []
        for i in range(nbLignes):
            matrice.append([0] * nbColonnes)
        return Prairie(matrice, population())



# Question 30
class Prairie:
    def __init__(self, matrice=None, population=None):
        if matrice is None:
            self.matrice = []
        else:
            self.matrice = matrice

        if population is None:
            self.population = population()
        else:
            self.population = population

    def ajouteLigne(self, ligne):
        self.matrice.append(ligne)

    def getMatrice(self):
        return self.matrice

    def setMatrice(self, matrice):
        self.matrice = matrice

    def getPopulation(self):
        return self.population

    def setPopulation(self, population):
        self.population = population

    @staticmethod
    def creerPrairieVide(nbLignes, nbColonnes):
        matrice = []
        for i in range(nbLignes):
            matrice.append([0] * nbColonnes)
        return Prairie(matrice, population())

    def affichePrairie(self):
        for ligne in self.matrice:
            for colonne in ligne:
                print(colonne, end=' ')
            print()


# Question 31
import random


class Prairie:
    def __init__(self, matrice=None, population=None):
        if matrice is None:
            self.matrice = []
        else:
            self.matrice = matrice

        if population is None:
            self.population = Population()
        else:
            self.population = population

    def ajouteLigne(self, ligne):
        self.matrice.append(ligne)

    def getMatrice(self):
        return self.matrice

    def setMatrice(self, matrice):
        self.matrice = matrice

    def getPopulation(self):
        return self.population

    def setPopulation(self, population):
        self.population = population

    @staticmethod
    def creerPrairieVide(nbLignes, nbColonnes):
        matrice = []
        for i in range(nbLignes):
            matrice.append([0] * nbColonnes)
        return Prairie(matrice, Population())

    def affichePrairie(self):
        for ligne in self.matrice:
            for colonne in ligne:
                print(colonne, end=' ')
            print()

    def prairieLucioles(self, nbLignes, nbColonnes, population):
        prairie = Prairie.creerPrairieVide(nbLignes, nbColonnes)
        lucioles = population.getLucioles()
        for luciole in lucioles:
            placed = False
            while not placed:
                ligne = random.randint(0, nbLignes - 1)
                colonne = random.randint(0, nbColonnes - 1)
                if prairie.matrice[ligne][colonne] == 0:
                    prairie.matrice[ligne][colonne] = luciole
                    placed = True
        return prairie


# Question 32
import random


class Prairie:
    def __init__(self, matrice=None, population=None):
        if matrice is None:
            self.matrice = []
        else:
            self.matrice = matrice

        if population is None:
            self.population = Population()
        else:
            self.population = population

    def ajouteLigne(self, ligne):
        self.matrice.append(ligne)

    def getMatrice(self):
        return self.matrice

    def setMatrice(self, matrice):
        self.matrice = matrice

    def getPopulation(self):
        return self.population

    def setPopulation(self, population):
        self.population = population

    @staticmethod
    def creerPrairieVide(nbLignes, nbColonnes):
        matrice = []
        for i in range(nbLignes):
            matrice.append([0] * nbColonnes)
        return Prairie(matrice, Population())

    def affichePrairie(self):
        for ligne in self.matrice:
            for colonne in ligne:
                print(colonne, end=' ')
            print()

    def prairieLucioles(self, nbLignes, nbColonnes, population):
        prairie = Prairie.creerPrairieVide(nbLignes, nbColonnes)
        lucioles = population.getLucioles()
        for luciole in lucioles:
            placed = False
            while not placed:
                ligne = random.randint(0, nbLignes - 1)
                colonne = random.randint(0, nbColonnes - 1)
                if prairie.matrice[ligne][colonne] == 0:
                    prairie.matrice[ligne][colonne] = luciole
                    placed = True
        return prairie

    def simulationPrairie(self, nbPas):
        for i in range(nbPas):
            for ligne in range(len(self.matrice)):
                for colonne in range(len(self.matrice[0])):
                    if self.matrice[ligne][colonne] != 0:
                        luciole = self.matrice[ligne][colonne]
                        luciole.simuleLucioleNbPas(1, False)
                        self.matrice[ligne][colonne] = 0
                        new_ligne = ligne + luciole.getDeltaLigne()
                        new_colonne = colonne + luciole.getDeltaColonne()
                        if new_ligne >= 0 and new_ligne < len(self.matrice) and new_colonne >= 0 and new_colonne < len(
                                self.matrice[0]):
                            if self.matrice[new_ligne][new_colonne] == 0:
                                self.matrice[new_ligne][new_colonne] = luciole



# Question 33
import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.increment_button = tk.Button(self)
        self.increment_button["text"] = "Incrémente"
        self.increment_button["command"] = self.increment
        self.increment_button.pack(side="top")

        self.quit = tk.Button(self, text="Quit", fg="red",
                              command=root.destroy)
        self.quit.pack(side="bottom")

    def increment(self):
        # Code pour incrémenter l'état de la prairie de lucioles
        pass


root = tk.Tk()
app = Application(master=root)
app.mainloop()

