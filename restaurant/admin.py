from django.contrib import admin
from .models import Menu, Booking

# Registrar os modelos no admin do Django
admin.site.register(Menu)
admin.site.register(Booking)
