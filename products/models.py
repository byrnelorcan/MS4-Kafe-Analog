from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Genre(models.Model):
    genre = models.CharField(max_length=254)

    def __str__(self):
        return self.genre


class Condition(models.Model):
    condition = models.CharField(max_length=254)

    def __str__(self):
        return self.condition


class Products(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    product_id = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    artist = models.CharField(max_length=254)
    genre = models.ForeignKey('Genre', null=True, blank=True,
                              on_delete=models.SET_NULL)
    sub_genre = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    year = models.CharField(max_length=254)
    condition = models.ForeignKey('Condition', null=True, blank=True,
                                  on_delete=models.SET_NULL)
    in_stock = models.BooleanField(default=True)

    def __str__(self):
        return self.name
