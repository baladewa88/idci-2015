from django import forms
from .models import Papers, Authors

class PaperForm(forms.ModelForm):

    class Meta:
        model = Papers
        fields = ('title','abstract',)

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
        model = Papers
        fields = ('publisher',)
