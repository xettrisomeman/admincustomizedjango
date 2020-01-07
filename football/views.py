from django.views.generic import (
    TemplateView,
    ListView

)



from .models import (
    Player,
    Club
)


class HomePageView(TemplateView):
    template_name = 'football/homepage.html'


class PlayerList(ListView):
    model = Player
    template_name= 'football/listdisplay.html'
    context_object_name = 'players'

class ClubList(ListView):
    model= Club
    template_name = 'football/listclub.html'
    context_object_name= 'clubs'

