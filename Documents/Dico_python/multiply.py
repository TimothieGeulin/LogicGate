"""module multipli contenant la fonction table"""

import os

def table(nb, max=10):
    """Fonction affichant la table de multiplication par nb de
    1 * nb jusqu'a max * nb"""
    i = 0
    while i < max:
        print(i + 1, "*", nb, "=", (i + 1) * nb)
        i += 1


# test de la fonction table
# ne s'execute que si on execute le fichier multiply (tt seul)
if __name__ == "__main__":
    table(4)
    #os.system("pause")
