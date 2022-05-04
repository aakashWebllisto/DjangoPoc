
# Create your models here.
from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Company(models.Model):
    make = models.CharField(max_length=100)

    def __str__(self):
        return self.make

class Car(models.Model):
    # make = models.CharField(max_length=200,)
    model_name = models.CharField(max_length=200,blank=False,null=False)
    condition = models.CharField(max_length=200,blank=True,null=False)
    year = models.PositiveIntegerField(blank=False, null=False)
    asking_price = models.FloatField(blank=False, null=False, validators=[MinValueValidator(0), MaxValueValidator(10)])
    make = models.ForeignKey(Company, blank=False, null=False, on_delete=models.CASCADE)
    # Remove null and blank true

    def __str__(self):
        if self.year:
            return f"{self.make} ({self.model_name})"
        return self.make


class Listing(models.Model):
    # make = models.CharField(max_length=200,)
    model_name = models.CharField(max_length=200,blank=False,null=False)
    condition = models.CharField(max_length=200,blank=True,null=False)
    year = models.PositiveIntegerField(blank=False, null=False)
    asking_price = models.FloatField(blank=False, null=False, validators=[MinValueValidator(0), MaxValueValidator(10)])
    make = models.ForeignKey(Company, blank=False, null=False, on_delete=models.CASCADE)
    seller_name = models.CharField(max_length=200,blank=False,null=False)
    seller_mobile = models.IntegerField(blank=False, null=False)

    def __str__(self):
        if self.year:
            return f"{self.make} ({self.model_name}) {self.seller_name}"
        return self.make



class Listing2(models.Model):
    # make = models.CharField(max_length=200,)
    model_name = models.CharField(max_length=100,blank=False,null=False)
    condition = models.CharField(max_length=100,blank=True,null=False)
    year = models.PositiveIntegerField(blank=False, null=False)
    asking_price = models.FloatField(blank=False, null=False, validators=[MinValueValidator(0), MaxValueValidator(10)])
    make = models.ForeignKey(Company, blank=False, null=False, on_delete=models.CASCADE)
    seller_name = models.CharField(max_length=100,blank=False,null=False)
    seller_mobile = models.IntegerField(blank=False, null=False)
    
    status = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        if self.year:
            return f"{self.id}:{self.make} ({self.model_name}-{self.year}) {self.seller_name}"
        return self.make


class Query2(models.Model):
    name = models.CharField(max_length=100,blank=False,null=False)
    mobile = models.CharField(max_length=100,blank=False,null=False)
    query_id = models.ForeignKey(Listing2, blank=False, null=False, on_delete=models.CASCADE)

    def __str__(self):
        if self.query_id:
            return f"{self.name} : {self.mobile} :{self.query_id}"
        return self.name
