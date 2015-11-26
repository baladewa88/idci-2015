from django import forms
from .models import Papers

class PaperForm(forms.ModelForm):

    class Meta:
        model = Papers
        fields = ('title','abstract',)

class PaperSearch(forms.ModelForm):

    class Meta:
        model = Papers
        fields = ('title',)
