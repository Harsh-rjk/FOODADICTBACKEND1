from django.db import models

class Account(models.Model):
    number = models.CharField(max_length=15)
    password = models.CharField(max_length=128)

    class Meta:
        db_table = 'account'
