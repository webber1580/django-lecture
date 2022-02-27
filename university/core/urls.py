from django.urls import path, include

urlpatterns = [
    path('', include('home.urls')),
    path('student/', include('student.urls')),
    path('group/', include('group.urls')),
]
