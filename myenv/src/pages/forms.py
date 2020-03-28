from django import forms

from .models import Code


class UploadFileForm(forms.ModelForm):
	class Meta:
		model = Code
		fields = [
		'Title_of_the_Code',
		'Description_of_the_code',
		'Code',
		'Upload_Code_file',
		]
