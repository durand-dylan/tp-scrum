import os
import sys
import shutil

dossier_resultat = sys.argv[1]+'/parseur_resultat'

if os.path.isdir(dossier_resultat):
    shutil.rmtree(dossier_resultat)
os.mkdir(dossier_resultat)


listfic = os.listdir(sys.argv[1])
for fic in listfic:
    print(fic)
