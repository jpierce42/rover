from django.db import models


class Owner(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class Dog(models.Model):
    owner = models.ForeignKey(Owner)
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name
