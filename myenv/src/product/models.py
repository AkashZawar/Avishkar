from django.db import models


#Create your models here.
class Product(models.Model):
	title = models.CharField(max_length=120, default='defaultTitle')
	description = models.TextField(blank=True, null=True)
	# price		=models.DecimalField(decimal_places=2,max_digits=10000)
	summery = models.TextField(blank=True, null=True)
	feature = models.BooleanField(default=False)
	First_Name = models.CharField(max_length=120, default='default')
	Last_Name = models.CharField(max_length=120, default='default')
	Email_Address = models.CharField(max_length=120, default='default')
	Gender_Male = models.BooleanField(default=False)
	Gender_Female = models.BooleanField(default=False)
	City = models.CharField(max_length=120, default='default')
	Country = models.CharField(max_length=120, default='india')


# class Product(models.Model):
# 	First_Name = models.CharField(max_length=120, default='default')
# 	Last_Name = models.CharField(max_length=120, default='default')
# 	Email_Address = models.CharField(max_length=120, default='default')
# 	Gender_Male = models.BooleanField(default=False)
# 	Gender_Female = models.BooleanField(default=False)
# 	City = models.CharField(max_length=120, default='default')
# 	Country = models.CharField(max_length=120, default='india')
# 	