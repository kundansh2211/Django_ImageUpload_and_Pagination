from django.db import models

class Hotels(models.Model):
    name = models.CharField(max_length=20, verbose_name='Hotel Name: ')
    city = models.CharField(max_length=30, verbose_name='City: ')
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f'{self.name} {self.city} {self.image}'

