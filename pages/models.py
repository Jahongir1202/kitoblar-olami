from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()
    photo = models.ImageField(upload_to='images/', blank=False)


    def __str__(self):
        return self.title
class Jahon_adabiyotlar(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()
    photo = models.ImageField(upload_to='images/', blank=False)


    def __str__(self):
        return self.title

class Badiy(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()
    photo = models.ImageField(upload_to='images/', blank=True)


    def __str__(self):
        return self.title
class Bolalar(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()
    photo = models.ImageField(upload_to='images/', blank=True)


    def __str__(self):
        return self.title

class Diniy(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()
    photo = models.ImageField(upload_to='images/', blank=True)


    def __str__(self):
        return self.title
class It(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()
    photo = models.ImageField(upload_to='images/', blank=True)


    def __str__(self):
        return self.title

class Chettil(models.Model):
        title = models.CharField(max_length=150)
        text = models.TextField()
        photo = models.ImageField(upload_to='images/', blank=True)


        def __str__(self):
            return self.title

