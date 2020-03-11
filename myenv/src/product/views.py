from django.shortcuts import render
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

    # context = {
    #     'First_Name': 'sergre',
    #     'Last_Name': 'grgdr',
    #     'Email_Address': 'grggrg',
    #     'Gender_Male': True,
    #     'Gender_Female': False,
    #     'City': 'fgdgd',
    #     'Country': 'dggrgdgr'
    # }

    return render(request, "products/products_detail.html", context)

# def excel_view(request):
# 	return render(request,"products/MainFile.htm",{})
