from django import forms


class AddDogForm(forms.Form):
    owner_name = forms.CharField(label='Owner name:', max_length=50)
    dog_name = forms.CharField(label='Dog name:', max_length=50)
    image = forms.ImageField()


class SearchForm(forms.Form):
    query = forms.CharField(label='Search:', max_length=50)
