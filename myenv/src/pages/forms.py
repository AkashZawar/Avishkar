from django import forms
from .models import Code, Search_page_input, CodeInput, XLUploadModel


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
        ]


class SearchForm(forms.ModelForm):
    class Meta:
        model = Search_page_input
        fields = [
            'searchInput'
        ]


class resultForm(forms.ModelForm):
    class Meta:
        model = Code
        fields = [
            'Title_of_the_Code',
            'accuracy',
        ]


class StepInput(forms.ModelForm):
    class Meta:
        model = CodeInput
        fields = [
            'Test_Action',
            'locator_type',
            'Test_input_value',
        ]


class XLUpload(forms.ModelForm):
    class Meta:
        model = XLUploadModel
        fields = [
            'xl_file',
            'description'
        ]
