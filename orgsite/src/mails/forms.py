from django import forms
from mails.models import LeaveMessage

class LeaveMessageForm(forms.Form):
	name = forms.CharField(
		max_length=100
	)
	content = forms.CharField(
		max_length=500, 
		widget=forms.Textarea
	)
	email = forms.EmailField(
		max_length=254
	)
