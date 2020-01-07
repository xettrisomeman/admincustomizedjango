
from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('', admin.site.urls),
    path('footballs/', include('football.urls' , namespace='football')),
    path('crickets/' , include('cricket.urls' , namespace='cricket')),

]


