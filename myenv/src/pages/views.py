from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import UploadFileForm,SearchForm


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
	# if request.method == 'POST':
	# search_input_forms = SearchForm()
	# print(request.GET)
	# context = {'search_input_forms': form }
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


# Below code for file upload handling 
def model_form_upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/upload')
    else:
        form = UploadFileForm()
    return render(request, 'page/model_form_upload.html', {
        'form': form
    })

# file Upload handling Ends 