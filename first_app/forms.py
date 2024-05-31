from django import forms
import datetime
from . import models
BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]
CHOISES = [
    ('b', 'Beef'),
    ('g', 'Grill'),
    ('c', 'Chicken'),
]
class PracticeForm(forms.Form):
    name = forms.CharField(max_length=255,initial="omor faruk")
    comment = forms.CharField(widget=forms.Textarea(attrs={'row' : 10}),label="drop your comments here",help_text= "write commetn in 100 words")
    email = forms.EmailField(max_length=255,required=False)
    agree = forms.BooleanField()
    date = forms.DateField(widget=forms.DateInput(attrs={'type' : 'date'}),initial= datetime.date.today)
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    num = forms.DecimalField()
    favorite_color = forms.ChoiceField(widget=forms.RadioSelect,choices=FAVORITE_COLORS_CHOICES)
    favorite_food = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices = CHOISES)
    

# modelform er kaj shuru

class EmployForm(forms.ModelForm):
    file = forms.FileField()
    class Meta:
        model = models.EmployModel
        fields = '__all__'
        widgets = {
            'salary_date': forms.DateInput(attrs={'type': 'date'}),
            'launch_break' : forms.DateTimeInput(attrs={'type' : 'datetime-local'})
        }
        
        
# class CompanyForm(forms.ModelForm):
#     class Meta:
#         models = models.Company
#         fields = '__all__'
        
        