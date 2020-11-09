from django import forms
from.models import TOdos



class Listform(forms.ModelForm):
    class Meta:
        model= TOdos
        fields = ["title","description","finished","date"]