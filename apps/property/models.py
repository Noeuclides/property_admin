from django.db import models
from apps.users.models import User
from apps.core.models import AddressModel
from django.core.exceptions import ValidationError

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

    @property
    def address(self):
        if self.rural:
            return self.rural
        STR_CHOICES = { key : value for (key,value) in self.ADDRESS }
        return f'{STR_CHOICES[self.street]} {self.street_number} #{self.corner} - {str(self.corner_number)}'


    def clean(self):
        if self.type == 1:
            address = [self.street, self.street_number, self.corner, self.corner_number]
            self.rural = None
            if not all(address):
                raise ValidationError("Se deben llenar los cuatro campos de dirección urbana")
        if self.type == 2:
            self.street = None
            self.street_number = None
            self.corner = None
            self.corner_number = None
            if not self.rural:
                raise ValidationError("se debe llenar el campo de nombre rural.")

        
    def __str__(self):
        """Unicode representation of Property."""
        return f'{self.owner} property {self.cadastral_id}'
