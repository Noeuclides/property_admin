from django.urls import path
from apps.users.views import Login, UserRegister, UserList, user_logout

urlpatterns = [
    path('login', Login.as_view(), name='login'),
    path('logout', user_logout, name='logout'),
    path('lista', UserList.as_view(), name='user_list'),
    path('registro', UserRegister.as_view(), name='register'),
]
