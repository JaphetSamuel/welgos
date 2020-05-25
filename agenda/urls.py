from django.urls import path
from . import views

urlpatterns = [
    path('',views.EventListView.as_view(), name='home'),
    path('inscription', views.Inscription.as_view(), name="signup"),

]