from django.db import models

class Comment(models.Model):
    author = models.CharField(max_length = 64)
    content = models.CharField(max_length = 128)

    def __str__(self):
        return (self.author + ': ' + self.content)

class Type(models.Model):
    name = models.CharField(max_length = 64)

    def __str__(self):
        return(self.name)

class Nameofgame(models.Model):
    name = models.CharField(max_length = 64)

    def __str__(self):
        return(self.name)

class Game(models.Model):
    name = models.ManyToManyField(Nameofgame, blank = True)
    type =  models.ManyToManyField(Type, blank = True)
    comments = models.ManyToManyField(Comment, blank = True)

    def __str__(self):
        return (str(self.type) + ' ' + str(self.name))

class Contact(models.Model):
    phone = models.CharField(max_length = 64)

    def __str__(self):
        return(self.phone)

# Create your models here.
