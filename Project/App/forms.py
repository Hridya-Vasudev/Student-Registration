from django import forms
from .models import Student

class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['enquiry_no', 'enquiry_date', 'name', 'gender', 'qualification',
                  'address', 'college', 'contact_no', 'whatsapp_no', 'dob', 'has_work_experience']

class StudentLoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)