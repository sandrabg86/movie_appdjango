# coding=utf-8

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Movie(models.Model):
    tittle = models.CharField(max_length=100, verbose_name="Título")
    director = models.CharField(max_length=100)
    year = models.IntegerField()
    point = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)],
                                verbose_name="Nota Media")

    class Meta:
        unique_together = ('tittle', 'director')
