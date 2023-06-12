from django.contrib import admin
from .models import Manager

class ManagerAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','username','password')

admin.site.register(Manager,ManagerAdmin)
# Register your models here.
