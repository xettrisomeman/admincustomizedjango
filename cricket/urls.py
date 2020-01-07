from django.urls import path


from . import views

#specifying app name (it can be used as 'cricket:homepage')
app_name='cricket'

urlpatterns = [
    path('cricket/' ,views.HomePageView.as_view() , name='homepage')
]
