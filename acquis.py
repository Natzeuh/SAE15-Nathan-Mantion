import requests
import time
from lxml import etree
from io import StringIO
import json
from parkNStations import *


def getParkFile(idPark:str,path="."):
	response=requests.get(f"https://data.montpellier3m.fr/sites/default/files/ressources/{idPark}.xml") #Acquision du fichier xml du parking grâce à la variable idPark qui renseigne l'identifiant du parking
	file=open(f"{path}/{idPark}_{int(time.time())}.xml","w+", encoding="UTF-8") #Création d'un fichier pour stocker le contenu du fichier .xml téléchargé, si l'utilisateur veut enregistrer le fichier dans un répertoire particulier, il peut renseigner la variable ``path`` par défaut, la fonction sauvergarde le fichier dans le même répertoire que le programme
	file.write(response.text) #Ecriture du ficher
	file.close() #Fermeture de l'instance de fichier
	return file.name #On retourne le chemin du fichier.

def getVeloFile(path="."):
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

def getPark(idPark:str):
	response=requests.get(f"https://data.montpellier3m.fr/sites/default/files/ressources/{idPark}.xml") #Acquision du fichier xml du parking grâce à la variable idPark qui renseigne l'identifiant du parking
	if not "Page non trouvée" in response.text: #On vérifie que le fichier récupéré est bien un fichier valide et non une erreur 404
		if not len(response.text) == 0:
			tree = etree.fromstring(str(response.text).encode()) #Le contenu du fichier récupéré est ensuite encodé en UTF-8 pour qu'il soit compris par la libraire lxml puis mis sous forme d'élément Etree
			return parking(idPark,tree.xpath("Status")[0].text=="Open",int(tree.xpath("Free")[0].text),int(tree.xpath("Total")[0].text)) #On crée et renvoie l'objet parking

def getVelo():
	result=[] #Intialisation de la liste qui va contenir les objets velo, un objet par station
	response=requests.get("https://montpellier-fr-smoove.klervi.net/gbfs/en/station_status.json") #Acquisition du fichier json représentant l'état de toutes les stations velaMag
	content=StringIO(response.text) #On convertit la chaine de caratéres du contenu du fichier en chaine considérable comme un fichier pour l'utiliser avec la libraire json
	content=json.load(content) #On load le fichier, il sera alors convertit en objets itérables et donc utilisables
	for station in content["data"]["stations"]: #le dictionnaire data contient la liste stations qui elle même contient les dictionnaires représentant chaque stations
		#On crée et ajoute l'objet vélo à la liste qui sera retournée en fin de fonction
		result.append(velo(int(station["station_id"]),int(station["num_bikes_available"]),int(station["num_bikes_disabled"]),int(station["num_docks_available"])))
	return result #On renvoie la liste contenant l'état de chaque station.
