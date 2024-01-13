from django import forms
from .models import Car_Info
'''
class ReviewForm(forms.Form):
	name = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'class' : 'form-control','placeholder':'Name'}))
	review = forms.CharField(widget=forms.Textarea(attrs={'form':'form-control', 'placeholder':'Review'}))
'''
class ReviewForm(forms.Form):
    name = forms.CharField(max_length=20, 
        widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Name',}))
    review = forms.CharField(widget=forms.Textarea(attrs={'class' : 'form-control', 'placeholder' : 'Review'}))

class FormName(forms.Form):
	Car = Car_Info.objects.order_by('CarName')

	category = forms.ChoiceField(choices=[(i,i)for i in Car])

	category2 = forms.ChoiceField(choices=[(i,i)for i in Car])

class FormName2(forms.Form):
	Car = Car_Info.objects.all()

	category = forms.ChoiceField(choices=[(i,i)for i in Car])


		