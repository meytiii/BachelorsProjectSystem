
from django.urls import path
from .views import UserLoginView, home

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('', home, name='home'),
]
