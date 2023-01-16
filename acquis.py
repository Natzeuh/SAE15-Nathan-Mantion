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