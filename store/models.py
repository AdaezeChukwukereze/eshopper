from django.db import models

class Image(models.Model):
    image = models.ImageField(upload_to="wears")

    def __str__(self):
        return self.image

COURSE_CHOICES =(
    ("Men's_Shirt","Men's_Shirt"),
    ("Skirt","Skirt"),
    ("Trouser","Trouser"),
    ("Gown","Gown")
)
class Clothes(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(choices = COURSE_CHOICES, max_length=30)
    image = models.ManyToManyField(Image)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    discount_price = models.DecimalField(max_digits=6 , decimal_places=2)


    class Meta():
        verbose_name_plural = "Clothes" 


    def __str__(self):
        return self.name
