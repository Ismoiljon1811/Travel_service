from django.db import models

class Category(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self) -> str:
        return self.name


class Reys(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self) -> str:
        return self.name



class Travel(models.Model):
    name = models.CharField(max_length = 100)
    category = models.ForeignKey(Category,on_delete = models.CASCADE, related_name = 'davlat')
    reys = models.ForeignKey(Reys,on_delete = models.CASCADE, related_name = 'reys', null = True)
    price = models.IntegerField()
    image = models.ImageField(upload_to ='product_image/', null=True)

    def __str__(self) -> str:
        return self.name
