import requests
import time

def getPark(idPark:str,path="."):
	response=requests.get(f"https://data.montpellier3m.fr/sites/default/files/ressources/{idPark}.xml") #Acquision du fichier xml du parking grâce à la variable idPark qui renseigne l'identifiant du parking
	file=open(f"{path}/{idPark}_{int(time.time())}.xml","w+", encoding="UTF-8") #Création d'un fichier pour stocker le contenu du fichier .xml téléchargé, si l'utilisateur veut enregistrer le fichier dans un répertoire particulier, il peut renseigner la variable ``path`` par défaut, la fonction sauvergarde le fichier dans le même répertoire que le programme
	file.write(response.text) #Ecriture du ficher
	file.close() #Fermeture de l'instance de fichier
	return file.name #On retourne le chemin du fichier.

def getCycle(path="."):
	response=requests.get("https://montpellier-fr-smoove.klervi.net/gbfs/en/station_status.json") #Acquisition du fichier json représentant l'état de toutes les stations velaMag
	file=open(f"{path}/veloMag_{int(time.time())}.json","w+", encoding="UTF-8")#Création d'un fichier pour stocker le contenu du fichier .json téléchargé, si l'utilisateur veut enregistrer le fichier dans un répertoire particulier, il peut renseigner la variable ``path`` par défaut, la fonction sauvergarde le fichier dans le même répertoire que le programme
	file.write(response.text) #Ecriture du fichier
	file.close() #Fermeture de l'instance du fichier
	return file.name #On retourne le chemin du ficher

def getInfos(path="."):
	#Dictionnaire contenant les URLs des stations liés au moyen de transport 
	urls = {"tram":"https://data.montpellier3m.fr/sites/default/files/ressources/MMM_MMM_ArretsTram.json","veloMag":"https://montpellier-fr-smoove.klervi.net/gbfs/en/station_information.json"}
	files=[] #Liste qui contiendra les deux fichiers d'informations récupérés
	for key in urls.keys: #Boucle pour les deux urls
		response=requests.get(urls[key]) #Récupération du fichier
		file=open(f"{path}/{key}.json","w+", encoding="UTF-8") #Création des fichiers .json avec les informations
		file.write(response.text) #Ecriture du fichier
		file.close() #Fermeture de l'instance du fichier
		files.append(file.name)#On ajoute le chemin d'accès au fichier dans la liste 
	return files #On retourne la liste contenant les deux fichiers

class parking:
	def __init__(self,parkID,open,free,total):
		self._time=time
		self._parkID=parkID
		self._open=open
		self._free=free
		self._total=total
	
	#défintion des getter et setters des attributs
	@property
	def time(self):
		return self.time
	@time.setter
	def time(self,time):
		#check si time est bien un entier
		if type(time) == int:
			self._time == time
		else:
			raise TypeError("time type must be an int !")
	

	@property
	def parkID(self):
		return self._parkID
	@parkID.setter
	def parkID(self,parkID):
		#check si parkID est bien dans les id disponibles sur le site opendata
		if parkID in ['FR_MTP_ANTI','FR_MTP_COME','FR_MTP_CORU','FR_MTP_EURO','FR_MTP_FOCH','FR_MTP_GAMB','FR_MTP_GARE','FR_MTP_TRIA','FR_MTP_ARCT','FR_MTP_PITO','FR_MTP_CIRC','FR_MTP_SABI','FR_MTP_GARC','FR_CAS_SABL','FR_MTP_MOSS','FR_STJ_SJLC','FR_MTP_MEDC','FR_MTP_OCCI','FR_CAS_VICA','FR_MTP_GA109','FR_MTP_GA250','FR_CAS_CDGA','FR_MTP_ARCE','FR_MTP_POLY']:
			self._parkID=parkID
		else:
			raise ValueError("parkID is not valid !")
	
	@property
	def open(self):
		return self._open
	@open.setter
	def open(self,open):
		#check si open est bien un booléen
		if type(open)==bool:
			self._open=open
		else:
			raise TypeError("open type must be a bool !")

	@property
	def free(self):
		return self._free
	@free.setter
	def free(self,free):
		#check si free est bien un int
		if type(free) == int:
			self._free=free
		else:
			raise TypeError("free must be an int !")
	@property
	def total(self):
		return self._total 
	@total.setter
	def total(self,total):
		#check si total est bien un int
		if type(total)==int:
			self._total==total
		else:
			raise TypeError("total must be an int !")
	

