from django.db import models

from django.utils import timezone

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return '{}'.format(self.name)

class Project(models.Model):
    client = models.ForeignKey('Client')
    name = models.CharField(max_length=200)

    def __str__(self):
        return '<{}> {}'.format(self.client, self.name)


class Entry(models.Model):
    start = models.DateTimeField(default=timezone.now)
    stop = models.DateTimeField(blank=True, null=True)
    project = models.ForeignKey('Project')
    description = models.CharField(max_length=200)

    def __str__(self):
        return '[{} - {}] ({}) {}'.format(self.start, self.stop, self.project, self.description)

    def is_finished(self):
        return self.stop is not None

    class Meta:
        verbose_name_plural = "Entries"
