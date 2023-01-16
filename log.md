# Journal de bord SAE 15

Dans le cadre de la SAE 1.5 - Traiter des donnés, j'ai été amené à mener un projet de collecte, stockage et traitement de données. 

16/01/2023 - Lecture du sujet

A la lecture du sujet, on remarque qu'il faudra produire un outil qui permettra les choses suivantes
* Collecte des données
    * Données des parkings
	* Données des vélos
	* Données du tramway
* Stockage des données 
    * Traduire les fichier xml des parkings en donnés stockables et réutilisables
	* De même pour les fichiers Json des vélos
	* De même pour le tramway

* Mise en forme des données

* Traitement des données
    * Permettre un affichage des données en fonction de plusieurs paramètres temporels
	    * date de début
		* date de fin
		* laps de temps
	* Permettre un affichage sur un plan géographique de la ville (à faire si le temps le permets)

Pour l'instant, nous garderons l'interprétation des données pour l'humain, il n'est pas exclu qu'un programme pouvant interpréter les données soit codé


## Acquisition des données

En regardant les données disponibles sur le site Open Data Montpellier, on voit que les données en rapport avec le tramway ne peuvent pas nous donner d'informations sur leur utilisation, nous ne pouvons avoir que des informations géographiques qui nous serviront pour le traitement et l'interpretation. Pour rendre mon code utilisable uniquement avec les programmes, je chosis tout de même d'ajouter une fonction pour récupérer le fichier contenant les informations sur les stations de tramway de la ville. Je profite de cette fonction pour prendre les mêmes informations sur les station veloMag. Pour les parkings automobiles, les informations n'existent pas sur le site de l'agglomération, je vais alors créer un fichier .csv manuellement.

#### Parkings automobiles
```python
def getPark(idPark:str,path="."):
	response=requests.get(f"https://data.montpellier3m.fr/sites/default/files/ressources/{idPark}.xml") #Acquision du fichier xml du parking grâce à la variable idPark qui renseigne l'identifiant du parking
	file=open(f"{path}/{idPark}_{int(time.time())}.xml","w+", encoding="UTF-8") #Création d'un fichier pour stocker le contenu du fichier .xml téléchargé, si l'utilisateur veut enregistrer le fichier dans un répertoire particulier, il peut renseigner la variable ``path`` par défaut, la fonction sauvergarde le fichier dans le même répertoire que le programme
	file.write(response.text) #Ecriture du ficher
	file.close() #Fermeture de l'instance de fichier
	return file.name #On retourne le chemin du fichier.
```

#### Parkings veloMag
```python
def getCycle(path="."):
	response=requests.get("https://montpellier-fr-smoove.klervi.net/gbfs/en/station_status.json") #Acquisition du fichier json représentant l'état de toutes les stations velaMag
	file=open(f"{path}/veloMag_{int(time.time())}.json","w+", encoding="UTF-8")#Création d'un fichier pour stocker le contenu du fichier .json téléchargé, si l'utilisateur veut enregistrer le fichier dans un répertoire particulier, il peut renseigner la variable ``path`` par défaut, la fonction sauvergarde le fichier dans le même répertoire que le programme
	file.write(response.text) #Ecriture du fichier
	file.close() #Fermeture de l'instance du fichier
	return file.name #On retourne le chemin du ficher
```

#### Emplacement des parkings veloMag et des stations de Tramway

## Mise en forme des données

Pour faciliter les passages entre fichiers, base de données et programmes de traitement des données, j'ai choisi de créer de nouvelles classes, une par type de station
* Une classe parking contenant
* Une classe velo contenant

Elles sont définies avec les codes suivants
#### Classe ``parking``

#### Classe ``velo``

#### Classe ``tram``

## Stockage des données

Pour stocker les données, je me suis orienté vers une base SQLite, facile d'utilisation avec python et un type de base avec laquelle j'ai déjà travaillé par le passé.

Il me faudra donc 3 tables 
* Table de parkings
* Table de vélo
* Table de tram

[Conception de la table]

Il me faut alors des fonctions pour enregistrer mes données dans ma base

#### Enregistrement d'un objet de classe ``parking``


#### Enregistrement d'un objet de classe ``velo``

#### Enregistrement d'un objet de classe ``tram``

## Traitement des données
Le traitement des données se fera via python et GNUplot. Dans un premier temps, nous ferons des graphiques qui ne seront que sauvegardés en fichiers images. A terme, si le temps le permet, il sera possible d'ajouter une interface graphique à notre programme