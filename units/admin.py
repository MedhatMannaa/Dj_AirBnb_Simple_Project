from django.contrib import admin
from .models import Unit, Furniture, Country, City, Area, Room

# Register your models here.
admin.site.register(Unit)
admin.site.register(Furniture)
admin.site.register(Room)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Area)
