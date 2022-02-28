from django.urls import path
from . import views
from .views import StudentUpdateView

urlpatterns = [
    path('', views.index, name='student'),
    path('create', views.create, name='student_create'),
    path('details', views.details, name='student_details'),
    path('<int:pk>/details', views.details, name='student_details'),
    path('<int:pk>/edit', StudentUpdateView.as_view(), name='student_edit'),
    path('<int:pk>/delete', views.delete, name='student_delete'),
]
