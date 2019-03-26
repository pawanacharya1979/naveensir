from django.db import models

# Create your models here.


class ContactUs(models.Model):
     Name = models.CharField(max_length=100)
     Email = models.EmailField()
     phone_number = models.CharField(max_length=100)
     subject = models.CharField(max_length=100)
     Message = models.CharField(max_length=200)

     def __str__(self):
         return self.Name