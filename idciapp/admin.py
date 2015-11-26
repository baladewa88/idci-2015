from django.contrib import admin
from .models import Papers
from .models import Urls, Citations, Keywords

# Register your models here.
admin.site.register(Papers)
admin.site.register(Urls)
admin.site.register(Citations)
admin.site.register(Keywords)
