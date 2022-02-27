from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView, UpdateView, DeleteView
from group.forms import GroupForm
from group.models import Group


def index(request):
    data = {
        'collection_size': Group.objects.all().count(),
        'collection': Group.objects.all()
    }
    return render(request, 'group/index.html', data)


def create(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            group = Group()
            group.name = form.cleaned_data['name']
            group.size = 0
            group.save()
            return redirect('group')
        else:
            error = "Ошибка в заполнении формы"

    data = {
        'form': GroupForm(),
        'error': '',
    }
    return render(request, 'group/create.html', data)


def details(request, pk):
    data = {
        'group': Group.objects.get(id=pk)
    }
    return render(request, 'group/details.html', data)


# def edit(request, pk):
#     group = Group.objects.get(id=pk)
#     if request.method == 'PUT':
#         form = GroupForm(request.PUT)
#         if form.is_valid():
#             group.name = form.cleaned_data['name']
#             group.save()
#             return redirect('group')
#         else:
#             error = "Ошибка в заполнении формы"
#
#     data = {
#         'form': GroupForm(group),
#         'error': '',
#     }
#     return render(request, 'group/create.html', data)

class GroupUpdateView(UpdateView):
    model = Group
    template_name = 'group/edit.html'
    fields = ['name']


class GroupDeleteView(DeleteView):
    model = Group
    template_name = 'group/delete.html'
    success_url = '/group'


def delete(request):
    return render(request, 'group/index.html')
