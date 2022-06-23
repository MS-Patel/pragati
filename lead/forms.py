from dataclasses import fields
from django.forms import ModelForm
from .models import Category, Connector,Service_types,Lead

class Category_form(ModelForm):
    class Meta:
        model=Category
        fields='__all__'


class Service_types_form(ModelForm):
    class Meta:
        model=Service_types
        fields='__all__'

class Connector_form(ModelForm):
    class Meta:
        model=Connector
        fields='__all__'

class Lead_form(ModelForm):
    class Meta:
        model=Lead
        fields='__all__'
