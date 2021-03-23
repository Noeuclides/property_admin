from django.urls import path
from apps.users.views import Login, UserRegister, UserList

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('list/', UserList.as_view(), name='user_list'),
    path('register/', UserRegister.as_view(), name='register'),
]
