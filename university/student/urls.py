from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='student'),
    path('create', views.create, name='student_create'),
    path('details', views.details, name='student_details'),
    path('edit', views.edit, name='student_edit'),
    path('delete', views.delete, name='student_delete'),
]
