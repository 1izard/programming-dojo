from django.db import models
from django.urls import reverse


class Ryugi(models.Model):
    na = models.CharField(max_length=20, unique=True)
    kotodute = models.CharField(max_length=40, blank=True)

    def __str__(self):
        return self.na


class Kata(models.Model):
    ryugi = models.ForeignKey(Ryugi, related_name='katas', on_delete=models.CASCADE)
    kataki = models.TextField()
    waza1 = models.CharField(max_length=40)
    waza2 = models.CharField(max_length=40, blank=True)
    waza3 = models.CharField(max_length=40, blank=True)
    rendo = models.CharField(
        max_length=1,
        choices=[('0', 'Mijuku'), ('1', 'Nami'), ('2', 'Jukuren')],
        default='0'
    )

    def __str__(self):
        return self.kataki
    
    def get_absolute_url(self):
        return reverse('izanamijinja:index')
