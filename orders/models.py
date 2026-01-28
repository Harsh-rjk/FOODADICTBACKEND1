from django.db import models

class Order(models.Model):

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('ready', 'Ready to Out'),
        ('out', 'Out for Delivery'),
        ('delivered', 'Delivered'),
    ]

 
    address = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

   

    class Meta:
        db_table = 'orders'   # ✅ SAFE


