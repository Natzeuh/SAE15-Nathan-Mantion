import sqlite3 as sq
from acquis import *
from parkNStations import *

def savePark(park:parking):
	#connection base
	connection = sq.connect("db.db")
	#Création curseur pour l'excécution de la requête
	cursor = connection.cursor()
	#Création de la requête sql
	query = f"""INSERT INTO acquisPark
	(time, idPark, free, total, occup)
	VALUES
	({park.time},'{park.parkID}',{park.free},{park.total},{100-(round(park.free/park.total,2))*100})
	"""
	#Exécution de la requête
	cursor.execute(query)
	#Sauvegarde de la base avec modification
	connection.commit()
	#Fermeture des instances
	cursor.close()
	connection.close()


def saveVelo(stat:velo):
	a=1


	