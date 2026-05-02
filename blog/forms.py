from django import forms


class GetArticlesQueryForm(forms.Form):
    q = forms.CharField(max_length=50, min_length=5, required=False)
    # limit = forms.IntegerField(min_value=1, max_value=100)
    # offset = forms.IntegerField(min_value=0)

    # field level validation
    def clean_q(self):
        data = self.cleaned_data

        if data['q'].startswith('ok'):
            raise forms.ValidationError('xato data')

        return data['q'].lower()
    
class WriteArticleForm(forms.Form):
    title = forms.CharField(min_length=5)
    content = forms.CharField(required=False)


    

class RegisterForm(forms.Form):
    email = forms.EmailField()
    password = forms.PasswordInput()
    confirm = forms.PasswordInput()

    # object level validation
    def clean(self):
        data = self.cleaned_data

        if data['password'] != data['confirm']:
            raise forms.ValidationError('password va confirm teng emas.')


        return super().clean()
