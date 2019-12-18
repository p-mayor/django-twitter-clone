from django import forms

class TwitterUserForm(forms.Form):
    twitter_user_name = forms.CharField(max_length=20)
    twitter_user_bio = forms.CharField(widget=forms.Textarea)

