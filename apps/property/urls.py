from django.urls import path

from apps.property.views import (PropertyDelete, PropertyList,
                                 PropertyOwnerList, PropertyRegister,
                                 PropertyUpdate, CompanyRegister)

urlpatterns = [
    path('lista', PropertyList.as_view(), name='properties'),
    path('detalle/<int:pk>', PropertyOwnerList.as_view(), name='owner_properties'),
    path('actualizar/<int:pk>', PropertyUpdate.as_view(), name='property_update'),
    path('eliminar/<int:pk>', PropertyDelete.as_view(), name='property_delete'),
    path('registro', PropertyRegister.as_view(), name='register_property'),
    path('registro-empresa', CompanyRegister.as_view(), name='register_company'),
]
