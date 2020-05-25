from django.shortcuts import render
from django.contrib.auth.views import LoginView, TemplateView
from django.views.generic.edit import ProcessFormView

# Create your views here.

def home(request):
    return render(request, template_name='index.html')

class Inscription(TemplateView, ProcessFormView):

    def get(self, request, *args, **kwargs):
        self.template_name = 'registration/signup.html'
        return super().get(request,**kwargs)

    def post(self, request, *args, **kwargs):
        return render(request,template_name='registration/signup.html', context={'erreur':'erreur sur le mot de passe'})