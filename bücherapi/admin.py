from django.contrib import admin
from .models import Buch, Autor

class BookAdmin(admin.ModelAdmin):
    filter_horizontal = 'authors' # Ermöglicht das einfache Hinzufügen von Autoren

admin.site.register([Buch])
admin.site.register([Autor])
# Register your models here.
