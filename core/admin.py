from django.contrib import admin
from .models import Markets,Match,Selections,Sport
# Register your models here.

admin.site.register(Markets)
admin.site.register(Match)
admin.site.register(Selections)
admin.site.register(Sport)