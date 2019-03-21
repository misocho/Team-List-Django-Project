from django.db import models

class TeamList(models.Model):
    firstname = models.CharField("Firstname", max_length=50)
    lastname = models.CharField("Lastname", max_length=50)