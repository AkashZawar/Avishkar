from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .forms import ProductForm

from .models import Product
# Create your views here.
def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {'form': form}
    return render(request, "products/products_create.html", context)


def product_detail_view(request):
    obj = Product.objects.get(id=1)
    print('THIS IS TEST')
    context = {
    	'title' : obj.title ,
    	'description' : obj.description,
    }
    context={"object" : obj}
    return render(request, "products/products_detail.html", context)

# def excel_view(request):
# 	return render(request,"products/MainFile.htm",{})
