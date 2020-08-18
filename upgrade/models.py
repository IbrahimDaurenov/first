from django.db import models

class Comment(models.Model):
    author = models.CharField(max_length = 64)
    content = models.CharField(max_length = 128)

    def __str__(self):
        return (self.author + ': ' + self.content)

class Game(models.Model):
    name = models.CharField(max_length = 64)

    def __str__(self):
        return(self.name)

class Games(models.Model):
    type =  models.ManyToManyField(Game, blank = True)
    comments = models.ManyToManyField(Comment, blank = True)

class Contact(models.Model):
    phone = models.CharField(max_length = 64)

# Create your models here.
