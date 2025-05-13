from django import forms

class ReviewForm(forms.Form):
    user_name = forms.CharField(label="Your Name", max_length=50, error_messages={
        "required": "Name can not be empty!",
        "max_length": "Max character length must be shorter than 50 characters!"
    })