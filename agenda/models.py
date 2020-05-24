from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser

# Create your models here.
class Compte(AbstractBaseUser):
    pseudonyme = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    img_url = models.ImageField(upload_to="profile/", blank=True)
    suivies = models.ManyToManyField('Organisation', blank=True)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['pseudonyme','email']

    def save(self, *args, **kwargs):
        self.set_password(self.password)
        return super().save(*args,**kwargs)

    def __str__(self):
        return self.pseudonyme

class Organisation(AbstractBaseUser):
    identifiant = models.CharField(max_length=50, unique=True)
    nom = models.CharField(max_length=300)
    info = models.TextField(blank=True)
    img_url = models.ImageField(upload_to='organisations/', blank=True)
    banner_url = models.ImageField(upload_to='organisations/banner/', blank=True)
    email = models.EmailField()
    contact = models.CharField(max_length=25)

    USERNAME_FIELD = 'identifiant'
    REQUIRED_FIELDS = ['nom']

    def save(self, *args, **kwargs):
        self.set_password(self.password)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.nom


class Event(models.Model):

    def upload(self):
        return f"event/${self.organisateur} "

    organisateur = models.ForeignKey(Organisation, on_delete=models.CASCADE)
    theme = models.CharField(max_length=500, blank=True)
    lieu = models.CharField(max_length=100)
    horodage = models.DateTimeField()
    affiche_url = models.ImageField(upload_to=upload, blank=True)
    reservations = models.ManyToManyField(Compte, blank=True)

    def __str__(self):
        return f"${self.theme} par ${self.organisateur}"

