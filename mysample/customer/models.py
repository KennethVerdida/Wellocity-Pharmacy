from django.db import models
from django.utils import timezone

# Create your models here.

class Person(models.Model):
    firstName = models.CharField(max_length = 100)
    middleName  = models.CharField(max_length = 100)
    lastName   = models.CharField(max_length = 100)
    street   = models.CharField(max_length = 50)
    barangay   = models.CharField(max_length = 50)
    city   = models.CharField(max_length = 50)
    Zip   = models.IntegerField()
    province   = models.CharField(max_length = 50)
    country   = models.CharField(max_length = 50)
    birthdate = models.DateField(default =  timezone.now)
    height   = models.IntegerField()
    weight   = models.IntegerField()
    religion   = models.CharField(max_length = 50)
    gender   = models.CharField(max_length = 50)
    status   = models.CharField(max_length = 50)
    spouseName   = models.CharField(max_length = 50)
    spouseOccupation   = models.CharField(max_length = 50)
    noChildren   = models.IntegerField()
    motherName   = models.CharField(max_length = 50)
    motherOccupation   = models.CharField(max_length = 50)
    fatherName   = models.CharField(max_length = 50)
    fatherOccupation   = models.CharField(max_length = 50)
    email = models.CharField(max_length = 50,  null=True)
    password = models.CharField(max_length = 50, null=True)
    
    class Meta:
      db_table = "Person"

class Medicine(models.Model):
    dateRegistered_Medicine = models.DateField(default = timezone.now)
    sku = models.CharField(max_length = 100)
    category = models.CharField(max_length = 100)
    genericName = models.CharField(max_length = 100)
    commonBrand = models.CharField(max_length = 100)
    manufacturedDate = models.DateField(default = timezone.now)
    expiryDate = models.DateField(default = timezone.now)
    size = models.FloatField()
    order = models.IntegerField()
    total = models.FloatField()
    howTo_Use = models.CharField(max_length = 100)
    sideEffects = models.CharField(max_length = 100)
    price = models.FloatField()
    noItems = models.IntegerField()
    img1 = models.ImageField(upload_to='images/', null=True, blank=True)
    img2 = models.ImageField(upload_to='images/', null=True, blank=True)
    img3 = models.ImageField(upload_to='images/', null=True, blank=True)
    
    class Meta:
      db_table = "Medicine"

class Customer(Person):
    dateRegistered_Customer = models.DateField(default = timezone.now)
    profilePicture = models.FileField(default='settings.MEDIA_ROOT/default.png')
    medicines = models.ManyToManyField(Medicine)
        
    class Meta:
      db_table = "Customer"