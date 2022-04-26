# from django.template import loader
# from django import template
# from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from .models import Car,Listing2,Company
from .forms import ListCarForm,QueryListCarForm
from django.core.paginator import Paginator


def List_car_form(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ListCarForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            
            # redirect to a new URL:
            form.save()
            
            
            return render(request,'cars/thanks_list_form.html')
            
            # return HttpResponseRedirect('/thanks/')


    # if a GET (or any other method) we'll create a blank form
    else:
        form = ListCarForm()

    return render(request, 'cars/car_list_view.html', {'form': form})


def Thanks_list_form(request):
    id = {
        'listingId': "Hello",
    }
    return render(request, 'cars/thanks_list_form.html')

def Homepage(request):

    list_of_make = Company.objects.all()
    list_of_cars = Listing2.objects.all()
    p = Paginator(list_of_cars,10)
    page_number = request.GET.get('page')
    page_obj = p.get_page(page_number)
    return render(request, 'cars/homepage.html',{'make':list_of_make,'cars':list_of_cars,'page_obj':page_obj})

def Listing_buy_query(request,id):

    if request.method == 'POST':
            # create a form instance and populate it with data from the request:
            form = QueryListCarForm(request.POST)
            # check whether it's valid:
            if form.is_valid():
                form.save()
                
                car = Listing2.objects.get(id=id)

                return render(request,'cars/thanks_list_query.html',{'car':car,'form':form})
        
    form = QueryListCarForm()

    return render(request,'cars/listing_buy_query.html',{'id':id,'form':form})

