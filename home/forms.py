from django import forms
from .models import Registaredfroms
from .models import cars
from .models import usercars
from .models import bookcars
from .models import approve
from .models import reviews
from .models import bookusercars
from django.http import  HttpResponse

class FromRegisterforms(forms.ModelForm):
    class Meta:
        model = Registaredfroms
        fields =["first_name","last_name","username","password","email","phone_no"]

class addcars(forms.ModelForm):
    class Meta:
        model = cars
        fields =["cars_name","cars_model","cars_number","cars_colour","price","seat_number"]

class usercarsinfo(forms.ModelForm):
    class Meta:
        model = usercars
        fields=["username","area","cars_name","cars_number","cars_model","cars_colour","price","seat_number","approval"]

class approvedcarsinfo(forms.ModelForm):
    class Meta:
        model = approve
        fields=["username","area","cars_name","cars_model","cars_number","cars_colour","price","seat_number"]

class bookinfo(forms.ModelForm):
    class Meta:
        model = bookcars
        fields=["username","address","ending_date","cars_number"]

class bookinfouser(forms.ModelForm):
    class Meta:
        model = bookusercars
        fields=["username","address","ending_date","cars_number"]

class feedback(forms.ModelForm):
    class Meta:
        model = reviews
        fields=["advice","rating"]
