from django.db import models


class Group(models.Model):
    name = models.CharField('Name', max_length=50)
    size = models.IntegerField('Age')

    def get_absolute_url(self):
        return f'/group/{self.id}/details'
