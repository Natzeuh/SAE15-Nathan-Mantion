import matplotlib.pyplot as plt
import sqlite3 as sq
from datetime import datetime

parkings =['FR_MTP_ANTI','FR_MTP_COME','FR_MTP_CORU','FR_MTP_EURO','FR_MTP_FOCH','FR_MTP_GAMB','FR_MTP_GARE','FR_MTP_TRIA','FR_MTP_ARCT','FR_MTP_PITO','FR_MTP_CIRC','FR_MTP_SABI','FR_MTP_GARC','FR_CAS_SABL','FR_MTP_MOSS','FR_STJ_SJLC','FR_MTP_MEDC','FR_MTP_OCCI','FR_CAS_VICA','FR_MTP_GA109','FR_MTP_GA250','FR_CAS_CDGA','FR_MTP_ARCE','FR_MTP_POLY']
linestyles = ["solid","dotted","dashed","dashdot"]
colors = ["#D18970","#33D837","#DC8AAF","#7AD4E7","#B1D42B","#ABCEC0","#5D1889","#EF0ABB","#7B561C","#1564CF","#F12138","#D4455A","#D24C21","#1C5C18","#879D09","#5176DC"]


def parkShowAll(debut,fin):
	count=0
	debut=datetime.timestamp(debut)
	fin=datetime.timestamp(fin)
	#création des listes de data
	for park in parkings:
		time=[]
		occup=[]
		
		connection = sq.connect("db.db")
		cursor = connection.cursor()
		query=f"""SELECT time,occup FROM acquisPark WHERE idPark='{park}' AND time<{fin} AND time>{debut}"""
		cursor.execute(query)
		result = cursor.fetchall()
		for record in result:
			time.append(datetime.fromtimestamp(int(record[0]),datetime.now().tzname()))
			occup.append(int(record[1]))
		plt.plot(time,occup,label=park,linestyle=linestyles[count//14],color=colors[count%14])
		count+=1
		

	plt.ylabel("Taux d'occupation (en %)")
	plt.xlabel("Temps")
	plt.legend(bbox_to_anchor=(1.04, 0), loc="lower left", borderaxespad=0)
	plt.show()


def parkShowMoy(debut,fin):
	debut=int(datetime.timestamp(debut))
	fin=int(datetime.timestamp(fin))
	times=[]
	moyennes=[]
	for time in range(debut,fin,300):
		somme=0
		entries=0
		connection = sq.connect("db.db")
		cursor = connection.cursor()
		query=f"""SELECT occup FROM acquisPark WHERE time<{time+300} AND time>{time}"""
		cursor.execute(query)
		result = cursor.fetchall()
		for record in result:
			somme+=record[0]
			entries+=1
		if entries!=0:
			moyenne=round(somme/entries,2)
			times.append(datetime.fromtimestamp(time,datetime.now().tzname()))
			moyennes.append(moyenne)
	plt.plot(times,moyennes)
	plt.ylabel("Moyenne du taux d'occupation (en %)")
	plt.xlabel("Temps")
	plt.show()


def veloShowAll(debut,fin):
	count=0
	debut=datetime.timestamp(debut)
	fin=datetime.timestamp(fin)
	#création des listes de data
	for i in range(1,59):
		time=[]
		occup=[]
		
		connection = sq.connect("db.db")
		cursor = connection.cursor()
		query=f"""SELECT time,occup FROM acquisVelo WHERE idStat={i} AND time<{fin} AND time>{debut}"""
		cursor.execute(query)
		result = cursor.fetchall()
		for record in result:
			time.append(datetime.fromtimestamp(int(record[0]),datetime.now().tzname()))
			occup.append(int(record[1]))
		print(count//15,i)
		plt.plot(time,occup,label=i,linestyle=linestyles[count//15],color=colors[count%15])
		count+=1
		

	plt.ylabel("Taux d'occupation (en %)")
	plt.xlabel("Temps")
	plt.legend(bbox_to_anchor=(1.04, 0), loc="center left", borderaxespad=0)
	plt.show()

def veloShowMoy(debut,fin):
	debut=int(datetime.timestamp(debut))
	fin=int(datetime.timestamp(fin))
	times=[]
	moyennes=[]
	for time in range(debut,fin,300):
		somme=0
		entries=0
		connection = sq.connect("db.db")
		cursor = connection.cursor()
		query=f"""SELECT occup FROM acquisVelo WHERE time<{time+300} AND time>{time}"""
		cursor.execute(query)
		result = cursor.fetchall()
		for record in result:
			somme+=record[0]
			entries+=1
		if entries!=0:
			moyenne=round(somme/entries,2)
			times.append(datetime.fromtimestamp(time,datetime.now().tzname()))
			moyennes.append(moyenne)
	plt.plot(times,moyennes)
	plt.ylabel("Moyenne du taux d'occupation (en %)")
	plt.xlabel("Temps")
	plt.show()