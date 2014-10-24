from django.db import models
from thumbs import ImageWithThumbsField


class Owner(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __unicode__(self):
        return self.name


class Dog(models.Model):
    owner = models.ForeignKey(Owner)
    name = models.CharField(max_length=50)
    image = ImageWithThumbsField(
        upload_to='dogs/images', sizes=((150, 150),))

    def __unicode__(self):
        return self.name
