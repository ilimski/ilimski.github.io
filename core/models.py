from django.db import models


class Faculty(models.Model):
    class Meta:
        verbose_name = 'Faculty'
        verbose_name_plural = 'Faculties'

    name = models.CharField(max_length=255, verbose_name='name')
    desc = models.TextField(verbose_name='desc')
    ort_needed = models.PositiveIntegerField(default=150, verbose_name='needed ort')
    fee = models.PositiveIntegerField(default=700, verbose_name='fee')

    def __str__(self):
        return self.name
