import requests
import time

def getPark(idPark:str,path="."):
	response=requests.get(f"https://data.montpellier3m.fr/sites/default/files/ressources/{idPark}.xml")
	file=open(f"{path}/{idPark}_{int(time.time())}.xml","w+", encoding="UTF-8")
	file.write(response.text)
	file.close()
	return file.name

def getCycle(path="."):
	response=requests.get("https://montpellier-fr-smoove.klervi.net/gbfs/en/station_status.json")
	file=open(f"{path}/veloMag_{int(time.time())}.json","w+", encoding="UTF-8")
	file.write(response.text)
	file.close()
	return file.name

getCycle()