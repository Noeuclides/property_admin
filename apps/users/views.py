import json
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.core.serializers import serialize
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, TemplateView, ListView
from apps.users.models import User
from apps.users.forms import LoginForm, RegisterForm
# from apps.users.mixins import LoginYSuperStaffMixin, ValidarPermisosMixin


class Login(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('index')

    @method_decorator(csrf_protect)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(Login, self).form_valid(form)


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/')


class UserList(ListView):
    model = User
    template_name = 'users/user_list.html'

    def get_queryset(self):
        return self.model.objects.filter(is_active=True)


class UserRegister(CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('property:properties')
