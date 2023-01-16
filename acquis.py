import requests
import time

def getPark(idPark:str):
	response=requests.get(f"https://data.montpellier3m.fr/sites/default/files/ressources/{idPark}.xml")
	file=open(f"{idPark}_{int(time.time())}.xml","w+")
	file.write(response.text)
	file.close


getPark("Bouchard")