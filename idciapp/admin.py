from django.contrib import admin
from .models import Papers, Citations
from .models import Urls, Citations, Keywords, Authors
from .forms import CitationInlineFormset

# Register your models here.

class CitationInline(admin.StackedInline):
    model = Citations
    extra = 3
    exclude = ['id', 'cluster']
    #list_display = ('authors','title','venue','venueType','year','pages','editors','publisher','pubAddress','volume','number','raw')

#    model = YourInlineModel
    formset = CitationInlineFormset

    def get_formset(self, request, obj=None, **kwargs):
        formset = super(CitationInline, self).get_formset(request, obj, **kwargs)
        formset.request = request
        return formset
    
class KeywordsInline(admin.TabularInline):
    model = Keywords
    extra = 3
    exclude = ['id']
    #list_display = ('id','title','ncites','selfcites')
    

class UrlInline(admin.TabularInline):
    model = Urls
    exclude = ['id']

class AuthorInline(admin.StackedInline):
    model = Authors
    extra = 3
    exclude = ['id','cluster']

class PapersAdmin(admin.ModelAdmin):
    fieldsets = [('Description',{'fields':['title','abstract','year', 'venue', 'venuetype', 'pages', 'volume', 'number','selfcites']}),
                ('Publisher',{'fields':['publisher','pubaddress']}),
                 ('Status',{'fields':['version','versionname','public']}),]
    list_filter = [('crawldate')]
    list_display = ('id','title','ncites','selfcites')
    ordering = ('-crawldate',)
    exclude = ['id']

    a=0
    def save_model(self, request, obj, form, change):
        rowCount = Papers.ea.all().count()
        refCount = Citations.objects.filter(title=form.cleaned_data['title']).count()
        a = rowCount+1
        obj.id=""+str(a)
        print ("Jumlah => "+str(a))
        print ("Jumlah => "+str(obj.id))
        print ("Jumlah 2 => "+str(refCount))
        obj.ncites = refCount
        obj.save()

    inlines =[CitationInline,KeywordsInline,UrlInline,AuthorInline]

class CitationAdmin (admin.ModelAdmin):
    fieldsets = [('Citation',{'fields':['paperid','authors','title','venue','venuetype', 'year', 'pages', 'editors','volume', 'number','tech','raw']}),
                ('Publisher',{'fields':['publisher','pubaddress']}),]
    list_display = ('id','authors','title')
    ordering = ('-id',)

    def save_model(self, request, obj, form, change):
        
        print (form.cleaned_data['authors'])
        obj.self=0
        obj.save()

admin.site.register(Papers, PapersAdmin)
admin.site.register(Citations, CitationAdmin)
