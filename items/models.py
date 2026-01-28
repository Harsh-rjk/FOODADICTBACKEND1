from django.db import models



class Items(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='items/')

  

    class Meta:
        db_table = 'items'   # 👈 MySQL table name
