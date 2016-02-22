from dal import autocomplete
from django import forms
from .models import Papers, Authors, Affiliations
import django_filters

class PaperFilter(django_filters.FilterSet):
    class Meta:
        model = Papers
        fields = ['title','venue', 'year']
        
class PaperForm(forms.ModelForm):
    
    '''
    paper_id = forms.ModelChoiceField(
        choices=Papers.ea.all(),
        widget=autocomplete.ModelSelect2(url='country-autocomplete')
    )
'''
    class Meta:
        model = Papers
        fields = ('__all__')
        widgets = {
            'paper_id': autocomplete.ModelSelect2(url='country-autocomplete')
        }

class PaperSearch(forms.ModelForm):

    class Meta:
        model = Papers
        fields = ('title',)

class AuthorSearch(forms.ModelForm):

    class Meta:
        model = Authors
        fields = ('name',)

class PublisherSearch(forms.ModelForm):

    class Meta:
        model = Affiliations
        fields = ('name',)

class CitationInlineFormset(forms.models.BaseInlineFormSet):
     def save_new(self, form, commit=True):
        obj = super(CitationInlineFormset, self).save_new(form, commit=False)
        # here you can add anything you need from the request
        refCek = Papers.ea.filter(title=obj.title).count()
        print ("ksajdhkas "+str(refCek))

        if refCek > 0:
            paper = Papers.ea.get(title=obj.title)
            paper.ncites = paper.ncites+1
            paper.save()
        
        if commit:
            obj.save()

        return obj
