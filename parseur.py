import os
import sys
import shutil
import re

if(len(sys.argv) < 2):
    print('Erreur : il faut entrer un argument : le nom du dossier contenant les fichier à traiter')
    exit()


if(len(sys.argv) >= 3):
    if(sys.argv[1].startswith('-')):
        option = sys.argv[1]
        dossier = sys.argv[2]
    elif(sys.argv[2].startswith('-')):
        option = sys.argv[2]
        dossier = sys.argv[1]
    else: #Si il y a 2 arguments mais qu'on n'a pas d'option
        option = '-x' #Par défaut on renvoie au format xml
        dossier = sys.argv[1] #On prend le premier argument comme le nom du fichier
else:
    option = '-x' #Par défaut on renvoie au format xml
    dossier = sys.argv[1]
    
if not (option == '-t' or option == '-x'):
    print('Erreur : option ' + option + ' inconnue')
    exit()
    
if not os.path.isdir(dossier):
    print('Erreur : le dossier "' + dossier + '" n\'existe pas')
    exit()
    
dossier_resultat = dossier+'/parseur_resultat'
if os.path.isdir(dossier_resultat):
    shutil.rmtree(dossier_resultat)
os.mkdir(dossier_resultat)


listfic = os.listdir(dossier)
for fic in listfic:
    
        if fic[-4:] == '.txt':
            
            fd = open(dossier + "/" + fic, "r")
            
            fs = open(dossier_resultat + "/" + fic[:-4] + '_information.txt', "w") 
            
            if(option == '-x'):
                fs.write('<article>\n')
            
            if(option == '-x'):
                fs.write('\t<preamble> ')
            else:
                fs.write('Nom du fichier : ')
            #Récuperation nom du fichier
            fs.write(fic)
            if(option == '-x'):
                fs.write(' </preamble>')
            fs.write('\n')
            
            if(option == '-x'):
                fs.write('\t<titre> ')
            else:
                fs.write('Titre : ')
            #Récuperation titre
            Lec = fd.readline()
            fs.write(Lec.replace('\n', ''))
            if(option == '-x'):
                fs.write(' </titre>')
            fs.write('\n')
            
            #Récuperation auteurs
            
            
            #Récupération résumé
            while(Lec.lower().find('abstract') != 0 and Lec !=''):
                Lec = fd.readline()
            if(Lec != ''):
                if(option == '-x'):
                    fs.write('\t<abstract> ')
                else:
                    fs.write('Résumé : \n')
                fs.write(re.sub('^abstract', '', Lec, flags=re.IGNORECASE).replace('\n', ' '))
                Lec = fd.readline()
                while(Lec.find('\n') == 0):
                    Lec = fd.readline()
                while(Lec.find('\n')>0 and Lec !=''):
                    if(option == '-x'):
                        fs.write(Lec.replace('\n', ' '))
                    else:
                        fs.write(Lec)
                    Lec = fd.readline()
                if(option == '-x'):
                    fs.write('<abstract>')
                fs.write('\n')
            else:
                if(option == '-t'):
                    fs.write('Pas de résumé')
                    
                    
            #Récuperation bibliographie
            
            
            if(option == '-x'):
                fs.write('</article>')
                
            fd.close()
            fs.close()
            
            
