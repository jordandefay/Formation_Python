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
#CE que l'on a vu :
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
#          : classe Chat hérite de la classe Animal (Chat est une sorte d'Animal)
