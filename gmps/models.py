from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    mob = models.CharField(max_length=20)
    message = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}, {self.date}"


class ResultPdf(models.Model):
    link = models.TextField()
    linkname = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)


class Image(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name