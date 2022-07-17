from django.contrib import admin
from .models import Prisoner


admin.site.site_header = "PMS Admin"
admin.site.site_title = "PMS Admin Area"
admin.site.index_title = "Welcome to the PMS Admin Area"


class PrisonerAdmin(admin.ModelAdmin) :
    model = Prisoner
    list_display = ['first_name','last_name','id_number',]

admin.site.register(Prisoner,PrisonerAdmin)
