# tp-scrum

Lancer le parseur avec la commande :
```python
python3 parseur.py (-x|-t) pathToDirectory
```
"pathToDirectory" est le chemin vers le dossier dans lequel se trouvent les fichiers txt à parser.
Le résultat du parsing est enregistré dans le dossier dossier_resultat (qui se trouve lui même dans le dossier contenant les fichier (pathToDirectory)).

option -x : format xml

option -t : format txt

option par défaut : -x (xml)

Possibilité de mettre l'option avant ou après le nom du fichier

Menu textuel au début du programme pour choisir si on veut parser tout le dossier 

Si on ne veut pas parser tout le dossier, menu pour choisir les fichiers à parser un par un
