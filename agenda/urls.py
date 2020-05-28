from django.urls import path
from . import views

urlpatterns = [
    path('',views.EventListView.as_view(), name='home'),
    path('nouvel-even/', views.EventCreateview.as_view(),name='new-event'),
    path('organisateur/', views.OrganisationListView.as_view(), name='list-org'),
    path('inscription', views.Inscription.as_view(), name="signup"),

]