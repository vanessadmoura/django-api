from django.db import models

class HelloWorld(models.Model):
    message = models.CharField(max_length=255)
