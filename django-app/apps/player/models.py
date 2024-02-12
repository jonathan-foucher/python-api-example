from django.db import models


class Player(models.Model):
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
