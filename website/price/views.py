from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader, RequestContext
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
import datetime
import sys
sys.path.append('cal')
from file import yunxing
import datahandle
def index(req):
	Rdata=datahandle.AirData()
	datas=Rdata.UsaData()
	print (req.method)
	print ("hahah")
	t = loader.get_template('price/mainpage.html')
	if (req.method == 'GET'):
		c = RequestContext(req,{'air':datas})
		return HttpResponse(t.render(c))
	else:
		def findair(code):
			for air in datas:
				if (code==air['code']):
					return air
		print req.POST['departure']
		today=datetime.date.today()
		today=today.strftime("%Y-%m-%d")
		print (today)
		res=yunxing(req.POST['departure'],req.POST['arrival'],req.POST['date'],today)
		c = {'dep':findair(req.POST['departure']),
			 'arr':findair(req.POST['arrival']),
			 'date':req.POST['date'],
			 'sug':res['ans'],
			 'price':res['price'],
			}
		c.update(csrf(req))
		print (c)
		return render_to_response("price/resultpage.html", c)
	
    
	# return HttpResponse("<h1>welcome!!!it workds!</h1>")
# Create your views here.
