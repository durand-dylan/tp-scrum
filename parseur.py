import os
import sys
import shutil
import re

if(len(sys.argv) < 2):
	print('Il faut entrer un argument : le nom du dossier contenant les fichier à traiter')
	exit()

dossier_resultat = sys.argv[1]+'/parseur_resultat'

if os.path.isdir(dossier_resultat):
	shutil.rmtree(dossier_resultat)
os.mkdir(dossier_resultat)


listfic = os.listdir(sys.argv[1])
for fic in listfic:
	
		if fic[-4:] == '.txt':
			
			fd = open(sys.argv[1] + "/" + fic, "r")
			
			 
			fs = open(dossier_resultat + "/" + fic[:-4] + '_information.txt', "w") 
			
						
			fs.write('Nom du fichier : ' + fic + '\n')
			
			#Récuperation titre
			Lec = fd.readline()
			fs.write('Titre : ')
			fs.write(Lec)
			
			#Résumé
			Par = ''
			while(Lec.lower().find('abstract') != 0 and Lec !=''):
				Lec = fd.readline()
			if(Lec != ''):
				fs.write('Résumé : \n')
				fs.write(re.sub('^abstract', '', Lec, flags=re.IGNORECASE))
				Lec = fd.readline()
				while(Lec.find('\n') == 0):
					Lec = fd.readline()
				while(Lec.find('\n')>0 and Lec !=''):
					fs.write(Lec)
					Lec = fd.readline()
			else:
				fs.write('Pas de résumé')
			
			fd.close()
			fs.close()
