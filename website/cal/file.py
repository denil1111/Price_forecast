import json

def flucturate(a,b):
	if b>a:
		c=b-a
		if c*100<a:
			return 0
	if a<b:
		c=a-b
		if c*100<b:
			return 0
	return 1

def yunxing(strdep,strarr,mon,day):
	depature_str=strdep
	arrival_str=strarr
	leavemonth=mon
	leaveday=day
	file=open("example.json")
	datas=[]
	pricelist=[]
	day=0
	totalinfo=0
	for line in file:
		#print(line[:-2])
		totalinfo=totalinfo+1
		data=json.loads(line[:-2])
		datas.append(data)
	#print(totalinfo)

	for i in range(0,totalinfo):
		if ((int(datas[i]['date'][6])==leavemonth) and (int(datas[i]['date'][8:])==leaveday)):
			if ((datas[i]['name'][0:3]==depature_str) and (datas[i]['name'][4:7]==arrival_str)):
				if (datas[i]['price'][4]!='<b> - </b>'):
					lin_float=float(datas[i]['price'][4][4:-4])
					pricelist.append(lin_float)
					day=day+1

	day=len(pricelist)
	depature=28
	today=1
	if pricelist[day-1]<pricelist[day-2]:
		ans="buy"
		mark=1
	if depature-today>20 :
		for i in range(0,3):
			if flucturate(pricelist[day-1],pricelist[day-i-1])==0:
				ans="buy"
				mark=1
	for i in range(0,day-2):
		if flucturate(pricelist[i],pricelist[i+1])!=0:
			for j in range(i,day):
				if flucturate(pricelist[j],pricelist[day])!=0:
					k=1
			if k==0:
				ans="buy"
				mark=1
	if mark==0:
		ans="wait"
	return {'ans':ans,'price':pricelist[day-1]}
#print(pricelist)


