from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import UploadFileForm,SearchForm,resultForm
from .models import Search_page_input,Code

def about_view(request,*args,**kwargs):
	my_context = {
	"pagetitle" : "NightWatch Automation : About",
	"key1" : "value1",
	"key2" : "value2",
	"key3" : "value3",
	}
	#return HttpResponse("<h1>About world</h1>")
	return render(request,"about.html",my_context)


def search_view(request, *args, **kwargs):
	rows = Search_page_input.objects.raw("select id,Title_of_the_Code,Description_of_the_code,vote from pages_code order by vote DESC LIMIT 3")
	return render(request, "page/search.html",{'rows': rows})


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
	form = UploadFileForm(request.POST, request.FILES)
	if form.is_valid():
		form.save()
		return redirect('/upload/')
	else:
		form = UploadFileForm()
		return render(request, 'page/model_form_upload.html', {
		'form': form
		})

	return render(request,"page/model_form_upload.html",my_context)
# file Upload handling Ends 

# Below code for result display 
def display_result(request):
	if request.method == 'POST':
		searchInput = request.POST.get('searchInput')
		SQL = "select id,Title_of_the_Code,author,language,Code,Upload_Code_file from pages_code where Title_of_the_Code COLLATE UTF8_GENERAL_CI like '%" +searchInput +"%' limit 3"
		rows = Code.objects.raw(SQL)
		return render(request, "result.html",{'rows': rows})
	else:
		return render(request, "result.html",{})

def result_form_submit(request):
	rows="resultSave"
	print(rows)
	form = UploadFileForm(request.GET)
	if form.is_valid():
		form.save()
		return render(request, "/resultSave/",{'rows': rows})
	else:
		return render(request, "result.html",{'rows': rows})