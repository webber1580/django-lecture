from django.urls import path
from . import views
from .views import GroupUpdateView, GroupDeleteView

urlpatterns = [
    path('', views.index, name='group'),
    path('create', views.create, name='group_create'),
    path('<int:pk>/details', views.details, name='group_details'),
    path('<int:pk>/edit', GroupUpdateView.as_view(), name='group_edit'),
    path('<int:pk>/delete', GroupDeleteView.as_view(), name='group_delete'),
]