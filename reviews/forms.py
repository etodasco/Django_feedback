from django import forms

class ReviewForm(forms.Form):
    user_name = forms.CharField(label="Your Name", max_length=50, error_messages={
        "required": "Name can not be empty!",
        "max_length": "Max character length must be shorter than 50 characters!"
    })
    review_text = forms.CharField(label="Your Feedback", widget=forms.Textarea, max_length=200)
    rating = forms.IntegerField(label="Your Rating", min_value=1, max_value=5)