from django.db import models


class Wazamoku(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Waza(modesl.Model):
    wazamoku = models.ForeignKey(Wazamoku, on_delete=models.CASCADE)
    toi = models.TextField()
    kai1 = models.CharField(max_length=40)
    kai2 = models.CharField(max_length=40, default='')
    kai3 = models.CharField(max_length=40, default='')
    shutoku = models.BooleanField(default=False)

    def __str__(self):
        return self.toi
