import json
class AirData:
	def GetCode(name):
		for m in datas:
			if (m==datas['name']):
				return 
	def AirportData(self):
		file=open("item.json")
		# datas=json.loads(file)
		self.datas=[]
		for line in file:
			# print line
			# print type(line)
			data=json.loads(line[:-2])
			if (data['name']!=[]):
				self.datas.append(data)
		print (len(self.datas))
		return self.datas
	def UsaData(self):
		file=open("airchina")
		self.datas=[]
		for line in file:
			# print line
			# print (line)
			# print type(line)
			data=json.loads(line)
			self.datas.append(data)
		return self.datas
