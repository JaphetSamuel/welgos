from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('inscription', views.Inscription.as_view(), name="signup")
]