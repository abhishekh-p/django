from django import forms
from .models import userm
from .models import userprofile
from .models import blog
from .models import register


class userform(forms.ModelForm):
    class Meta:
        model=userm
        fields='__all__'

        def clean_username(self):
            username = self.cleaned_data.get('user_name')
            if len(username)<3:
                raise forms.ValidationError("username must be at least 3 charecter")
            return username

class userprofiles(forms.ModelForm):
    class Meta:
        model=userprofile
        fields='__all__'



class blogform(forms.ModelForm):
    class Meta:
        model = blog
        fields = '__all__'



class regi(forms.ModelForm):
    class Meta:
        model = register
        fields = '__all__'



# class iim(forms.ModelForm):
#     class Meta:
#         model=img
#         fields='__all__'