from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']

    def __init__(self,*args,**kwargs):
        super(CustomUserCreationForm, self).__init__(*args,**kwargs)

        for label,field in self.fields.items():
            field.widget.attrs.update({"class":"form-control"})
