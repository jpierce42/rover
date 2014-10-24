from django.shortcuts import (
    render, get_object_or_404)
from django.http import HttpResponseRedirect

from dogs.models import Owner, Dog
from dogs.forms import AddDogForm, SearchForm


def index(request):
    ''' Main page displaying all owners & dogs.  If search has been submitted,
        displays search results.
    '''
    owner_list = []
    error_message = ''

    if request.GET.items():
        form = SearchForm(request.GET)

        if form.is_valid():
            query = form.cleaned_data['query']

            if Owner.objects.filter(name__contains=query).exists():
                owner_list.extend(
                    list(Owner.objects.filter(name__contains=query)))

            if Dog.objects.filter(name__contains=query).exists():
                for dog in list(Dog.objects.filter(name__contains=query)):
                    if dog.owner not in owner_list:
                        owner_list.append(dog.owner)

            if not owner_list:
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

                o.dog_set.create(
                    name=dog_name, image=form.cleaned_data['image'])

                return HttpResponseRedirect('/')

    else:
        form = AddDogForm()

    return render(request, 'dogs/add.html', {'form': form})
