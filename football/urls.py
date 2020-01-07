from django.urls import path


from . import views


#specifying app name (it can be used as 'football:homepage')

app_name='football'

urlpatterns = [
    path('' , views.HomePageView.as_view() , name='homepage'),


]


