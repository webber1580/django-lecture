from django.db import models
from group.models import Group


class Student(models.Model):
    name = models.CharField('Name', max_length=50)
    surname = models.CharField('Surname', max_length=50)
    age = models.IntegerField('Age')
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return f'/student/{self.id}/details'