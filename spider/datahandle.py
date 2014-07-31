import json
def AirportData():
	file=open("item.json")
	# datas=json.loads(file)
	datas=[]
	for line in file:
		# print line
		# print type(line)
		data=json.loads(line[:-2])
		if (data['name']!=[]):
			datas.append(data)
	print len(datas)
	return datas