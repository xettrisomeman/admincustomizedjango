from django.contrib import admin



from .models import (
    Club ,
    Player
)

#registering the models in admin


#first create a custom modelAdmin

class PlayerAdmin(admin.ModelAdmin):
    list_display = ('date_of_birth' , 'country') #this we want to display on admin page
    list_filter= ('first_name' , )#we want to filter the list by first name
    ordering = ('country' , ) #order the display page by nationality
    search_fields = ('first_name' , ) #search captures the first name and search according to it
    fieldsets = (
        #classifying the info as according to the class
        ('Personal Info', {
            "fields": (
                'first_name' , 'middle_name' , 'last_name'
            ),
        }),
        #this show up as a header
        ('Date Of Birth' , {
            'fields':(
                'date_of_birth',
            )
        }),
        ('Club' , {
            'fields':(
                'joined_club',
            )
        }),
        ('Nationality' , {
            'fields' : (
                'country',
            )
        })

    )


class ClubAdmin(admin.ModelAdmin):
    list_display = ('name' , 'country')
    search_fields = ('country' , )
    fieldsets = (
        ('Club Info', {
            "fields": (
                'name', 'country' , 'date_formed'
            ),
        }),
    )
       

admin.site.register(Player , PlayerAdmin)
admin.site.register(Club , ClubAdmin)

