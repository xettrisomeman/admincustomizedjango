from django.urls import path


from . import views

app_name='cricket'

urlpatterns = [
    path('cricket/' ,views.HomePageView.as_view() , name='homepage')
]
