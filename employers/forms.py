from django import forms
import re
from .models import JobPosting
from users.models import CustomUser

# Form for employers to submit job postings for review by administrator
class JobPostingForm(forms.ModelForm):
    class Meta:
        model = JobPosting
        fields = [
            'job_name', 
            'job_description', 
            'employer_name', 
            'employer_phone', 
            'employer_email', 
            'minimum_age', 
            'min_pay', 
            'max_pay',
            'application_url',
        ]
        widgets = {
            'job_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter job title'}),
            'job_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Enter job description'}),
            'employer_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter employer name'}),
            'employer_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone number'}),
            'employer_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email address'}),
            'minimum_age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter minimum age (Optional)'}),
            'min_pay': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter minimum pay (Optional)'}),
            'max_pay': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter maximum pay (Optional)'}),
            'application_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enter link to application (If left blank, the student will be prompted to upload their resume instead.)'}),
        }

    
    # Clean the data and verify that the minimum pay isn't higher than the maximum pay
    def clean_min_max_pay(self):
        cleaned_data = super().clean()
        min_pay = cleaned_data.get('min_pay')
        max_pay = cleaned_data.get('max_pay')

        if min_pay and max_pay and min_pay > max_pay:
            raise forms.ValidationError("The minimum pay must be lower than the maximum pay.")
        
        return cleaned_data
    

    def clean_employer_phone(self):
        phone_number = self.cleaned_data.get('employer_phone')
        # Validate phone number format
        if not re.match(r'^(\d{10}|\d{3}-\d{3}-\d{4})$', phone_number):
            raise forms.ValidationError("Invalid phone number format. Use ********** or ***-***-****.")
        return phone_number


    def clean_employer_email(self):
            email = self.cleaned_data.get('employer_email')
            # Validate email format
            if not re.match(r'^[^@]+@[^@]+\.[^@]+$', email):
                raise forms.ValidationError("Invalid email format. Please enter a valid email address.")
            return email