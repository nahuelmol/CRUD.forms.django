from django import forms
<<<<<<< HEAD
from .models import Contact,Countries
=======
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from .models import Contact
>>>>>>> c3219e750c5c06f187097b7f923f5db793807721

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"

<<<<<<< HEAD
class CountriesForm(forms.ModelForm):
	class Meta:
		model = Countries
		fields = "__all__"
=======
class Creater_User(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
>>>>>>> c3219e750c5c06f187097b7f923f5db793807721
