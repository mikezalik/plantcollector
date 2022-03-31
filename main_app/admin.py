from django.contrib import admin

# Register your models here.
from .models import Plant, Care, Photo

admin.site.register(Plant)
admin.site.register(Care)
admin.site.register(Photo)
