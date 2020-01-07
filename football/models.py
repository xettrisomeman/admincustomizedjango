from django.db import models
from django.utils.translation import ugettext_lazy as _


class Player(models.Model):
    first_name = models.CharField(_("First Name"),max_length=50)
    middle_name = models.CharField(_("Middle Name"), max_length=50 , blank=True)
    last_name= models.CharField(_("Last Name"), max_length=50)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
    joined_club = models.ForeignKey("Club", verbose_name=_("Current Club"), on_delete=models.SET_NULL , null=True)
    country = models.CharField(_("Nationality"), max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}"



class Club(models.Model):
    name = models.CharField(_("Club Name"), max_length=50)
    country = models.CharField(_("Nation") , max_length=50)
    date_formed = models.DateField(auto_now=False, auto_now_add=False)


    def __str__(self):
        return self.name

