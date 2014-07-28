from django.shortcuts import render
from django.http import HttpResponse
def index(req):
	return HttpResponse("<h1>welcome!!!it workds!</h1>")
# Create your views here.
