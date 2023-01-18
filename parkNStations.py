class parking:
	def __init__(self,parkID,open,free,total):
		self._time=int(time.time())
		self._parkID=parkID
		self._open=open
		self._free=free
		self._total=total
	
	#défintion des getter et setters des attributs
	@property
	def time(self):
		return self.time
	@time.setter
	def time(self,time):
		#check si time est bien un entier
		if type(time) == int:
			self._time == time
		else:
			raise TypeError("time type must be an int !")
	

	@property
	def parkID(self):
		return self._parkID
	@parkID.setter
	def parkID(self,parkID):
		#check si parkID est bien dans les id disponibles sur le site opendata
		if parkID in ['FR_MTP_ANTI','FR_MTP_COME','FR_MTP_CORU','FR_MTP_EURO','FR_MTP_FOCH','FR_MTP_GAMB','FR_MTP_GARE','FR_MTP_TRIA','FR_MTP_ARCT','FR_MTP_PITO','FR_MTP_CIRC','FR_MTP_SABI','FR_MTP_GARC','FR_CAS_SABL','FR_MTP_MOSS','FR_STJ_SJLC','FR_MTP_MEDC','FR_MTP_OCCI','FR_CAS_VICA','FR_MTP_GA109','FR_MTP_GA250','FR_CAS_CDGA','FR_MTP_ARCE','FR_MTP_POLY']:
			self._parkID=parkID
		else:
			raise ValueError("parkID is not valid !")
	
	@property
	def open(self):
		return self._open
	@open.setter
	def open(self,open):
		#check si open est bien un booléen
		if type(open)==bool:
			self._open=open
		else:
			raise TypeError("open type must be a bool !")

	@property
	def free(self):
		return self._free
	@free.setter
	def free(self,free):
		#check si free est bien un int
		if type(free) == int:
			self._free=free
		else:
			raise TypeError("free must be an int !")
	@property
	def total(self):
		return self._total 
	@total.setter
	def total(self,total):
		#check si total est bien un int
		if type(total)==int:
			self._total==total
		else:
			raise TypeError("total must be an int !")
	

class velo:
	def __init__(self,statID,bikes,dis,free):
		self._time=int(time.time())
		self._statID=statID
		self._bikes=bikes
		self._dis=dis
		self._free=free

	#défintion des getter et setters des attributs
	@property
	def time(self):
		return self._time
	@time.setter
	def time(self,time):
		#check si time est bien un entier
		if type(time) == int:
			self._time == time
		else:
			raise TypeError("time type must be an int !")

	@property
	def statID(self):
		return self._parkID
	@statID.setter
	def statID(self,statID):
		#check si statID est bien un entier
		if type(statID) == int:
			self._statID=statID
		else:
			raise TypeError("statID must be an int !")

	@property
	def bikes(self):
		return self._bikes
	@bikes.setter
	def bikes(self,bikes):
		#check si dis est bien un int
		if type(bikes)==int:
			self._bikes==bikes
		else:
			raise TypeError("bikes must be an int !")

	@property
	def dis(self):
		return self._dis 
	@dis.setter
	def dis(self,dis):
		#check si dis est bien un int
		if type(dis)==int:
			self._dis==dis
		else:
			raise TypeError("dis must be an int !")

	@property
	def free(self):
		return self._free
	@free.setter
	def free(self,free):
		#check si free est bien un int
		if type(free) == int:
			self._free=free
		else:
			raise TypeError("free must be an int !")