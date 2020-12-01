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
            fs = open(dossier + "/" + fic, "r")
            
            if(option == '-x'):
                fd = open(dossier_resultat + "/" + fic[:-4] + '_information.xml', "w") 
            else:
                fd = open(dossier_resultat + "/" + fic[:-4] + '_information.txt', "w") 
                
            #Récuperation nom du fichier
            if(option == '-x'):
                fd.write('<article>\n')
            
            if(option == '-x'):
                fd.write('\t<preamble> ')
            else:
                fd.write('Nom du fichier : ')
            fd.write(fic)
            if(option == '-x'):
                fd.write(' </preamble>')
            fd.write('\n')
            
            #Récuperation titre
            if(option == '-x'):
                fd.write('\t<titre> ')
            else:
                fd.write('\nTitre : ')
            Lec = fs.readline()
            fd.write(Lec.replace('\n', '').replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;'))
            if(option == '-x'):
                fd.write(' </titre>')
            fd.write('\n')
            
            #Récuperation auteurs
            authorFound = False
            while('abstract' not in Lec.lower() and Lec !=''):
                Lec = fs.readline()
                if('@' in Lec):
                    if(authorFound == False):
                        if(option == '-x'):
                            fd.write('\t<author>\n')
                        else:
                            fd.write('\nAuteur(s) : \n')
                        authorFound = True
                    else:
                        fd.write('; \n')
                    nom_prenom = Lec.rsplit('@')[0]
                    nom_prenom = nom_prenom.rsplit(' ')
                    nom_prenom = nom_prenom[len(nom_prenom) - 1]
                    nom_prenom = nom_prenom.rsplit('.')
                    if(option == '-x'):
                        fd.write('\t\t')
                    fd.write(nom_prenom[0].capitalize())
                    if(len(nom_prenom) > 1):
                        fd.write(' ' + nom_prenom[1].capitalize())
                    Email = Lec.rsplit(' ')
                    Email = Email[len(Email) - 1]
                    fd.write(' | Email : ' + Email.replace('\n', '').replace(',', ''))
            if(authorFound == True):
                if(option == '-x'):
                    fd.write('\n\t</author>')
                fd.write('\n')
            elif(option == '-t'):
                fd.write('\nAucun auteur trouvé\n')
            
            #Récupération résumé
            while(Lec.lower().find('abstract') != 0 and Lec !=''):
                Lec = fs.readline()
            if(Lec != ''):
                if(option == '-x'):
                    fd.write('\t<abstract>')
                else:
                    fd.write('\nRésumé :')
                fd.write(re.sub('^abstract', '\n', Lec.replace('\n', ''), flags=re.IGNORECASE))
                Lec = fs.readline()
                while(Lec.find('\n') == 0):
                    Lec = fs.readline()
                while(Lec.find('\n')>0 and Lec !=''):
                    if(option == '-x'):
                        fd.write('\t\t' + Lec.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;'))
                    else:
                        fd.write(Lec)
                    Lec = fs.readline()
                if(option == '-x'):
                    fd.write('\t</abstract>')
                fd.write('\n')
            else:
                if(option == '-t'):
                    fd.write('\nPas de résumé\n')
                fs.seek(0,0)
                Lec = fs.readline()
            
            #Récuperation bibliographie
            while(Lec.lower().find('references') != 1 and Lec.lower().find('references') != 0 and Lec !=''):
                Lec = fs.readline()
            if(Lec != ''):
                if(option == '-x'):
                    fd.write('\t<biblio>')
                else:
                    fd.write('\nBibliographie :')
                fd.write(re.sub('references', '\n', Lec.replace('\n', ''), flags=re.IGNORECASE))
                Lec = fs.readline()
                while(Lec.find('\n') == 0):
                    Lec = fs.readline()
                while(Lec !=''):
                    if(option == '-x'):
                        fd.write('\t\t' + Lec.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;'))
                    else:
                        fd.write(Lec)
                    Lec = fs.readline()
                if(option == '-x'):
                    fd.write('\n\t</biblio>')
                fd.write('\n')
            else:
                if(option == '-t'):
                    fd.write('\nPas de bibliographie')
            

            if(option == '-x'):
                fd.write('</article>')

            fd.close()
            fs.close()
