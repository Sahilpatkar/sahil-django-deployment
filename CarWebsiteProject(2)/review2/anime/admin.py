from django.contrib import admin

from .models import Review
from .models import Car_Info

admin.site.register(Review)
admin.site.register(Car_Info)