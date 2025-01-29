from django.contrib import admin
from .models import Buch, Autor

admin.site.register([Buch])
admin.site.register([Autor])
# Register your models here.
