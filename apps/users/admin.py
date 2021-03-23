from os import register_at_fork
from django.contrib import admin
from .models import User

admin.site.register(User)