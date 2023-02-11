from django.db import models

four_seasons = (
    ("Spring", "Spring"),
    ("Summer", "Summer"),
    ("Autumn", "Autumn"),
    ("Winter", "Winter"),
)


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=10, choices=four_seasons)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    photographer = models.CharField(max_length=254, default=None, null=True, blank=True)
    image = models.ImageField(null=False, blank=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.name
