
from django.urls import path
from .import views
app_name='ecommersapp'


urlpatterns = [

    path('',views.allProdCat,name='allProdCat'),
    path('<slug:c_slug>/',views.allProdCat,name='Products_by_category')
]