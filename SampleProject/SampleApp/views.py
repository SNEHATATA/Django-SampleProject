from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
def hello(request):
	return HttpResponse("<h1>Hello World!!!</h1>")

def sam(request):
	return HttpResponse("<h1>welcome to django learning</h1>")

def dyn(request,a):
	return HttpResponse("<h1 style=color:cyan;text-align:center;background-color:yellow>lucky numer is :{}</h1>".format(a))

def data(request,b):
	return HttpResponse("<h2 style=text-align:center>my name is:{}</h2>".format(b))

def temp(request):
	return render(request,'temp.html',{})

def table(request):
	return render(request,'table.html',{})

def internal(request):
	return render(request,'internal.html')
def external(request):
	return render(request,'external.html')

def boot(request):
	return render(request,'boot.html')

def offline(request):
	return render(request,'offline.html')