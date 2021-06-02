from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class author(models.Model):
    auth = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.full_name

class publisher(models.Model):
    auth = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.full_name

class book(models.Model):
    writer = models.ForeignKey(author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(publisher, on_delete=models.CASCADE)
    bookname = models.CharField(max_length=50)
    qty = models.IntegerField()

    def __str__(self):
        return self.bookname
    