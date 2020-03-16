from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request,*args,**kwargs):
	print(request)
	print(args,kwargs)
	print(request.user)
	#return HttpResponse(request,"<h1>Hellow world</h1>")
	my_context = {
			"pagetitle" : "NightWatch Automation : Home"
			}
	return render(request, "page/index.html", {})

def about_view(request,*args,**kwargs):
	my_context = {
			"pagetitle" : "NightWatch Automation : About",
			"key1" : "value1",
			"key2" : "value2",
			"key3" : "value3",
	}
	#return HttpResponse("<h1>About world</h1>")
	return render(request,"about.html",my_context)

def search_view(request,*args,**kwargs):
	my_context = {
			"pagetitle" : "NightWatch Automation : Search"
			}
	#return HttpResponse("<h1>Social world</h1>")
	return render(request,"page/search.html",{})

def contact_view(request,*args,**kwargs):
	my_context = {
			"pagetitle" : "NightWatch Automation : Contact"
			}
	#return HttpResponse("<h1>Contact world</h1>")
	return render(request,"contact.html",{})

def social_view(request,*args,**kwargs):
	my_context = {
			"pagetitle" : "NightWatch Automation : Contact"
			}
	#return HttpResponse("<h1>Contact world</h1>")
	return render(request,"social.html",{})