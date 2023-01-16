import requests
import time

def getPark(idPark:str,path="."):
	response=requests.get(f"https://data.montpellier3m.fr/sites/default/files/ressources/{idPark}.xml")
	file=open(f"{path}/{idPark}_{int(time.time())}.xml","w+", encoding="UTF-8")
	file.write(response.text)
	file.close()


