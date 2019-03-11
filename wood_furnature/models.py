from django.db import models

# Create your models here.

class wood_metal(models.Model):
    id=models.IntegerField(auto_created=True,primary_key=True)
    name=models.CharField(max_length=25,null=True)
    description=models.TextField(null=True)
    furnature_image=models.ImageField(blank=True,null=True,upload_to='images')
    updated=models.DateTimeField(auto_now=True)
    price=models.DecimalField(max_digits=9,decimal_places=2)


    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural="furnatures"





