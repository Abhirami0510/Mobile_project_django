from django.db import models

# Create your models here.
class Mobile(models.Model):
    model_name=models.CharField(max_length=30,unique=True)
    specs = models.CharField(max_length=120)
    price = models.IntegerField()
    stock = models.IntegerField()
    image = models.ImageField(upload_to="images/")
    def __str__(self):
        return self.model_name
