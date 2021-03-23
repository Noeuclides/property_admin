from __future__ import annotations
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)


class UserManager(BaseUserManager):
    def _create_user(
            self, id_card: str, email: str, name: str, last_name: str,
            password: str, is_staff: bool, is_superuser: bool,
            **extra_fields
    ) -> User:
        user = self.model(
            id_card=id_card,
            email=email,
            name=name,
            last_name=last_name,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(
            self, id_card: str, email: str, name: str,
            last_name: str, password: str = None, **extra_fields
    ) -> User:
        return self._create_user(
            id_card,
            email,
            name,
            last_name,
            password,
            False,
            False,
            **extra_fields)

    def create_superuser(
            self, id_card: str, email: str, name: str,
            last_name: str, password: str = None, **extra_fields
    ) -> User:
        return self._create_user(
            id_card,
            email,
            name,
            last_name,
            password,
            True,
            True,
            **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    id_card = models.CharField('Identification card', max_length=50, unique=True)
    email = models.EmailField('email', max_length=255, unique=True)
    name = models.CharField(
        'name', max_length=255, blank=True, null=True)
    last_name = models.CharField(
        'last name', max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['id_card', 'name', 'last_name']

    def __str__(self) -> str:
        return f'{self.name} {self.last_name}'
