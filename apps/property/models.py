from django.db import models
from apps.users.models import User
from apps.core.models import AddressModel

# Create your models here.

class Property(AddressModel):
    """Model definition for Property."""
    URBAN = 1
    RURAL = 2
    TYPE = (
        (URBAN, 'Urbano'),
        (RURAL, 'Rural')
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.PositiveSmallIntegerField(choices=TYPE, verbose_name="tipo de predio", default=None)
    cadastral_id = models.CharField("Cédula catastral", max_length=50, unique=True)
    registration_number = models.CharField("Número de matrícula inmobiliaria", max_length=250, unique=True)

    class Meta:
        """Meta definition for Property."""

        verbose_name = 'Property'
        verbose_name_plural = 'Properties'

    def __str__(self):
        """Unicode representation of Property."""
        return f'{self.owner} property {self.cadastral_id}'
