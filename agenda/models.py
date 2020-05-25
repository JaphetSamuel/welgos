from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User

# Create your models here.

# class Compte(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
#     img_url = models.ImageField(upload_to="profile/", blank=True)
#     suivies = models.ManyToManyField('Organisation', blank=True)
#
#
#     def __str__(self):
#         return self.user.username


class Organisation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    info = models.TextField(blank=True)
    img_url = models.ImageField(upload_to='organisations/', blank=True)
    banner_url = models.ImageField(upload_to='organisations/banner/', blank=True)
    contact = models.CharField(max_length=25)
    siteweb = models.CharField(max_length=300, blank=True)
    facebook = models.CharField(max_length=300, blank=True)
    suiveur = models.ManyToManyField(User, blank=True, related_name='suiveur')


    def __str__(self):
        return self.user.username

# class Organisation(AbstractBaseUser):
#     identifiant = models.CharField(max_length=50, unique=True)
#     nom = models.CharField(max_length=300)
#     info = models.TextField(blank=True)
#     img_url = models.ImageField(upload_to='organisations/', blank=True)
#     banner_url = models.ImageField(upload_to='organisations/banner/', blank=True)
#     email = models.EmailField()
#     contact = models.CharField(max_length=25)
#
#     USERNAME_FIELD = 'identifiant'
#     REQUIRED_FIELDS = ['nom']
#
#     def save(self, *args, **kwargs):
#         self.set_password(self.password)
#         self.normalize_username(self.get_username)
#         return super().save(*args, **kwargs)
#
#     def __str__(self):
#         return self.nom
#

class Event(models.Model):

    def upload(self):
        return f"event/${self.organisateur} "

    organisateur = models.ForeignKey(Organisation, on_delete=models.CASCADE)
    theme = models.CharField(max_length=500, blank=True)
    lieu = models.CharField(max_length=100)
    horodage = models.DateTimeField()
    affiche_url = models.ImageField(upload_to=upload, blank=True)
    reservations = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return f"${self.theme} par ${self.organisateur} "

