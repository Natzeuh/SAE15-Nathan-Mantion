import matplotlib.pyplot as plt
import sqlite3 as sq

parkings =['FR_MTP_ANTI','FR_MTP_COME','FR_MTP_CORU','FR_MTP_EURO','FR_MTP_FOCH','FR_MTP_GAMB','FR_MTP_GARE','FR_MTP_TRIA','FR_MTP_ARCT','FR_MTP_PITO','FR_MTP_CIRC','FR_MTP_SABI','FR_MTP_GARC','FR_CAS_SABL','FR_MTP_MOSS','FR_STJ_SJLC','FR_MTP_MEDC','FR_MTP_OCCI','FR_CAS_VICA','FR_MTP_GA109','FR_MTP_GA250','FR_CAS_CDGA','FR_MTP_ARCE','FR_MTP_POLY']

def parkShow():
	#création des listes de data
	for park in parkings:
		time=[]
		occup=[]
		connection = sq.connect("db.db")
		cursor = connection.cursor()
		query=f"""SELECT time,occup FROM acquisPark WHERE idPark='{park}'"""
		cursor.execute(query)
		result = cursor.fetchall()
		for record in result:
			time.append(int(record[0]))
			occup.append(int(record[1]))
		plt.plot(time,occup,label=park)
		

	plt.axis([1674208601,1674381118,0,100])
	plt.ylabel("Taux d'occupation (en %)")
	plt.xlabel("Temps (en secondes depuis epoch)")
	plt.legend()
	plt.show()
