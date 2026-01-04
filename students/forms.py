from django import forms
from .models import Students

class DateInput(forms.DateInput):
    input_type='date'

class StudentForm(forms.ModelForm):
    class Meta:
        model=Students
        fields=['roll_no','name','email','phone_no','course','year','dob','gender','address']
        widgets={'dob': DateInput(), 'address': forms.Textarea(attrs={'rows':3})}