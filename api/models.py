from django.contrib.auth import get_user_model
from django.db import models
from gdstorage.storage import GoogleDriveStorage
from gdstorage.storage import GoogleDriveStorage, GoogleDrivePermissionType, GoogleDrivePermissionRole, GoogleDriveFilePermission

permission =  GoogleDriveFilePermission(
   GoogleDrivePermissionRole.OWNER,
   GoogleDrivePermissionType.ANYONE
)

User = get_user_model()

gd_storage = GoogleDriveStorage()

class File(models.Model):
    file = models.FileField(storage=gd_storage)
    name = models.CharField(max_length=200)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file_size = models.IntegerField()
    file_type = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)