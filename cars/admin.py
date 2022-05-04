from django.contrib import admin
from .models import Company, Car , Listing2, Query2

# Register your models here.
admin.site.register(Car)
admin.site.register(Company)
admin.site.register(Listing2)
admin.site.register(Query2)