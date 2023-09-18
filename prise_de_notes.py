#coding:utf-8

"""FORMATION PYTHON"""

#Différentes commandes :

#coding:utf-8 (à mettre en début de fichier, normalement il y sera par défaut)
#input() = lire au clavier
#type() = retourne le type d'une variable, d'une donnée etc...
#str.format() = formater une chaîne
#int(), float(), str(), bool() = caster une donnée; la convertir
#print("") ou print('') = sert à afficher un texte à l'écran (print est une fonction)

#Exemples :

print("Hello World")
print('Hello World')
print('L\'envers du décor') #pour les simples quotes uniquement
print("L'envers\n du décor") #\n permet un retour à la ligne
print("\tL'envers du décor") #\t permet la tabulation

#Les variables

#Doit commencer par une lettre ou un underscore
#Ne doit pas contenir de caractéres spéciaux
#Ne pas contenir d'espace
#Utiliser des underscores
#* Il est meilleur d'utiliser la même syntaxe tout au long de son code

#Exemples :
#agePersonne
#age_personne
#agepersonne
#AgePersonne
#Age_Personne
#_AgePersonne

#TYPES STANDARDS :
#Entier numérique (int)
#Nombre flottant (float)
#Chaîne de caractéres (str)
#Booléen (bool)

#EXEMPLES :

agePersonne=14 #sera considéré comme un entier
prixHT=120.46
agePersonne2="25" #sera considéré comme un texte
continuer_partie=True
print("Âge de la personne:", agePersonne) #en enlevant les doubles quotes, Python récupere la donnée de la variable précedemment crée
print(type(agePersonne2))

#EXEMPLE 2 :
texte="L'âge de la personne est {} et le prix HT est de {} euros."
print(texte.format(agePersonne, prixHT))
#ou
print("L'âge de la personne est {} et le prix HT est de {} euros.".format(agePersonne, prixHT))

#LA FONCTION INPUT

nomJoueur=input("Choisir un nom de joueur :")
print("Bienvenue, ", nomJoueur)

#LES DIFFERENTES FONCTIONS int(), float(), str(), bool()

#int():
prixHT=input("Entrez un prix HT : ")
prixHT=int(prixHT) #int permet de convertir le prixHT en donnée chiffrable et il ne sera plus considéré comme une chaîne de caractére
prixTTC=prixHT + (prixHT * 20/100)
print("Prix TTC=", prixTTC)

#bool() :
valeur_booleen=False
valeur_booleen=int(valeur_booleen)
print(valeur_booleen)

#OPERATEURS EN PYTHON :
# + (addition)
# - (soustraction)
# * (multiplication)
# / (division)
# % (modulo) reste d'une division Euclidienne

#EXEMPLE :
calcul=5/2
calcul=int(calcul)
print("Résultat=", calcul)

calcul=5/2
calcul=float(calcul)
calcul2=5%2
calcul2=int(calcul2)
print("Résultat=", calcul, "reste", calcul2)

niveauPersonnage=input("Niveau de départ ?")
niveauPersonnage=int(niveauPersonnage)
print("Niveau du personnage", niveauPersonnage)
print("Combat réussi, tu gagnes deux niveaux!")
niveauPersonnage=niveauPersonnage+2
print("Niveau du personnage", niveauPersonnage)

#LES CONDITIONS

#Exemple :
identifiant="Jordan"
mot_de_passe="password123"
print("Interface de connexion")

user_id=input("Entrez votre identifiant:")
user_password=input("Entrez votre mot de passe:")
if user_id and user_password==mot_de_passe:
    print("Vous êtes connectés, bienvenue", user_id) #print est dans le if

print("Je ne suis plus dans le if")

#Les opérateurs de comparaison

# == (égal à)
# != (différent de)
# < (plus petit que)
# > (plus grand que)
# <= (plus petit ou égal à)
# >= (plus grand ou égal à)

#Mots clés des conditions : if/elif/else
#Les conditions multiples :
# and (ET)
# or (OU)
# in/not in (DANS/PAS DANS)

#EXEMPLE :
lettre_hasard="b"
if lettre_hasard in "aeiouy":
    print("C'est une consonne")
else:
    print("C'est une voyelle")

#Exemple 2 :
age=int(input("Quel âge as tu ?"))
if age==18:
    print("Tu viens d'être majeur")
elif age==50:
    print("Tu viens d'avoir 50 ans")
elif age==60:
    print("Tu viens d'avoir 60 ans")
else:
    print("Tu as", age, "ans")

#Exemple 3 :
jeu_charge = True #True = vrai (=1)
if not jeu_charge:
    print("Le jeu est éteint")
else:
    print("Le jeu est lancé")

#Exemple 4 :
age = input("Quel âge as-tu ?")
age = int(age)

if age > 0 and age < 100:
    print("L'âge est validé")
else:
    print("L'âge est incorrect")

if 0 < age <= 100:
    print("L'âge est validé")
else:
    print("L'âge est incorrect")

#Les boucles

#Boucles : while/for
#Mots-clés : break (casse la boucle) / continue (revient au début de la boucle)

#Exemples :

compteur = 0
while compteur < 5:
    print("Je suis une phrase")
    compteur += 1
print("Je suis sorti de la boucle...") #Lorsqu'il n'y a plus la tabulation, on sort du while

##########################

jeu_lance = True
print("")

while jeu_lance:
    #Fais des instructions en rapport avec le jeu
    choixMenu = input(">")
    if choixMenu =="again":
        continue
    elif choixMenu == "quit":
        jeu_lance = False
    elif choixMenu =="hello":
        print("Bonjour !")
    else:
        print("Commande introuvable")
print("A bientôt !")

#Les fonctions (def)

def dire(nom_personne="Tom", message_personne="Salut !", age_personne=18):
    print("{} ({} ans):{}".format(nom_personne, age_personne, message_personne))
    dire(nom_personne="Jason", age_personne=26)

def show_inventory(*list_items):
    for item in list_items:
        print(item)
show_inventory("epee", "arc", "cape", "bouclier")

#Les valeurs de retour

def calculer_somme(nombre1, nombre2):
    resultat = nombre1 + nombre2
    return resultat
print(calculer_somme(5,16))

######
def calculer_somme(nombre3, nombre4):
    return nombre3 + nombre4
print(calculer_somme(3, 45))

#Modularité

#Les fonctions lambdas : elle ne réalise qu'une seule instruction
coucou = lambda:print("Bonjour") #si on l'exécute, cela n'affiche rien du tout, nous avons seulement défini une fonction
coucou() #si on l'exécute, cela affiche Bonjour, comme définit ci dessus

calculer = lambda a, b : a + b
print(calculer(14, 25))

#Les modules

# Importer un module : import <nom_module>
# from <nom_module> import <nom_fonction>
# from <nom_module> import *

# Exemples :
resultat = sqrt(100)
print(resultat) #Cela ne fonctionne pas car il n'y a pas le module requis (math)

# Ce qui est juste :
import math
resultat = math.sqrt(130)
print(resultat)

############
from math import sqrt
resultat=sqrt(102)
print(resultat)

############
from math import *
resultat = sqrt(101)
print(resultat)

# Pour créer un module, il faut créer un nouveau fichier dans le dossier du projet (ressemble au principe CSS avec HTML5)

# Exemples :
def parler(personnage, message):
    print("{} : {}".format(personne, message))

def au_revoir():
    print("Au revoir !")

# Ensuite il faut écrire dans le fichier main :

import player #ceci est la commande permettant de charger le module
player.au_revoir()
player.parler("Jason", "Salut les abonnées !")

#Si l'on souhaite déplacer le module dans un sous-dossier (p.ex includes) où se trouve notre fichier main :
import includes.player as player
player.au_revoir()
player.parler("Jason", "Salut les abonnées !")

# Gestion des erreurs :

#Les différents types d'exceptions :
# ValueError
# NameError
# TypeError
# ZeroDivisionError
# OSError
# AssertionError

ageUser = input("Quel âge as-tu ?")
try : #permet d'essayer l'instruction
    ageUser = int(ageUser)
except : #ce qui se passe en cas d'échec
    print("L'âge indiqué est incorrect !")
else: #ce qui se passe en cas de réussite
    print("Tu as", ageUser, "ans")
finally : # affichera dans tout les cas
    print("Fin du programme")

###########

nombre6=150
nombre7= input("Choiisr le nombre pour diviser : ")
try:
    nombre7=int(nombre7)
    print("Résultat = {}".format(nombre6/nombre7))
except ZeroDivisionError:
    print("Vous ne pouvez pas diviser par zéro.")
except ValueError:
    print("Vous devez entrer un nombre")
except:
    print("Valeur incorrecte")
else:
    print("Bravo, tu as noté un nombre valide !")
finally:
    print("Fin du programme")
# ou pour lever l'exception
try:
    age = input("Quel âge as-tu?")
    age = int(age)
    if age < 25:
        raise ZeroDivisionError
except ZeroDivisionError:
    print("J'ai attrapé ton exception inutile")

#AssertionError
try:
    age = input("Quel âge as-tu?")
    age = int(age)
    assert  age < 25 #je veux que âge soit plus grand que 25
except AssertionError:
    print("J'ai attrapé l'exception")

#La Programmation Orienté Objet avec le langage Python (POO)
#Ce que l'on a vu :
# Afficher du texte (print)
# Saisir des informations
# Variables
# Conditions et boucles
# Fonctions et modularité
# Gestion des erreurs

# Notions de base :
# Classe : plan de conception, genre (Humain)
# Objet : instance de classe (Julien est un objet de classe Humain)
# Attribut : variable de classe (nom, âge, sexe, taille...)
# Propriété : maniére de manipuler les attributs (lecture seule, accés non autorisé en dehors de la classe...)
# Méthode : fonction d'une classe (ex: manger, marcher, parler, dormir, mourir etc...)
# Méthode de classe : fonction d'une classe (explication à venir plus tard)
# Méthode statique : fonction d'une classe, mais indépendante de celle-ci (on peut trés bien crée une fonction de classe même en dehors de tout objet)
# Héritage : classe Fille qui hérite d'une classe Mére (Fille est sorte de Mére)
#          : classe Chat hérite de la classe Animal

# La programmation orienté objet (POO) avec le language Python

# Classe : plan de conception, genre (ex: Humain)
# Objet : instance d'une classe (ex : Julien, est un objet de classe Humain)
# Attribut : variable de classe (ex : prénom, âge, taille, sexe)

class Humain:
    """
    Classe des êtres humains
    """
    def __init__(self, c_prenom, c_age=1):
        print("Création d'un Humain...")
        self.prenom = c_prenom
        self.age = c_age
print("Lancement du programme...")

h1 = Humain("Jojo")
print("Prénom de h1 -> {}".format(h1.c_prenom))
print("Age de h1 -> {}".format(h1.c_age))


h2 = Humain("Albert")
print("Prénom de h2 -> {}".format(h2.c_prenom))
print("Age de h2 -> {}".format(h2.c_age))

###################################

class Humain:
    """
    Classe des êtres humains
    """
    humains_crees = 0

    def __init__(self, c_prenom, c_age=1):
        print("Création d'un Humain...")
        self.prenom = c_prenom
        self.age = c_age
        Humain.humains_crees += 1

print("Lancement du programme...")

h1 = Humain("Jojo", 34)
print("Humains existants : {}".format(Humain.humains_crees))

h2 = Humain("Albert", 87)
print("Humains existants : {}".format(Humain.humains_crees))


# Les méthodes (statiques)

class Humain:
    """
    Classe qui définit un humain
    """
    lieu_habitation = "Terre"
    def __int__(self, nom, age):
        self.nom = nom
        self.age = age
    def parler(self, message):
        print("{} a dit : {}".format(self.nom, message))
    def changer_planete(cls, nouvelle_planete): #cls = méthode de classe
        Humain.lieu_habitation = nouvelle_planete
    changer_planete = classmethod(changer_planete)

    def definition():
        print("L'humain est en haut de la chaîne alimentaire")

    definition = staticmethod(definition)
#Programme principal

h1 = Humain("Jordan", 29)

h1.parler("Bonjour à tous !")
h1.parler("Comment allez-vous ?")
print("Planète actuelle : {}".format(Humain.lieu_habitation))

# Les propriétés d'encapsulation
"""
Propriété : manière de manipuler/contrôler des attributs
            principe d'encapsulation ! 
"""

class humain:
    def __init__(self, nom, age):
        print("Création d'un humain...")
        self.nom = nom
        self._age = age

    def _getage(self):
        return self._age
    def _setage(self, nouvel_age):
        if nouvel_age < 0:
            self._age = 0
        self._age = nouvel_age

    def _delage(self):
        del self._age

# property (<getter>, <setter>, <deleter>, <helper>)
age = property(_getage, _setage, _delage)

#Héritage

#Classe Mére
class Vehicule:

    def __init__(self, nom, quantite_essence):
        self.nom = nom
        self.essence = quantite_essence
    def se_deplacer(self):
        print("Le véhicule se déplace".format(self, nom))
#Classe Fille

class Voiture(Vehicule):
    def __init__(self, nom_voiture, essence, puissance):
        Vehicule.__init__(self, nom_voiture, essence)
        self.puissance = puissance
#Programme principal
voiture1 = Voiture("Fiat Uno", 42, 90)
voiture1.se_deplacer()

#Exemple

#Classe Mére 1
class ObjetJeu:
    pass

#Classe Mére
class Arme:
    pass

#Classe Fille
class Fusil(Arme, ObjetJeu):
    pass
#-----------------------------------------------------------------------------------------------------------------------
class Etudiant:
    pass

class Enseignant:
    pass

class Doctorant(Etudiant, Enseignant):
    pass

#-----------------------------------------------------------------------------------------------------------------------

"""
Fonctions utiles : 
    isinstance(<objet>, <classe>) : vérifie qu'un objet est de la classe renseignée
    
    issubclass(<class_fille>, <classe_mere>) : vérifie qu'une classe est fille d'une autre
"""
class Animal:
    def __init__(self, nom):
        self.nom = nom

    def manger(self):
        print(self.nom, "mange...")

class Reptile(Animal):
    def __init__(self, nom, regime_alimentaire):
        Animal.__init__(self, nom)
        self.regime = regime_alimentaire

    def manger(self):
        print("Le reptile mange...")

#Code principal
lezard = Reptile("Lézard", "grenouilles")
if isinstance(lezard, Reptile):
    print("Lézard est un Animal")

"""
Pour vérifier qu'une classe est bien une classe Fille : 
if issubclass(Reptile, Animal:
    print("Reptile hérite d'Animal")
"""

#Les chaînes de caractères

# Classe str : string (chaînes de caractères)

help(str) # Pour avoir de la doc python (dans ce cas là ce sera sur str)

#-----------------------------------------------------------------------------------------------------------------------
"""
Une méthode de chaîne travaille sur une copie et pas sur la chaîne elle-même.

str.upper(), str.lower(), str.capitalize(), str.title()
str.center(<largeur>, <caractere_remplissage>)

str.find(<chaine>, <debut>, <fin>)
str.index(<chaine>, <debut>, <fin>)
str.replace(<ancienne>, <nouvelle>, <occurences>)

str.isalpha(), str.isdigit(), str.isdecimal(), str.isnumeric
str.isalphanum()

str.islower(), str.isupper()

str.isidentifier(), str.iskeyword()
"""

ma_chaine = "Bonjour tout le monde"

ma_chaine = ma_chaine.upper()

print(ma_chaine)

#-----------------------------------------------------------------------------------------------------------------------

ma_chaine = "MonSuperProgramme"
print(ma_chaine)

ma_chaine = ma_chaine.center(50, "-")
print(ma_chaine)

#-----------------------------------------------------------------------------------------------------------------------

# Classe str : string (chaînes de caractères)
# Par exemple, pour verifier si "class" est un mot réservé sous Python avec str.isidentifier()
ch = "class"

if ch.isidentifier():
    print("Réservé")
else:
    print("Libre")

#-----------------------------------------------------------------------------------------------------------------------

# Listes

# Création d'une liste

inventaire = list(1, 6, 154, "voiture")
print(inventaire)

inventaire1 = list("arc") * 10
print(inventaire1)

inventaire2 = range(20)
i = 0
while i < len(inventaire2):
    print(inventaire2[i])
    i += 1

#-----------------------------------------------------------------------------------------------------------------------
"""
liste[X] = affiche élément d'indice X
liste[-X] = affiche Xéme élément en partant de la fin

liste[:] = affiche tous les éléments
liste[:X] affiche les X premiers éléments
liste[X:] = affiche les X derniers éléments

liste[A:B]= affiche de l'élément d'indice A à l'élément indice B (exclus)
"""

inventaire3 = ["Arc", "épée", "bouclier", "potion", "armure"]
#Arc : indice 0 (1er élément)
#épée : indice 1 (2eme élémént)
#bouclier : indice 2 (3eme élément)

print(inventaire3[:]) # Affichera la totalité des éléments.
print(inventaire3[0]) # Affichera la chaine de caractére 'arc' qui corresponds à l'indice 0.
print(inventaire3[3:]) # Affichera les trois derniers éléments seulement.
print(inventaire3[-3]) # Affichera le troisiéme élément en partant de la fin.
print(inventaire3[-1]) # Affichera le dernier élément.
# Pour changer l'élément d'un indice

inventaire3[:2] = ["bouclier d'acier"] * 2 #len(inventaire3) pour modifier tous les éléments
print(inventaire3[:])

# Pour vérifier qu'un élément est présent dans la liste
inventaire4 = ["Arc", "épée", "bouclier", "potion", 16]

if "bouclier" in inventaire4:
    print("Je posséde un bouclier.")

else:
    print("Je n'ai pas de bouclier.")

# Les méthodes dans les listes

inventaire5 = []
print(inventaire5[:])

inventaire5.append("Arc") # permet d'ajouter un élément à la liste
print(inventaire5[:])

inventaire6 = ["Arc", "Bouclier", "Manteau de cuir"]
print(inventaire6[:])

inventaire6.insert(1, "Potion de mana") # permet d'insérer un élément entre plusieurs éléments
print(inventaire[:])

inventaire6.remove("Bouclier") # permet de supprimer un élément
print(inventaire6[:])

del inventaire6[1] # permet de supprimer un élément mais cette fois ci avec del
print(inventaire6[:])

objet_a_supprimer = inventaire6.index("Bouclier)") # permet de créer un index et de supprimer l'élément choisi
del inventaire6[objet_a_supprimer]

print(inventaire6[:])

# Création d'une liste de chiffres et pouvoir les trier par ordre croissant

inventaire7 = [7, 3, 54, -3, 90, -245, 445, 26]
print(inventaire7[:])

inventaire7.sort()
print(inventaire7[:])

# ou pour inverser les valeurs

inventaire7 = [7, 3, 54, -3, 90, -245, 445, 26]
print(inventaire7[:])

inventaire7.reverse()
print(inventaire7[:])

# pour compter le nombre d'éléments redondant dans une liste

inventaire8 = ["potion", "arc", "potion", "potion", "manteau"]
print(inventaire8[:])

print("Nombre de potions :", inventaire8.count("potion"))

# pour effacer la liste

inventaire.clear()
print(inventaire[:])

inventaire7[:] = [] # pour effacer la liste aussi
print(inventaire7[:])

# pour séparer/coup une chaîne de caractére en liste

chaine = "Bonjour à tous"
chaine = chaine.split(" ")
print(chaine)

# pour passer d'une liste à une chaîne de caractére

inventaire0 = ["Bonjour", "à", "tous"]
phrase = " ".join(inventaire0)
print(phrase)

# pour effectuer une copie de liste

import copy
liste1 = ["Arc", "cheval", "armure"]
liste2 = copy.deepcopy(liste1)

print("Liste 1", liste1[:])
print("Liste 2", liste2[:])

liste2.append("Potion de mana")

print("Liste 1", liste1[:])
print("Liste 2", liste2[:])

# pour ajouter une liste à une autre

liste3 = ["Arc", "cheval", "armure"]
liste4 = ["potion", "parchemin", "livre"]

print(liste3[:])

liste3.extend(liste4)

print(liste3[:])

# pour énumérer une liste

inventaire9 = ["Arc", "Epee", "Fleches"]
for k, v in enumerate(inventaire9):
    print("Element d'indice {} -> {}".format(k, v))

# Les tuples

liste = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for chose in enumerate(liste):
    print(chose)

"""

Tuple : conteneur immuable (dont on ne peut modifier les valeurs)
Création de tuple : mon_tuple = () #Vide
mon_tuple = 17, #une seule valeur
mon_tuple = (17,) #idem qu'au dessus
mon_tuple = (4, 6) #plusieurs valeurs

Accés aux valeurs : mon_tuple[X] #valeur d'indice X
2 raisons d'utiliser les tuples : affectation multiple de variable
                                  retour multiple de fonction
"""

mon_tuple = (45, 64) #ou sans parenthése (mais moins lisible)
print(mon_tuple[1])

#-----------------------------------------------------------------------------------------------------------------------
# Exemple d'affectation multiple

def get_player_position():
    posX = 159
    posY = 23

    return (posX, posY)

# Programme principal
coordX = 0
coordY = 0

print("Position du joueur : ({}/{})".format(coordX, coordY))

coordX = 156
coordY = 34

print("Position du joueur : ({}/{})".format(coordX, coordY))

# Les dictionnaires
"""
Création de dictionnaire : dico = {} #vide
                           dico = {<cle>:<valeur>, <cle2>:<valeur>}
Accés à une valeur       : dico[<cle>]
Ajout et modification    : dico[<cle>] = <valeur>
Suppression              : dico.pop(<cle>)
                           del dico[<cle>)    
Copie de dictionnaire    : dico1 = {1:11, 2:22}
                         : dico2 = dico1.copy()
"""
dico = {1:"Jason", "prénom":"Jason"}

print(dico[1])
print(dico["prénom"])

#Pour ajouter une valeur à dico

dico["chien"] = "C'est un mammifére, le meilleur ami de l'Homme"

print(dico)

dico.pop("chien")
print(dico)

if 1 in dico:
    print("Oui")
else:
    print("Non")

for key in dico.keys():
    print(key)

for truc in dico.values():
    print(truc)

#-----------------------------------------------------------------------------------------------------------------------

def maFonction(**parametres):
    print(parametres)
maFonction(p=154, nom="blabla")

# Les fichiers

"""
Modes d'ouverture : r (lecture seule)
                    w (écriture avec remplacement)
                    a (écriture avec ajout en fin de fichier)
                    x (lecture et écriture)
                    r+ (lecture/écriture dans un même fichier)
                    
Lecture          : read(), readline(), readlines() # sera considéré comme classe str
"""

fic = open("docs/donnees.txt", "r") #indiquer le chemin du fichier selectionnés
fic.close()

if fic.closed:
    print("Fichier fermé")
else:
    print("Fichier encore ouvert")
    
#------------------------------------------------------------------------------

fic = open("docs/donnees.txt", "r")

content = fic.read()
print(content) #pour lire tout le fichier

#------------------------------------------------------------------------------
# pour récupérer ligne par ligne

fic = open("doc/donnees.txt", "r")

line = fic.readline()
print(line)

line = fic.readline()
print(line)

line = fic.readlines() #permet de récupérer toutes les lignes restantes
print(line)

fic.close()

#------------------------------------------------------------------------------
# syntaxe plus courte pour ne pas oublier la fermeture du fichier
with open("docs/donnees.txt", "r") as fic:
    content = fic.read()
    print(content)
    
    # pas besoin de fermer le fichier avec with

print("Le reste du programme")

#------------------------------------------------------------------------------

# pour écrire dans le fichier

with open("docs/donnees.txt", "w") as fic:
    nombre0 = 34
    fic.write(str(nombre0))
    fic.write("\nBonjour, je suis une chaine de caractére\n")
    fic.write("Et une autre...\n") #\n pour le retour à la ligne sinon les phrases seront écrites à la suite des autres
    
#------------------------------------------------------------------------------

# pour enregistrer un objet en binaire

class Players:
    def __init__(self, name, level):
        self.name = name
        self.level = level
    def whoami(self):
        print("{} ({})".format(self.name, self.level))


p1 = Players("Jaja", 23)
with open("players.data", "wb") as fic: # on ajoute un "b" à la suite du mode écriture "w" pour écrire en mode binaire
    record = pickle.Pickler(fic)
    record.dump(p1)
    
# pour charger l'objet crée en binaire

with open("players.data", "rb") as fic: # on ajoute un "b" à la suite du mode lecture "r" pour lire en mode binaire
    get_record = pickle.Unpickler(fic)
    player_one = get_record.load()

player_one.whoami()

#------------------------------------------------------------------------------

 #Introduction tkinter

import tkinter

#from tkinter import * pour tout importer

mainapp = tkinter.Tk()
mainapp.title("Mon premier programme fenêtré")
mainapp.geometry("800x600")
#mainapp.minsize(640, 480) # pour afficher la fenêtre avec des dimensions minimales
#mainapp.maxsize(1280, 720) # pour afficher la fenêtre avec des dimensions maximales
#mainapp.resizable(width=False, height=False) # pour interdire le redimensionnement
#mainapp.positionfrom("user")
#mainapp.sizefrom("user")
#geometry("XxY+0+0")
#position_X = (largeur_ecran // 2) - (largeur_fenetre // 2) # pour centrer la fenetre en largeur
#position_Y = (hauteur_ecran // 2) - (hauteur_fenetre // 2) # pour centrer la fenetre en hauteur

screen_x = mainapp.winfo_screenmmwidth()
screen_y = mainapp.winfo_screenheight()
window_x = 800
window_y = 600
geo = "{}x{}+{}+{}".format(window_x, window_y, posX, posY)
mainapp.geometry(geo)

mainapp.mainloop()

# Premiéres fonctions

"""
<nom_variable> = <nom_widget>(<widget_parent, <params>...)
"""

import tkinter


app = tkinter.Tk()

message_welcome = tkinter.Message(app, text="Bonjour tout le monde") # affichera le message sur plusieurs lignes
label_welcome = tkinter.Label(app, text="Bienvenue à tous !") # affichera le message sur une seule ligne

label_welcome.config(text="Nouveau message")

print(label_welcome.cget("text")) # pour afficher le 'text' via la console

label_welcome.pack()
app.mainloop()

#------------------------------------------------------------------------------

import tkinter
app = tkinter.Tk()

entry_name = tkinter.Entry(app, width=45) #show pour indiquer à l'écran ce que l'on veut (comme des * pour des mots de passe)

entry_name.pack()
app.mainloop()

#------------------------------------------------------------------------------


import tkinter
app = tkinter.Tk()

entry_name = tkinter.Entry(app, exportselection=0) # pour empêcher que la selection se mette dans le presse papier

entry_name.pack()
app.mainloop()

#------------------------------------------------------------------------------


import tkinter
app = tkinter.Tk()

def hello():
    print("Hello sur le terminal !") # pour afficher ce texte sur le terminal lorque l'user appuie sur OK dans la fenêtre


button_quit = tkinter.Button(app, text="OK", command = hello, width=25)#pour la taille du button ou height
button_quit.pack()
app.mainloop()

#------------------------------------------------------------------------------

"""
showerror
showinfo
showwarning
askquestion
askokcancel
askyesno
askretrycancel
"""

import tkinter
from tkinter import messagebox

def show_modal_window():
    messagebox.showerror("ERREUR", "Un probléme est survenu !")
    
app = tkinter.Tk()
btn = tkinter.Button(app, text="Déclencher une erreur", command=show_model_window)

btn.pack()
app.mainloop()

#------------------------------------------------------------------------------

# Variables contrôles
"""
StringVar() : chaine de caractéres (str)
IntVar() : nombre entier (int)
DoubleVar() : nombre flottant (float)
BooleanVar() : booléen (bool)
"""
import tkinter

# Observateur
def update_label(*args):
    var_label.set(var_entry.get())

# Création et paramétrage de la fenêtre
app = tkinter.Tk()
app.geometry("400x300")
app.title("Variables tkinter")

# Widgets...
var_entry = tkinter.StringVar()
var_entry.trace("w", update_label)
entry = tkinter.Entry(app, textvariable=var_entry)

var_label = tkinter.StringVar()
label = tkinter.Label(app, textvariable=var_label)

label.pack()
entry.pack()



# Boucle principale
app.mainloop()

#------------------------------------------------------------------------------

import tkinter

# Observateur
def update_observer(*args):
    if var_gender.get():
        var_label_gender.set("C'est un homme")
    else:
        var_label_gender.set("C'est une femme")

# Création et paramétrage de la fenêtre
app = tkinter.Tk()
app.geometry("400x300")
app.title("Variables tkinter")

# Widgets...
var_gender = tkinter.IntVar()
var_gender.trace("w", update_observer)
radio1 = tkinter.Radiobutton(app, text="homme", value=1, varible=var_gender)
radio2 = tkinter.Radiobutton(app, text="Femme", value=2, variable=var_gender)

var_label_gender = tkinter.StringVar()
label_gender = tkinter.Label(app, textvariable=var_label_gender)

#trace_vedelete("u", update_observer) pour supprimer l'observateur

radio1.pack()
radio2.pack()
label_gender.pack()


# Boucle principale
app.mainloop()

#------------------------------------------------------------------------------

# Postionnement widgets avec mainframe

import tkinter

# Création et paramétrage de la fenêtre
app = tkinter.Tk()
app.geometry("640x480")
app.title("Variables tkinter")

# Widgets...
mainframe = tkinter.Frame(app, width=300, height=200, borderwidth=1) # pour nommer le cadre écrire 'LabelFrame'
mainframe.pack()

btn = tkinter.Button(app,text="Bienvenue")
btn.pack()

# Boucle principale
app.mainloop()

#------------------------------------------------------------------------------

import tkinter

# Création et paramétrage de la fenêtre
app = tkinter.Tk()
app.geometry("640x480")
app.title("Variables tkinter")

# Widgets...
label = tkinter.Label(app, text="Un label")
ent = tkinter.Entry(app)
btn = tkinter.Button(app,text="Bienvenue")

label.pack(side="top") #bottom pour afficher en bas, right/left
ent.pack(side="top")
btn.pack(expand=1) #pour que le widget occupe l'espace restant
#btn.pack(side="left", fill"y") # remplira l'espace y a gauche
#btn.pack(padx=10, pady=5) pour régler les bordures 
# Boucle principale
app.mainloop()

#------------------------------------------------------------------------------
import tkinter
"""
Options Sticky :
n = nord
s = sud
e = est
w = ouest
"""
# Création et paramétrage de la fenêtre
app = tkinter.Tk()
app.geometry("640x480")
app.title("Variables tkinter")

# Widgets...
label = tkinter.Label(app, text="Un label")
ent = tkinter.Entry(app)
btn = tkinter.Button(app,text="Bienvenue")

label.grid(row=0, column=0, columspan=2, rowspan=3) # on considére que notre fenétre est tableau, et permet de positionner nos éléments
ent.grid(row=0, column=1)
btn.grid(row=0, column=3)

# Boucle principale
app.mainloop()

#------------------------------------------------------------------------------

# Création de menu sous tkinter

"""
# add_checkbutton()
# add_separator()
# add_radiobutton()
"""

import tkinter


def about():
    about_window = tkinter.Toplevel(app)
    about_window.title("A propos")
    lb = tkinter.Label(about_window, text="Bonjour")
    
def hello():
    print("Coucou !")

# Création et paramétrage de la fenêtre
app = tkinter.Tk()
app.geometry("640x480")
app.title("Variables tkinter")

# Widgets...
mainmenu = tkinter.Menu(app)

first_menu = tkinter.Menu(mainmenu, tearoff=0) 
first_menu.add_command(label="Option1", command=hello)
first_menu.add_command(label="Option2")
first_menu.add_command(label="Quitter", command=app.quit)

second_menu = tkinter.Menu(mainmenu)
second_menu.add_command(label="Commande1")
second_menu.add_command(label="A propos", command=about)

mainmenu.add_cascade(label="Premier", menu=first_menu)
mainmenu.add_cascade(label="Second", menu=second_menu)



# Boucle principale
app.config(menu=mainmenu)
app.mainloop()

#------------------------------------------------------------------------------

# Gestion temps

import time

print("Le 1er texte")

time.sleep(5) #permet au processus de se mettre en pause pendant 5 sec

print("Le 2nd texte")

#------------------------------------------------------------------------------

import time

# 1er Janvier 1970 à 00h00 = Epoch (date de référence pour l'informatique)

begin = time.time()
print("Début")

time.sleep(5)

end = time.time()
print("Fin")

print(f"Temps exécuté : {end - begin}s")

#------------------------------------------------------------------------------
"""
                localtime()
(TIMESTAMP)---------------------> structure de temps
           <---------------------                     
                mktime()
"""
import time

tps = time.localtime()
print(tps)

tps = time.mktime(tps)
print(tps)

#------------------------------------------------------------------------------

import time

"""
%d : jour(01 à 31)
%m : mois (01 à 12)
%Y : année (ex : 2023 - %y - 00 à 99)
%H : heure (00 à 23)
%I : minutes (00 à 59)
%S : secondes (00 à 59)
%p : AM/PM

%A : jour semaine / %a (jour abrégé)
%B: mois / %b (mois abrégé)

%Z : fuseau horaire (timezone)  
"""


my_time = time.strftime("%d/%m/%Y")

#------------------------------------------------------------------------------

# Gestion dates

import datetime

d1 = datetime.datetime(2023, 8, 26, 11, 16, 43)
print(d1)

d2 = datetime.datetime(2023, 8, 26, 11, 17, 33)
if d1 < d2:
    print("d1 est plus ancien que d2")
else:
    print("d1 est plus récent que d2")

print(d1.year) #pour récupérer l'année (seulement) de d1

#------------------------------------------------------------------------------

import datetime

t1 = datetime.time(23, 00, 45)
print(t1) # permet d'afficher l'heure indiqué au dessus

print(datetime.now())

#------------------------------------------------------------------------------

import datetime
from datetime import date

now = date.today()
born = datetime.date(1991, 2, 14)
print(f"{now.year - born.year} ans.")

#-----------------------------------------------------------------------------------------------------------------------

# Programmation asynchrone
import time
import threading

class MyProcess(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        
    def run(self):
        i = 0
        while i < 3:
            print(threading.current_thread())
            time.sleep(0.3)
            i += 1


thread1 = MyProcess()
thread2 = MyProcess()

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Fin du programme")

#------------------------------------------------------------------------------

# Les processus bloquants

import time
import threading


my_lock = threading.RLock()

class MyProcess(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        
    def run(self):
        i = 0
        while i < 3:
            with my_lock:
                letterss = "ABC"
                for lt in letterss:
                    print(lt)
                time.sleep(0.3)
            i += 1


thread1 = MyProcess()
thread2 = MyProcess()

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Fin du programme")

#------------------------------------------------------------------------------

# Serveur HTTP et page web
"""
Côté serveur
"""
import http.server
import socketserver

port = 80
address = ("", port)

server = http.server.HTTPServer
handler = http.server.CGIHTTPRequestHandler
handler.cgi_directories = ["/"]
httpd = server(address, handler)

print(f"Serveur démarré sur le port {port}")

httpd.serve_forever()

"""
Côté client
"""

#index.py

import cgi

print("Content-type: text/html; charset=utf-8\n")
html = """<!DOCTYPE html>
<head>
    <meta charset="utf-8">
    <title>Ma page Web</title>
</head>
<body>
    <h1>Bonjour !</h1>
    <p>bla bla bla</p>
</body>
</html>
"""

print("<h1>Bonjour</h1>")
    <p>bla bla bla</p>
</body>
</html>
"""

print("<h1>Bonjour</h1>")

#------------------------------------------------------------------------------

# Données formulaires

import cgi

print("Content-type: text/html; charset=utf-8\n")
html = """<!DOCTYPE html>
<head>
    <meta charset="utf-8">
    <title>Ma page Web</title>
</head>
<body>
    <h1>Ma page web Python avec CGI</h1>
    
    <form method="post" action="result.py">
        <p><input type>="text" name="username">
        <input type="submit" value="Envoyer"></p>
    </form>
</body>
</html>
"""

# result.py

import cgi
import cgitb

cgitb.enable()
form = cgi.FieldStorage()

if form.getvalue("username"):
    username = form.getvalue("username")
else:
    raise Exception("Pseudo non transmis")

html = """<!DOCTYPE html>
<head>
    <meta charset="utf-8">
    <title>Ma page Web</title>
</head>
<body>
    <h1>Page de résultat</h1>
    """
print(html)
print(f"Bonjour {username}")
html = """
</body>
</html>
"""
print(html)

#------------------------------------------------------------------------------

# Les cookies

import cgi
import http.cookies
import datetime
import os
import sys
import codecs

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

"""
expires
path
comment
domain
secure
version
httponly

print("Set-Cookie : pref_lang=fr; httponly") # pour intégrer les cookies
expiration = datetime.datetime.now() + datetime.timedelta(days=365) # pour intégrér les cookies il est préférable de créer des dictionnaires
expiration = expiration.strftime("%a, %d-%b-%Y %H:%M:%S")
my_cooki = http.cookies.SimpleCookie()
my_cookie["pref_lang"] = "fr"
my_cookie["pref_lang"]["expires"] = expiration
my_cookie["pref_lang"]["httponly"] = True
"""
print("Set-Cookie : pref_lang=fr; httponly")

print("Content-type: text/html; charset=utf-8\n")
print(my_cookie.output())
html = """<!DOCTYPE html>
<head>
    <meta charset="utf-8">
    <title>Ma page Web</title>
</head>
<body>
    <h1>Cookies avec Python</h1>
"""
print(html)

try:
    user_lang = http.cookies.SimpleCookie(os.environ["HTTP_COOKIE"])
    print(user_lang["pref_lang"].value)
except(http.cookies.CookieError, KeyError):
    print("Not find")

html = """
</body>
</html>
"""
print(html)

#-----------------------------------------------------------------------------------------------------------------------

# Base de données (avec DB Browser SqLite)
import sqlite3
# CRUD : Create, Read, Update, Delete
connection = sqlite3.connect("base.db")
cursor = connection.cursor()

my_username = ("Jason",)
cursor.execute('SELECT * FROM tt_users WHERE user_name = ?', my_username)
result = cursor.fetchone()[1]
print(f"Le nom d'utilisateur est : {result}")

connecion.close()

#-----------------------------------------------------------------------------------------------------------------------
import sqlite3

connection = sqlite3.connect("base.db")
cursor = connection.cursor()

new_user = (cursor.lastrowid, "Julie", 23)
cursor.execute('INSERT INTO tt_users VALUES(?,?,?)', new_user)
connection.commit()
print("Nouvel utilisateur ajouté!")

connection.close()

#-----------------------------------------------------------------------------------------------------------------------
import sqlite3

connection = sqlite3.connect("base.db")
cursor = connection.cursor()

req = cursor.execute('SELECT * FROM tt_users')

for row in req.fetchall():
    print(row[1]
except Exception as e:
    print("[ERREUR]", e)
    connection.rollback()
finally:
    connection.close()

#-----------------------------------------------------------------------------------------------------------------------

# Les sockets (software)
#server.py (par exemple, pour serveur)
import socket
import threading

class ThreadForClient(threading.Thread):
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.conn = client

    def run(self):
        data = self.conn.recv(1024)
        data = data.decode("utf8")
        print(data)

host, port =('', 5566)

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((host, port))
print("Serveur démarré")

while True:
    socket.listen(5)
    conn, address = socket.accept()
    print("En écoute...")

    my_thread = ThreadForClient(conn)
    my_thread.start()

    data = conn.recv(1024)
    data = data.decode("utf8")
    print(data)

conn.close()
socket.close()

#----------------------------------------------------------------------------------------------------------------------
#client.py (par exemple, pour client)

import socket

host, port = ('localhost', 5566)
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    socket.connect((host, port))
    print("Client connecté")

    data = "Bonjour à toi, je suis le client ^^!"
    data = data.encode("utf8")
    socket.sendall(data)


except ConnectionRefusedError:
    print("Connexion au serveur échouée !")
finally:
    socket.close()

#-----------------------------------------------------------------------------------------------------------------------
#Introduction pygame

import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))

launched = True

while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False

#Premiére fenêtre

import pygame
"""
pygame.FULLSCREEN (plein écran)
pygame.RESIZABLE 
pygame.NOFRAME

pygame.OPENGL
pygame.HWSURFACE (accélération matérielle)
pygame.DOUBLEBUF
"""
res = (640, 480)

pygame.init()
pygame.display.set_caption("TITRE DE LA FENETRE")
window_surface = pygame.display.set_mode(res, pygame.RESIZABLE | pygame.NOFRAME)

print(pygame.display.Info())
#print(pygame.get_sdl_version()) pour check la version de SDL
launched = True
while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False

pygame.quit() #pour refaire une initialisation, sinon Python quit lui même

#-----------------------------------------------------------------------------------------------------------------------
# Dessiner une surface

import pygame
"""
 Surface, rect
 Rect(left, top, width, height)
"""
pygame.init()

window_resolution = (640, 480)
blue_color = (89, 152, 255)
black_color = (0, 0, 0)
pygame.display.set_caption("Python #36")

window_surface = pygame.display.set_mode(window_resolution)
window_surface.fill(blue_color)
coords = [(10,10), (100,10), (30, 50), (50,40)]


pygame.draw.line(window_surface, black_color, [10, 10],[100, 100] )
#rect_form = pygameRect(10, 10, 150, 65)
#pygame.draw.rect(window_surface, black_color, rect_form)
#pygame.draw.circle(window_surface, black_color,[150, 100], 50)
#pygame.draw.polygon(window_surface, black_color, coords)

pygame.display.flip()

launched = True
while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
#-----------------------------------------------------------------------------------------------------------------------

# Afficher images

import pygame

pygame.init()
window_resolution = (640, 480)
blank_color = (255, 255, 255)
black_color = (0, 0, 0)

pygame.display.set_caption("Python 37")
window_surface = pygame.display.set_mode(window_resolution)

cat_image = pygame.image.load("cat.jpg")
cat_image.convert()
cat_image.set_colorkey(blank_color) # pour mettre en transparence la zone choisie

launched = True
while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False

    # Corps du programme
    window_surface.fill(blank_color)
    window_surface.blit(cat_image, [10, 10])
    pygame.display.flip()

#-----------------------------------------------------------------------------------------------------------------------

# L'objet Rect

import pygame
import time

"""
pygame.Rect(x, y, width, height)
Rect.copy()
Rect.move() | Rect.move_ip()
Rect.inflate()
Rect.coliderect()

"""

pygame.init()
window_resolution = (640, 480)
black_color = (0, 0, 0)
red = (255, 0, 0)
i = 0

pygame.display.set_caption("Python 38")
window_surface = pygame.display.set_mode(window_resolution)

myrect = pygame.Rect(10, 10, 250, 80)
myblock = pygame.Rect(600, 50, 20, 300)
pygame.draw.rect(window_surface, red, myrect)
pygame.draw.rect(window_surface, blue_color, myblock)
pygame.display.flip()

while not myrect.colliderect(myblock):
    time.sleep(.010) # 10 millisecondes
    window_surface.fill(black_color)
    myrect.x += 1
    pygame.draw.rect(window_surface, red, myrect)
    pygame.draw.rect(window_surface, blue_color, myblock)
    pygame.display.flip()

launched = True
while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False

#-----------------------------------------------------------------------------------------------------------------------

#Afficher du texte

import pygame

"""
arial_font.set_bold() texte en gras
arial_font.set_italic() texte en italique
arial_font.set_underline() texte surligné
"""

pygame.init()
window_resolution = (640, 480)

pygame.display.set_caption("Python 39")
window_surface = pygame.display.set_mode(window_resolution)

arial_font = pygame.font.SysFont("arial", 20)
hello_text_surface = arial_font.render("Hello World ! ", False, blue_color)


window_surface.blit(hello_text_surface, [10, 10])
pygame.display.flip()

# récupére le nom des font et l'affiche en console print(pygame.font.get_fonts())

launched = True
while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False

# pour charger un fichier font : pygame.font.Font("XXXXXXX.ttf", 10)

#-----------------------------------------------------------------------------------------------------------------------

# Evenements

import pygame
"""
QUIT ==> none
ACTIVEEVENT ==> gain, state
KEYDOWN ==> unicode, key, mod
KEYUP ==> key, mod
MOUSEMOTION ==> pos, rel, buttons
MOUSEBUTTONUP ==> pos, button
MOUSEBUTTONDOWN ==> pos, button
JOYAXISMOTION ==> joy, axis, value
JOYBALLMOTION ==> joy, ball, rel
JOYHATMOTION ==> joy, hat, value
JOYBUTTONUP ==> joy, button
JOYBUTTONDOWN ==> joy, button
VIDEORESIZE ==> size, w, h
VIDEOEXPOSE ==> none
USEREVENT ==> code
"""
window_resolution = (640, 480)

pygame.init()
pygame.display.set_caption("Python 40")
window_surface = pygame.display.set_mode(window_resolution)


arial_font = pygame.font.SysFont("arial", 30)
dimensions_text = arial_font.render("{}".format(window_resolution), True, while_color)
window_surface.blit(dimensions_text, [10, 10])

pygame.display.flip()

launched = True
while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT():
            launched = False
        elif event.type == pygame.VIDEORESIZE:
            window_surface.fill(black_color)
            dimensions_text = arial_font.render("{}x{}".format(event.w, event.h), True, while_color)
            window_surface.blit(dimensions_text, [10, 10])
            pygame.display.flip()

#-----------------------------------------------------------------------------------------------------------------------

pygame.init()
pygame.display.set_caption("Python 40")
window_surface = pygame.display.set_mode(window_resolution)

pygame.display.flip()

launched = True
while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT():
            launched = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print("HAUT")
            elif event.key == pygame.K_DOWN:
                print("BAS")
            elif event.key == pygame.K_LEFT:
                print("GAUCHE")
            elif event.key == pygame.K_RIGHT:
                print("DROITE")
            else:
                print("AUTRE TOUCHE...")

#-----------------------------------------------------------------------------------------------------------------------

pygame.init()
pygame.display.set_caption("Python 40")
window_surface = pygame.display.set_mode(window_resolution)

pygame.display.flip()

launched = True
while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT():
            launched = False
        elif event.type == pygame.MOUSEMOTION:
            print("{}".format(event.pos))

#-----------------------------------------------------------------------------------------------------------------------

# Mesurer le temps

import pygame

window_resolution = (640, 480)
black_color = (0, 0, 0)
blue_color = (132, 180, 255)
launched = True

pygame.init()
#clock = pygame.time.Clock()
#pygame.time.set_timer(pygame.USEREVENT, 2000)

pygame.display.set_caption("Python 41")
window_surface = pygame.display.set_mode(window_resolution)
arial_font = pygame.font.SysFont("arial", 36)
text = arial_font.render("Bjr les gens !", True, blue_color)

#pygame.time.wait(2000) permet d'endormir le programme pdt 2 secondes
#pygame.delay(5000) permet d'endormir le programme pdt 5 secondes via le processeur
print(pygame.time.get_ticks())

window_surface.blit(text, [50, 50])
pygame.display.flip()

while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
        elif event.type == pygame.USEREVENT:
            window_surface.fill(black_color)
            print(f"{clock.get_fps():.2f} FPS")
            window_surface.blit(dimensions_text, [10, 10])
            pygame.display.flip()

    clock.tick(30) 30 fps

#-----------------------------------------------------------------------------------------------------------------------

import pygame
"""
<Sound>.play(loop = 0, time = 0, fadein = 2000)
       .stop()
       .fadeout(ms)
       .set_volume(0.0 -> 1.0)
       .get_volume()
       .get_length()
       
Pour utiliser le fichier audio en streaming : 

pygame.mixer.music.load("song.ogg")
pygame.mixer.music.play()
"""
window_resolution = (640, 480)
launched = True

pygame.init()
pygame.display.set_caption("Python 42")
window_surface = pygame.display.set_mode(window_resolution)

song = pygame.mixer.Sound("celtic.ogg")
song.play()

pygame.display.flip()

while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False

#-----------------------------TERMINE-----------------------------------------------------------------------------------
