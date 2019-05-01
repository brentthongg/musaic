import random
import Platform

class Level(object):

	@staticmethod
	def init():
		Platform.Plat.init()
		pass

	def __init__(self, numPlats):
		self.rows = 10
		self.cols = 64
		self.numPlats = numPlats
		self.Plats = []
		#self.map = createMap(self)
		self.numPlats = 3
		self.Plats = []
		self.createPlatforms()
		#Level.createPlatforms(self)

	def createMap(self):
		tempMap = [[0] * self.cols for i in range(self.rows)]
		return tempMap

	#def fillMap(self):
		#for i in range(self.numPlats):
			#randRow = 
			#tempMap[]


	def createPlatforms(self):
		for i in range(self.numPlats):
			new = Platform.Plat()
			self.Plats.append(new)