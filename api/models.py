from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class File(models.Model):
    file = models.FileField(upload_to='uploads/')
    name = models.CharField(max_length=200)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file_type = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)