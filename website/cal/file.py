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

def yunxing(strdep,strarr,datestr,todaystr):
	depature_str=strdep
	arrival_str=strarr
	date=datestr
	present=todaystr
	mon=8
	day=6
	factor1=0
	factor2=0
	totalinfo=0
	datas=[]
	for j in range(0,4):
		filename="result"
		filename=filename+str(mon)+str(day)+".json"
		file=open(filename)
		pricelist=[]
		for line in file:
			#print(line[:-2])
			totalinfo=totalinfo+1
			data=json.loads(line[:-2])
			datas.append(data)
		file.close()
		day=day+1
	for i in range(0,totalinfo):
		if (datas[i]['date']==date):
			#factor=factor+1
			if ((datas[i]['name'][0:3]==depature_str) and (datas[i]['name'][4:7]==arrival_str)):
				#factor2=factor2+1
				if (datas[i]['price'][4]!='<b> - </b>'):
					lin_float=float(datas[i]['price'][4][4:-4])
					pricelist.append(lin_float)
	

	mark=0
	day=len(pricelist)
	depature=int(date[8:])
	today=int(present[8:])
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
				if flucturate(pricelist[j],pricelist[day-1])!=0:
					k=1
			if k==0:
				ans="buy"
				mark=1
	if (mark==0):
		ans="wait"
	return {'ans':ans,'price':pricelist[day-1]}


#print(pricelist)

