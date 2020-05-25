from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, TemplateView
from django.contrib.auth import authenticate
from django.views.generic import  ListView, DetailView
from django.views.generic.edit import ProcessFormView
from .models import *

# Create your views here.

def home(request):
    return render(request, template_name='index.html')

class Inscription(TemplateView, ProcessFormView):

    def get(self, request, *args, **kwargs):
        self.template_name = 'registration/signup.html'
        return super().get(request,**kwargs)

    def post(self, request, *args, **kwargs):
        error_context = {}
        pseudo = request.POST['pseudo']
        email = request.POST['email']
        pass1 : str = request.POST['pass1']
        pass2 = request.POST['pass2']

        #verification du mot de passe
        if pass1.__eq__(pass2) :
            error_context["passerreur"] = "les mot de passe sont différents"
        
        #TODO: verification de l'email

        if error_context.__len__() > 0:
            return render(request,template_name='registration/signup.html', context=error_context)

        else:
            u = User(username=pseudo, email=email)
            u.set_password(pass2)
            u.save()
            Compte(user=u).save()
            user = authenticate(username=u.username, password=pass2)
            if user is not None:
                return redirect('home')
            return


class EventListView(ListView):
    model = Event
    template_name = 'agenda/listeEvent.html'