from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout

# Create your views here.

from .models import Car,Listing2,Company, Query2
from .forms import ListCarForm,QueryListCarForm, UserForm, UserRegistrationForm
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
    
    return render(request, 'cars/thanks_list_form.html')

def Homepage(request):

    if request.user.is_authenticated:

        list_of_make = Company.objects.all()
        list_of_cars = Listing2.objects.all()
        list_of_query = Query2.objects.all()

        

        p = Paginator(list_of_cars,10)
        page_number = request.GET.get('page')
        page_obj = p.get_page(page_number)

        return render(request, 'cars/homepage.html',{'make':list_of_make,
                    'cars':list_of_cars,'page_obj':page_obj,'query_obj':list_of_query,'login':True})

    else:
        return render(request,'cars/homepage.html',{'login':False})

def Admin(request):
    pass

def Listing_buy_query(request,id):

    if request.method == 'POST':
            # create a form instance and populate it with data from the request:
            form = QueryListCarForm(request.POST)
            # check whether it's valid:

            if form.is_valid():
                query_form = form.save()
                query_form
                car = Listing2.objects.get(id=id)
                query_details = Query2.objects.order_by('id')
                query_details = query_details[len(query_details)-1]

                # Send email to iron mike regarding query details and commission
                # sendMailToCustomer(car,query_details)
                
                return render(request,'cars/thanks_list_query.html',{'car':car,'query_details':query_details})


        
    form = QueryListCarForm()

    return render(request,'cars/listing_buy_query.html',{'id':id,'form':form})

def sendMailToCustomer(car,query_details):
    import smtplib
              

    smtp_obj = smtplib.SMTP("smtp.gmail.com",587)
    smtp_obj.starttls()

    email = "email here"
    pwd = "password here"
    smtp_obj.login(email,pwd)


    from_add = email
    to_add = email
    subject = "Listed Car Query and commission details "
    message = "Details of car:"+str(car)+"\nDetails of Query:"+str(query_details)+"\nCommission:"+str(0.05*car.asking_price)+"\nNet Amount:"+str(1.05*car.asking_price)

    # msg = "Subject:"+subject+"\n"+message

    smtp_obj.sendmail(from_add,to_add,(str(0.05*car.asking_price)+str(1.05*car.asking_price)))




def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password =  request.POST['password']
        user = authenticate(
        request, 
        username=username, 
        password=password
        )
        if user is None:
            return HttpResponse("Invalid credentials.")
        else:
            login(request, user)
            return render(request,'cars/homepage.html',{'login':True})
    else:
        form = UserForm()
        return render(request, 'cars/login_form.html', {'form':form})


def signout(request):
    logout(request)
    return render(request,'cars/homepage.html')

def signup(request):
    if request.method=="POST":
        # first_name = request.POST['first_name']
        # last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        newuser = User.objects.create_user(
        # first_name=first_name, 
        # last_name=last_name,
        username=username,
        password=password,
        email=email
        )
        try:
            newuser.save()
        except:
            return HttpResponse("Something went wrong.")
        else:
            return render(request,'cars/login_form.html')
    else:
        form = UserRegistrationForm()
        return render(request, 'cars/register_form.html', {'form':form})  