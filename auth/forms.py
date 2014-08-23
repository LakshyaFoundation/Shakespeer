from django import forms
 
from login.models import *
 
from functools import partial

 
 
class ProfileUserForm(forms.ModelForm):
    """
        Seprating the User model with Profile Details.
        As Form saving can be done directly instead of bulky code.
        ProfileForm is made different.
    """
 
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
 
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
 
    def clean(self):
        """
            clean function performs all the validation before saving.
        """
 
        data = super(ProfileUserForm, self).clean()
        if 'email' in self.data and User.objects.filter(email=self.data['email']).exists():
            raise forms.ValidationError("Email should be unique.")
 
#    Checks if the passwords entered matches or not
        elif 'password' in self.data and 'confirm_password' in self.data:
            if self.data['password'] != self.data['confirm_password']:
                raise forms.ValidationError("Passwords don't match. Please enter both fields again.")
            return self.data
 
        else:
            raise forms.ValidationError("Passwords not there.")
 
 
 
class ProfileForm(forms.ModelForm):
    """
        ProfileForm refers to Profile model excluding user details.
    """
 
    class Meta:
        model = Profile
        fields = ['gender']
 
 
 
class AdditionalProfileForm(forms.ModelForm):
    #d_o_b = forms.DateField(widget=SelectDateWidget(years=range(datetime.date.today().year, 1930, -1)),label="Date of Birth")
    date_of_birth = forms.DateField(label="Date of birth",widget=DateTimePicker(options={"format":"YYYY-MM-DD","pickTime":False}))
 
    class Meta:
        model = Profile
        fields = ['date_of_birth', 'city', 'state', 'pin', 'country', 'github', 'twitter', 'facebook', 'linkedin']
 
 
class EditProfileUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']
    
 
class EditProfileForm(forms.ModelForm):
    date_of_birth = forms.DateField(label="Date of birth",widget=DateTimePicker(options={"format":"YYYY-MM-DD","pickTime":False}))
 
    class Meta:
        model = Profile
        fields = ['gender', 'date_of_birth', 'city', 'state', 'pin', 'country', 'college_name', 'course', 'year', 'branch', 'cgpa', 'interests', 'github', 'twitter', 'facebook', 'linkedin']
 
class UserForm(forms.ModelForm):
    class Meta:
        model = User