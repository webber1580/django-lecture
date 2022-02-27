from django.shortcuts import render, redirect
from student.models import Student
from student.forms import StudentForm
from group.models import Group


def index(request):
    data = {
        'collection_size': Student.objects.all().count(),
        'collection': Student.objects.all()
    }
    return render(request, 'student/index.html', data)


def details(request):
    data = {
        'collection_size': Student.objects.all().count(),
        'collection': Student.objects.all()
    }
    return render(request, 'student/details.html', data)


def create(request):
    form = StudentForm()
    error = ''

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid() and Group.objects.filter(id=form.cleaned_data['group_id']).exists():
            student = Student()
            student.name = form.cleaned_data['name']
            student.surname = form.cleaned_data['surname']
            student.age = form.cleaned_data['age']
            student.group_id = form.cleaned_data['group_id']
            student.save()
            return redirect('student')
        else:
            error = "Ошибка в заполнении формы"

    data = {
        'form': form,
        'error': error,
    }
    return render(request, 'student/create.html', data)


def edit(request):
    data = {
        'collection_size': Student.objects.all().count(),
        'collection': Student.objects.all()
    }
    return render(request, 'student/edit.html', data)


def delete(request):
    data = {
        'collection_size': Student.objects.all().count(),
        'collection': Student.objects.all()
    }
    return render(request, 'student/delete.html', data)
