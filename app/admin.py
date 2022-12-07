from django.contrib import admin
from .models import Footballer
from .models import FootballerScore
# Register your models here.

admin.site.register(Footballer)
admin.site.register(FootballerScore)