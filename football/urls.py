from django.urls import path


from . import views


#specifying app name (it can be used as 'football:homepage')

app_name='football'

urlpatterns = [
    path('' , views.HomePageView.as_view() , name='homepage'),
    path('players/' , views.PlayerList.as_view() , name='players'),
    path('clubs/' ,views.ClubList.as_view() ,name='clubs'),
    

]


