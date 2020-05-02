from django import forms
from .models import Code,Search_page_input,resultForm


class UploadFileForm(forms.ModelForm):
	class Meta:
		model = Code
		fields = [
		'Title_of_the_Code',
		'Description_of_the_code',
		'Code',
		'Upload_Code_file',
		'author',
		'language',
		'vote',
		'score',
		'visits',
		]


class SearchForm(forms.ModelForm):
	class Meta:
		model = Search_page_input
		fields = [
			'searchInput'
		]

		
class resultForm(forms.ModelForm):
	class Meta:
		model = resultForm
		fields = [
			'Functionality_Name',
			'Accuracy'
		]
