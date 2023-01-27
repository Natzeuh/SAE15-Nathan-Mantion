from courbes import *
from datetime import datetime

debut = datetime.strptime("24/01/23 06:00:00","%d/%m/%y %H:%M:%S")
fin = datetime.strptime("26/01/23 22:30:00","%d/%m/%y %H:%M:%S")


parkShowMoy(debut,fin)