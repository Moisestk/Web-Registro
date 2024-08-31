from django import forms
from .models import Personal, Tipo

        
class TipoForm (forms.ModelForm):
    class Meta:
        model = Tipo
        fields = "__all__"
        

class PersonalForm (forms.ModelForm):
    class Meta :
        model = Personal
        fields = "__all__"
        
        