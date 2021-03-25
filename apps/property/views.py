from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Value as V
from django.db.models.expressions import Case, When
from django.db.models.functions import Concat
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from apps.property.forms import RegisterForm
from apps.property.models import Property
from apps.users.models import User


def home(request):
    return render(request, 'property/home.html')


class PropertyList(LoginRequiredMixin, ListView):
    model = Property
    template_name = 'property/user_list.html'
    login_url = reverse_lazy('users:login')
    context_object_name = 'property_obj'

    def get_queryset(self):
        return self.model.objects.select_related('owner').annotate(
            address=Case(
                When(rural__isnull=False, then='rural'),
                default=Concat('street', V(' '), 'street_number',
                               V(' #'), 'corner', V(' - '), 'corner_number')
            )
        )


class PropertyOwnerList(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'property/user_properties.html'
    # login_url = reverse_lazy('users:login')
    context_object_name = 'owner'

    def get_context_data(self, **kwargs):
        context = super(PropertyOwnerList, self).get_context_data(**kwargs)
        properties = Property.objects.filter(owner=self.request.user).annotate(
            address=Case(
                When(rural__isnull=False, then='rural'),
                default=Concat('street', V(' '), 'street_number',
                               V(' #'), 'corner', V(' - '), 'corner_number')
            )
        )

        context['property_obj'] = properties

        return context


class PropertyRegister(LoginRequiredMixin, CreateView):
    model = Property
    form_class = RegisterForm
    template_name = 'property/register_property.html'
    # login_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = User.objects.get(id=self.request.user.id)
        form.instance.owner = user
        return super(PropertyRegister, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('property:owner_properties', kwargs={'pk': self.request.user.id})


class PropertyUpdate(LoginRequiredMixin, UpdateView):
    model = Property
    form_class = RegisterForm
    template_name = 'property/register_property.html'

    def get_success_url(self):
        return reverse_lazy('property:owner_properties', kwargs={'pk': self.request.user.id})


class PropertyDelete(LoginRequiredMixin, DeleteView):
    model = Property
    form_class = RegisterForm
    template_name = 'property/delete_property.html'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        property = Property.objects.filter(pk=self.object.id)
        property.delete()
        return HttpResponseRedirect(success_url)

    def get_success_url(self):
        return reverse_lazy('property:owner_properties', kwargs={'pk': self.request.user.id})
