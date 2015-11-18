from django.contrib import admin
from .models import Papers
from .models import Urls

# Register your models here.
admin.site.register(Papers)
admin.site.register(Urls)
