
from django import forms
from filter_app.models import *

GENDER_CHOICE= (
    ('Male','Male'),
    ('Female','Female'),
)

class JobDescriptionForm(forms.ModelForm):

    gender = forms.ChoiceField( widget=forms.RadioSelect,choices=GENDER_CHOICE, required=False)
    class Meta:
        model = JobDescription
        exclude = ['status']
        fields = ("__all__")
        labels = {
            'title' : 'Job title',
            'level' : 'Level of Study',
            'gender_preference' : 'Gender Preference',
            'qualification' : 'Tutor’s Qualifications',
            'description' : 'Job description',
            'experience' : 'Experience',
            'budget' : 'Budget Range',
        }   
        widgets = {
            'title' : forms.TextInput(attrs={'placeholder' : 'Add title', 'class':'form-control'}),
            'level' : forms.Select(attrs={'class':'form-control', 'placeholder' : 'Select a level of Study'}),
            'description' : forms.Textarea(attrs={'class':'form-control', 'placeholder' : 'Type the description here...'}),
            'budget' : forms.Select(attrs={'class':'form-control', 'placeholder' : 'Select range'}),
            'experience' : forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'E.g. Minimum 3 years'}),
        }
