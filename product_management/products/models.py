from django.db import models
from datetime import datetime

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    image=models.ImageField(null=False,blank=False)
    name=models.CharField(max_length=300,null=False,blank=False)
    category=models.ForeignKey(Category,on_delete=models.CASCADE ,default=True,null=False)
    price=models.FloatField()
    description=models.TextField()
    is_published=models.BooleanField(default=True)
    created_at=models.DateField(default=datetime.now)

    def __str__(self) :
        return self.name
