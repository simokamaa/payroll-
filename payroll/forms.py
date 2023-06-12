from django import forms
from first.models import Manager

class ManagerForm(forms.Form):
    
    class Meta:
        model = Manager
        fields = "__all__"
        