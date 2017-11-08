import os # On importe le module os qui dispose de variables 
          # et de fonctions utiles pour dialoguer avec votre 
          # systeme d'exploitation
          
########################################################################

# IF
a=4
if a > 0 :
	print# ("a > 0")
elif  a<=0 :
	print# ("a <= 0");

########################################################################

# ENTREE STANDARD
#annee = int (input ("fais toi plaiz :) :"))
#print (annee)
#print (type (annee))

########################################################################

# BOUCLE WHILE
i=0
while i<10 :
	i+=1
#print (i)

########################################################################

# BOUCLE FOR (attention un peu differente des autres langages)
chaine = "bonjour"
for lettre in chaine :
	print# (lettre)

########################################################################

# FONCTION
def new_fonction (nb) :
	i=0
	while i<10:
		# print (i+1, '*', nb, '=', (i+1) * nb)
		i += 1		
new_fonction(4)

########################################################################

# FONCTION AVEC RETOUR
def new_fonction2 (nb) :
	i= 2 * nb
	return i
# print (new_fonction2 (2))

########################################################################

# FONCTIONS LAMBDA
f = lambda x: x*x
#print f(5)

########################################################################

# IMPORT
import math
#print math.sqrt(4)

########################################################################

# DOC
#help ("math")

########################################################################
	
# IMPORT (bonus)
import math as mathematiques
#print mathematiques.sqrt(4)

from math import sqrt
#print (sqrt (16))

# On met le programme en pause pour eviter qu'il ne se referme (Windows)
# os.system("pause")

########################################################################

# IMPORT "HEADERS"
from multiply import *
# test de la fonction table
#table(3, 20)
#print

########################################################################

# EXCEPTIONS
# TODO

########################################################################

# CLASS methodes

chaine = "NE CRIE PAS SI FORT !"
#print chaine.lower() # Mettre la chaine en minuscule

minuscules = "une chaine en minuscules"
#print minuscules.upper() # Mettre en majuscules

#print minuscules.capitalize() # La premiere lettre en majuscule

espaces = "   une  chaine avec  des espaces   "
#print espaces.strip() # On retire les espaces au debut et a la fin de la chaine

titre = "introduction"
#print titre.upper().center(20)

########################################################################

# Suite  TODO






























		
