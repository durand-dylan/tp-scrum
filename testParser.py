
import os,sys
	
def main():

	
	path = ''
	if(len(sys.argv)>1):
		path = sys.argv[1]		
	path = os.path.abspath(path)
	#faut d'abord crée un dossier ou stocker les info 
	
	enr = os.listdir(path)
	for ft in enr:
		Tit = ''
		Par = ''
		if ft[-4:] == '.txt':
			
			
			fil = open(path+'/'+ft, "r")
			
			 
			fo = open('fichierstxtParsee/'+ft[:-4]+'information.txt',"w") 
			
						
			fo.write('Nom du fichier : '+ft[:-4]+'\n')
			
			#Récuperation titre		
			Lec = fil.readline()
			while(Lec.find('\n')>0):
				Tit = Tit + Lec[:-1]
				Lec = fil.readline()	
			fo.write('Title : '+ Tit +'\n')
			
			#Résumé
			fo.write('Resume : \n')
			while(Lec.lower().find('abstract')!=0 and Lec !=''):
				Lec = fil.readline()
			fo.write(Lec[:-1])
			Lec = fil.readline()
			while(Lec.find('\n') == 0):
				Lec = fil.readline()
			while(Lec.find('\n')>0 and Lec !=''):
				o = -1
				if(Lec[-2] =='-'):
					o = -2
				Par = Par + Lec[:o]
				Lec = fil.readline()
			
			fo.write(Par)
			
			fil.close()
			fo.close()
			

if __name__ == '__main__':
	main()
			

			
