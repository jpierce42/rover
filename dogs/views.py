from django.shortcuts import (
    render, get_object_or_404)
from django.http import HttpResponseRedirect
from django import forms

from dogs.models import Owner


class AddDogForm(forms.Form):
    owner_name = forms.CharField(label='Owner name:', max_length=50)
    dog_name = forms.CharField(label='Dog name:', max_length=50)
    image = forms.ImageField()


def index(request):
    owner_list = Owner.objects.all()

    context = {'owner_list': owner_list}
    return render(request, 'dogs/index.html', context)


# TODO:  Dog detail should appear in lightbox, not separate window.
def dog_detail(request, owner_id):
    owner = get_object_or_404(Owner, pk=owner_id)
    return render(request, 'dogs/dog_detail.html', {'owner': owner})


def add(request):
    if request.method == 'POST':
        form = AddDogForm(request.POST, request.FILES)

        if form.is_valid():
            owner_name = form.cleaned_data['owner_name']
            dog_name = form.cleaned_data['dog_name']

            # Check to see if an owner with this name already exists
            if Owner.objects.filter(name=owner_name).exists():
                return render(request, 'dogs/add.html', {
                    'error_message': 'An owner with this name already exists.',
                    'form': form
                })
            else:
                o = Owner(name=owner_name)
                o.save()

                d = o.dog_set.create(name=dog_name)
                o.save()

                d.image = form.cleaned_data['image']
                d.save()

                return HttpResponseRedirect('/dogs/')

    else:
        form = AddDogForm()

    return render(request, 'dogs/add.html', {'form': form})
