from django.db import models


class Wazamoku(models.Model):
    daimoku = models.CharField(max_length=20)
    # kotodute = models.CharField(max_length=40, blank=True)

    def __str__(self):
        return self.name


class Waza(models.Model):
    wazamoku = models.ForeignKey(Wazamoku, on_delete=models.CASCADE)
    toi = models.TextField()
    kai1 = models.CharField(max_length=40)
    kai2 = models.CharField(max_length=40, blank=True)
    kai3 = models.CharField(max_length=40, blank=True)
    rendo = models.CharField(
        max_length=1,
        choices=[('0', 'Mijuku'), ('1', 'Nami'), ('2', 'Jukuren')],
        default='0'
    )

    def __str__(self):
        return self.toi
