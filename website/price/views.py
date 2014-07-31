from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
def index(req):
	t = loader.get_template('price/mainpage.html')
	c = Context({
        })
	return HttpResponse(t.render(c))
    
	# return HttpResponse("<h1>welcome!!!it workds!</h1>")
# Create your views here.
