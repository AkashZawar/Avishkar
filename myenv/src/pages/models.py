from django.db import models

# Create your models here.

class Code(models.Model):
	Title_of_the_Code = models.CharField(max_length=120, default='defaultTitle')
	Description_of_the_code = models.TextField(blank=True, null=True)
	# price		=models.DecimalField(decimal_places=2,max_digits=10000)
	Code = models.TextField(blank=True, null=True)
	Upload_Code_file = models.FileField(upload_to='uploads/')
	uploaded_at = models.DateTimeField(auto_now_add=True)
	author = models.CharField(max_length=120, default='default_author')
	language = models.CharField(max_length=120, default='default_Language')
	vote = models.IntegerField(default=1)
	score = models.IntegerField(default=1)
	visits = models.IntegerField(default=1)


class Search_page_input(models.Model):
	searchInput = models.CharField(max_length=120, default='defaultTitle')