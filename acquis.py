import requests
import time
from lxml import etree
from io import StringIO
import json

def getParkFile(idPark:str,path="."):
	response=requests.get(f"https://data.montpellier3m.fr/sites/default/files/ressources/{idPark}.xml") #Acquision du fichier xml du parking grâce à la variable idPark qui renseigne l'identifiant du parking
	file=open(f"{path}/{idPark}_{int(time.time())}.xml","w+", encoding="UTF-8") #Création d'un fichier pour stocker le contenu du fichier .xml téléchargé, si l'utilisateur veut enregistrer le fichier dans un répertoire particulier, il peut renseigner la variable ``path`` par défaut, la fonction sauvergarde le fichier dans le même répertoire que le programme
	file.write(response.text) #Ecriture du ficher
	file.close() #Fermeture de l'instance de fichier
	return file.name #On retourne le chemin du fichier.

def getCycleFile(path="."):
	response=requests.get("https://montpellier-fr-smoove.klervi.net/gbfs/en/station_status.json") #Acquisition du fichier json représentant l'état de toutes les stations velaMag
	file=open(f"{path}/veloMag_{int(time.time())}.json","w+", encoding="UTF-8")#Création d'un fichier pour stocker le contenu du fichier .json téléchargé, si l'utilisateur veut enregistrer le fichier dans un répertoire particulier, il peut renseigner la variable ``path`` par défaut, la fonction sauvergarde le fichier dans le même répertoire que le programme
	file.write(response.text) #Ecriture du fichier
	file.close() #Fermeture de l'instance du fichier
	return file.name #On retourne le chemin du ficher

getCycleFile()

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
		self._time=int(time.time())
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
	

class velo:
	def __init__(self,statID,bikes,dis,free):
		self._time=int(time.time())
		self._statID=statID
		self._bikes=bikes
		self._dis=dis
		self._free=free

	#défintion des getter et setters des attributs
	@property
	def time(self):
		return self._time
	@time.setter
	def time(self,time):
		#check si time est bien un entier
		if type(time) == int:
			self._time == time
		else:
			raise TypeError("time type must be an int !")

	@property
	def statID(self):
		return self._parkID
	@statID.setter
	def statID(self,statID):
		#check si statID est bien un entier
		if type(statID) == int:
			self._statID=statID
		else:
			raise TypeError("statID must be an int !")

	@property
	def bikes(self):
		return self._bikes
	@bikes.setter
	def bikes(self,bikes):
		#check si dis est bien un int
		if type(bikes)==int:
			self._bikes==bikes
		else:
			raise TypeError("bikes must be an int !")

	@property
	def dis(self):
		return self._dis 
	@dis.setter
	def dis(self,dis):
		#check si dis est bien un int
		if type(dis)==int:
			self._dis==dis
		else:
			raise TypeError("dis must be an int !")

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



parking("FR_MTP_ANTI",True,400,500)
velo(1,3,0,9)


def getPark(idPark:str):
	response=requests.get(f"https://data.montpellier3m.fr/sites/default/files/ressources/{idPark}.xml") #Acquision du fichier xml du parking grâce à la variable idPark qui renseigne l'identifiant du parking
	if not "Page non trouvée" in response.text: #On vérifie que le fichier récupéré est bien un fichier valide et non une erreur 404
		tree = etree.fromstring(str(response.text).encode()) #Le contenu du fichier récupéré est ensuite encodé en UTF-8 pour qu'il soit compris par la libraire lxml puis mis sous forme d'élément Etree
		return parking(idPark,tree.xpath("Status")[0].text=="Open",int(tree.xpath("Free")[0].text),int(tree.xpath("Total")[0].text)) #On crée et renvoie l'objet parking

def getCycle():
	result=[] #Intialisation de la liste qui va contenir les objets velo, un objet par station
	response=requests.get("https://montpellier-fr-smoove.klervi.net/gbfs/en/station_status.json") #Acquisition du fichier json représentant l'état de toutes les stations velaMag
	content=StringIO(response.text) #On convertit la chaine de caratéres du contenu du fichier en chaine considérable comme un fichier pour l'utiliser avec la libraire json
	content=json.load(content) #On load le fichier, il sera alors convertit en objets itérables et donc utilisables
	for station in content["data"]["stations"]: #le dictionnaire data contient la liste stations qui elle même contient les dictionnaires représentant chaque stations
		#On crée et ajoute l'objet vélo à la liste qui sera retournée en fin de fonction
		result.append(velo(int(station["station_id"]),int(station["num_bikes_available"]),int(station["num_bikes_disabled"]),int(station["num_docks_available"])))
	return result #On renvoie la liste contenant l'état de chaque station.
