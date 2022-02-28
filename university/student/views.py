from django.shortcuts import render, redirect
from django.views.generic import UpdateView, DeleteView
from student.models import Student
from student.forms import StudentForm
from group.models import Group


def index(request):
    data = {
        'collection_size': Student.objects.all().count(),
        'collection': Student.objects.all()
    }
    return render(request, 'student/index.html', data)


def details(request, pk):
    data = {
        'student': Student.objects.get(id=pk)
    }
    return render(request, 'student/details.html', data)


def create(request):
    form = StudentForm()
    error = ''

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            if Group.objects.filter(id=form.cleaned_data['group_id']).exists():
                student = Student()
                student.name = form.cleaned_data['name']
                student.surname = form.cleaned_data['surname']
                student.age = form.cleaned_data['age']
                student.group_id = form.cleaned_data['group_id']

                group = Group.objects.get(id=form.cleaned_data['group_id'])
                group.size += 1
                student.save()
                group.save()
                return redirect('student')
            else:
                error = "Указан несуществующий номер группы"
        else:
            error = "Ошибка в заполнении формы"

    data = {
        'form': form,
        'error': error,
    }
    return render(request, 'student/create.html', data)


class StudentUpdateView(UpdateView):
    model = Student
    template_name = 'student/edit.html'
    fields = ['name', 'surname', 'age']


# class StudentDeleteView(DeleteView):
#     model = Student
#     template_name = 'student/delete.html'
#     success_url = '/student'

def delete(request, pk):
    if request.method == "POST":
        student = Student.objects.get(id=pk)
        group = Group.objects.get(id=student.group_id)
        student.delete()
        group.size -= 1
        group.save()

        return redirect('/student')

    data = {
        'student': Student.objects.get(id=pk)
    }
    return render(request, "student/delete.html", data)
