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


lookingfor_choices = (
    ('AP', 'Apartment (2/3 BHK)'),
    ('Villa', 'Villa / Independent house'),
    ('Re', 'Residental Plot'),
    ('Ag', 'Agriculture Plot'),

)


class About(models.Model):
     First_name = models.CharField(max_length=100)
     Last_name = models.CharField(max_length=100)
     Phone_number = models.CharField(max_length=100)
     Looking_for = models.CharField(choices=lookingfor_choices, default='Apartment (2/3 BHK)', max_length=100)
     AreaPreferred = models.CharField(max_length=100)
     Budget = models.CharField(max_length=100)


def __str__(self):
     return self.Firstname
