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
	#connection base
	connection = sq.connect("db.db")
	#Création curseur pour l'excécution de la requête
	cursor = connection.cursor()
	#calcul du nombre total de places 
	total = stat.free + stat.dis + stat.bikes  
	#Création de la requête sql
	if total != 0:
		query = f"""INSERT INTO acquisVelo
		(time, idStat, bikes, dis, free, total, occup)
		VALUES
		({stat.time},'{stat.statID}',{stat.bikes},{stat.dis},{stat.free},{total},{100-(round(stat.free/total,2))*100})
		"""
	else:
		query = f"""INSERT INTO acquisVelo
		(time, idStat, bikes, dis, free, total, occup)
		VALUES
		({stat.time},'{stat.statID}',{stat.bikes},{stat.dis},{stat.free},{total},0.0)
		"""
	#Exécution de la requête
	cursor.execute(query)
	#Sauvegarde de la base avec modification
	connection.commit()
	#Fermeture des instances
	cursor.close()
	connection.close()
