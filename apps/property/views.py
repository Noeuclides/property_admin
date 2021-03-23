import json
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.core.serializers import serialize
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, TemplateView, ListView
from apps.users.models import User
from apps.users.forms import LoginForm, RegisterForm
# from apps.users.mixins import LoginYSuperStaffMixin, ValidarPermisosMixin



class UserList(ListView):
    model = User
    template_name = 'users/user_list.html'

    def get_queryset(self):
        return self.model.objects.filter(is_active=True)
