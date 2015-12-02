from django.contrib import admin
from .models import Papers
from .models import Urls, Citations, Keywords

# Register your models here.

class PapersAdmin(admin.ModelAdmin):
    fieldsets = [('Description',{'fields':['id','title','abstract','year', 'venue', 'venuetype', 'pages', 'volume', 'number']}),
                ('Publisher',{'fields':['publisher','pubaddress']}),
                 ('Status',{'fields':['version','versionname','public']}),]
    list_filter = [('crawldate')]
    ordering = ('-crawldate',)
    
admin.site.register(Papers, PapersAdmin)
admin.site.register(Urls)
admin.site.register(Citations)
admin.site.register(Keywords)
