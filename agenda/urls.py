from django.urls import path
from . import views

urlpatterns = [
    path('',views.EventListView.as_view(), name='home'),
    path('organisateur/', views.OrganisationListView.as_view(), name='list-org'),
    path('inscription', views.Inscription.as_view(), name="signup"),

]