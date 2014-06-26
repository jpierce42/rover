from django.shortcuts import (
    render, redirect, get_object_or_404)
from django.http import HttpResponseRedirect
# from django.core.urlresolvers import reverse
from django.forms import ModelForm
from dogs.models import Owner, Dog


# class OwnerForm(ModelForm):
#     class Meta:
#         model = Owner
#         fields = ['name']


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
        owner_name = request.POST['owner_name']
        dog_name = request.POST['dog_name']

        # Check to see if an owner with this name already exists
        if Owner.objects.filter(name=owner_name).exists():
            print 'owner exists!'
            return render(request, 'dogs/add.html', {
                'error_message': 'An owner with this name already exists.'
            })
        else:
            o = Owner(name=owner_name)
            o.save()

            o.dog_set.create(name=dog_name)
            o.save()

            # return render(request, 'dogs/index.html')
            return redirect('dogs:index')

    else:
        return render(request, 'dogs/add.html')

# TODO:  use ModelForm

# def add(request):
#     if request.method == 'POST':
#         owner_name = request.POST['owner_name']

#         # Check to see if an owner with this name already exists
#         if Owner.objects.get(name=owner_name).exists():
#             print 'owner exists!'
#             return render(request, 'dogs/add.html', {
#                 'error_message': 'An owner with this name already exists.'
#             })
#         else:
#             o = Owner(name=owner_name)
#             o.save()
#             return render(request, 'dogs/index.html')

#     else:
#         form = OwnerForm()

#     return render(request, 'dogs/add.html', {
#         'form': form,
#     })
