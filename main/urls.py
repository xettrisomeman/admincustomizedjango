
from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('', admin.site.urls),
    path('football/', include('football.urls' , namespace='football')),
    path('cricket/' , include('cricket.urls' , namespace='cricket')),

]


