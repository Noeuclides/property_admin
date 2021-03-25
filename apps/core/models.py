# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from django.conf import settings


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    _deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True
        ordering = ["-created_at"]

    def delete(self):
        self._deleted = True
        self.save()

    def __str__(self):
        name = self.__class__.__name__
        return f"{name} {self.pk}"


class AddressModel(BaseModel):
    CALLE = 0
    CARRERA = 1
    AVENIDA = 2
    AVENIDA_CARRERA = 3
    AVENIDA_CALLE = 4
    CIRCULAR = 5
    CIRCUNVALAR = 6
    DIAGONAL = 7
    MANZANA = 8
    TRANSVERSAL = 9
    VIA = 10
    ADDRESS = (
        (CALLE, 'Calle'),
        (CARRERA, 'Carrera'),
        (AVENIDA, 'Avenida'),
        (AVENIDA_CARRERA, 'Avenida Carrera'),
        (AVENIDA_CALLE, 'Avenida Calle'),
        (CIRCULAR, 'Circular'),
        (CIRCUNVALAR, 'Circunvalar'),
        (DIAGONAL, 'Diagonal'),
        (MANZANA, 'Manzana'),
        (TRANSVERSAL, 'Transversal'),
        (VIA, 'Vía'),
    )
    street = models.PositiveSmallIntegerField(choices=ADDRESS, default=None, null=True, blank=True)
    street_number = models.CharField(max_length=10, null=True, blank=True)
    corner = models.CharField(max_length=10, null=True, blank=True)
    corner_number = models.IntegerField(null=True, blank=True)
    rural = models.CharField(max_length=255, verbose_name="Dirección rural", null=True, blank=True)

    class Meta:
        abstract = True
        ordering = ["-created_at"]
