from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
  title = models.CharField(max_length=255)
  price = models.IntegerField()
  ship_date = models.DateTimeField()
  image = models.ImageField()
  discribtion = models.TextField()
  count = models.IntegerField()

  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return reverse('post', kwargs={'post_id': self.pk})

# class User(models.Model):
#   nickname = models.CharField(max_length=25)
#   name = models.CharField(max_length=255)
#   email = models.CharField(max_length=255)
#   image = models.ImageField()
#   discribtion = models.TextField()