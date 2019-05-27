from django.conf import settings
from django.db import models


class Zone(models.Model):
    name = models.CharField(max_length=128)
    notes = models.TextField(blank=True, null=True)
    active = models.BooleanField(blank=True, default=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'


class Report(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reports')
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    notes = models.TextField(blank=True, null=True)
    active = models.BooleanField(blank=True, default=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.zone} - {self.name} by <{self.user}>'
