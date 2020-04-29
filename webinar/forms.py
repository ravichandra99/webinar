from django import forms
from django.forms import ModelForm
from webinar.models import JustUser

class UserForm(ModelForm):
	class Meta:
		model = JustUser
		fields = '__all__'

class EditForm(forms.Form):
	subject = forms.CharField(label='Subject', max_length=100)
	body = forms.CharField(widget=forms.Textarea)
