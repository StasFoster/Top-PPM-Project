from django import forms
from .models import MyUser

class MyUserForm(forms.ModelForm):
    
    class Meta:
        model = MyUser
        fields = ["username", "password"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].help_text = ""
    