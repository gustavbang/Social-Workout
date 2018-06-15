from django.db import models


class Post(models.Model):
    headline = models.CharField(max_length=200)
    text = models.CharField(max_length=200)


class Fitnessguy(models.Model):
    strength = models.IntegerField()
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)

