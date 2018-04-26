from django import forms
from blog_app.models import Prize,Userprize,Trip,Vote,Story,Storycomment,Tripcomment,Userprofile
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db import models
import datetime
from django.contrib.auth.password_validation import validate_password

class TripForm(forms.ModelForm):
    class Meta():
        model = Trip

        fields = ('date','title','details')

        widgets = {
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'details':forms.Textarea(attrs={'class':'editable medium-editors-textarea tripcontent'}),
        }
    def clean_date(self):
        date = self.cleaned_data['date']
        if date > datetime.date.today():
            raise forms.ValidationError("Enter a valid date!")
        return date

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['date'].label = 'Trip Date'
        self.fields['title'].label = 'Trip Title'
        self.fields['details'].label = 'Trip Details'


class StoryForm(forms.ModelForm):
    class Meta():
        model = Story
        fields = ('date','details')

        widgets = {
            'details':forms.Textarea(attrs={'class':'editable medium-editors-textarea'})
        }

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['date'].label = 'Story Date'
        self.fields['details'].label = 'Story Details'

class TripCommentForm(forms.ModelForm):
    class Meta():
        model = Tripcomment
        fields = ('comment',)

        widgets = {
            'comment':forms.Textarea(attrs={'class':'editable medium-editors-textarea'}),
        }

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['comment'].label = 'Comment'

class StoryCommentForm(forms.ModelForm):
    class Meta():
        model = Storycomment
        fields = ('comment',)

        widgets = {
            'comment':forms.Textarea(attrs={'class':'editable medium-editors-textarea'}),
        }

class UserProfileForm(forms.ModelForm):
    class Meta():
        model = Userprofile
        fields = ('profilepic',)

    def __init__(self,*args,**kwargs):
       super().__init__(*args,**kwargs)
       self.fields['profilepic'].label = 'Profile Picture'

class UserForm(UserCreationForm):

   class Meta():
        model = User
        fields = ('username','first_name','last_name','email','password1','password2',)

   def save(self,commit=True):
       user = super(UserForm,self).save(commit=False)
       user.username = self.cleaned_data["username"]
       user.email = self.cleaned_data["email"]
       user.first_name = self.cleaned_data["first_name"]
       user.last_name = self.cleaned_data["last_name"]
       user.password1 = self.cleaned_data["password1"]
       user.password2 = self.cleaned_data["password2"]
       if commit:
           user.save()
       return user


   def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].label = 'Username'
        self.fields['first_name'].label = 'First Name'
        self.fields['last_name'].label = 'Last Name'
        self.fields['email'].label = 'Email Address'
        self.fields['password1'].label = 'Password'
        self.fields['password2'].label = 'Re-enter Password'
