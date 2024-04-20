from django.db import models

# Create your models here.
class item(models.Model):
    iname=models.CharField(max_length=200,null=True)
class slider(models.Model):
    spic=models.ImageField(upload_to='static/sliderimg',null=True)
    sdate=models.DateField(null=True)
class itemcategory(models.Model):
    itemname=models.CharField(max_length=200,null=True)
    itempic=models.ImageField(upload_to='static/itemcategoryimg',null=True)
    itemdiscount=models.IntegerField(null=True)
