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
	* Permettre un affichage sur un plan géographique de la ville

Pour l'instant, nous garderons l'interprétation des données pour l'humain, il n'est pas exclu qu'un programme pouvant interpréter les données soit codé

La collecte des données étant primordiale pour le reste des tâches, ce sera la première chose à laquelle je vais m'atteller. Il est urgent de faire ces programmes afin de lancer au plus vite la capture de données.

## Acquisition des données

## Mise en forme des données

Pour faciliter les passages entre fichiers, base de données et programmes de traitement des données, j'ai choisi de créer de nouvelles classes, une par type de station
* Une classe parking contenant
* Une classe velo contenant
* Une classe tram contenant

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