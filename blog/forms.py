from django import forms


class GetArticlesQueryForm(forms.Form):
    q = forms.CharField(max_length=50, min_length=5, required=False)
    # limit = forms.IntegerField(min_value=1, max_value=100)
    # offset = forms.IntegerField(min_value=0)

