from django import forms

from .models import Product


# class ProductForm(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = [
#             'First_Name',
#             'Last_Name',
#             'Email_Address',
#             'Gender_Male',
#             'Gender_Female',
#             'City',
#             'Country'

#         ]

class ProductForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = [
		'title',
		'description',
		'First_Name',
        'Last_Name',
        'Email_Address',
        'Gender_Male',
        'Gender_Female',
        'City',
        'Country'

		]
