from django.shortcuts import (
    render, get_object_or_404)
from django.http import HttpResponseRedirect
from django import forms

from dogs.models import Owner


class AddDogForm(forms.Form):
    owner_name = forms.CharField(label='Owner name:', max_length=50)
    dog_name = forms.CharField(label='Dog name:', max_length=50)
    image = forms.ImageField()


class SearchForm(forms.Form):
    query = forms.CharField(label='Search:', max_length=50)


def index(request):
    ''' Main page displaying all owners & dogs.  If search has been submitted,
        displays search results.
    '''
    owner_list = []
    error_message = ''

    if request.method == 'POST':
        form = SearchForm(request.POST)

        if form.is_valid():
            query = form.cleaned_data['query']
            if Owner.objects.filter(name__contains=query).exists():
                owner_list = Owner.objects.filter(name__contains=query)
            else:
                error_message = 'No results found.'
        else:
            error_message = 'Invalid query; please try again.'
    else:
        owner_list = Owner.objects.all()
        form = SearchForm()

    context = {'owner_list': owner_list, 'form': form}
    if error_message:
        context['error_message'] = error_message

    return render(request, 'dogs/index.html', context)


# TODO:  Dog detail should appear in lightbox, not separate window.
def dog_detail(request, owner_id):
    owner = get_object_or_404(Owner, pk=owner_id)
    return render(request, 'dogs/dog_detail.html', {'owner': owner})


def add(request):
    ''' Add an owner & dog.  Form takes owner name, dog name, and image file;
        thumbnail image is automatically generated from submitted image.
    '''
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
