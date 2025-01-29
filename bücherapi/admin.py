from django.contrib import admin
from .models import Buch, Autor

class BuchAdmin(admin.ModelAdmin):
    filter_horizontal = ('autors',) # Ermöglicht das einfache Hinzufügen von Autoren


admin.site.register(Autor)
admin.site.register(Buch, BuchAdmin)