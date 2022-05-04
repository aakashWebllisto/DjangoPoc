from django.urls import path
from . import views

app_name = 'cars'

urlpatterns = [
    # path('cars/list', views.CarListView),
    path('cars/list_car', views.List_car_form),
    path('cars/thanks', views.Thanks_list_form),
    path('cars/home', views.Homepage),
    path('cars/admin', views.Admin),
    path('cars/login', views.signin),
    path('cars/logout', views.signout),
    path('cars/register', views.signup),
    # path('cars/posted_form', views.posted_form),
    path('cars/listing_buy_query/<int:id>', views.Listing_buy_query),
    # path('cars/submit_listing_query/<int:id>', views.Submit_listing_query),

]
