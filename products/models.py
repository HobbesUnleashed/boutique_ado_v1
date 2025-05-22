from django.db import models

""" Category model includes a name that is mandatory, friendly_name that is optional """


class Category(models.Model):

    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    """ Returns the name """

    def __str__(self):
        return self.name

    """ Returns the friendly_name """

    def get_friendly_name(self):
        return self.friendly_name


""" Product model has multiple fields 
The category can be left blank when being created and if it is deleted the product will remain but not have a category attached to it
Product MUST HAVE a name, description and a price - everything else is optional """


class Product(models.Model):
    category = models.ForeignKey(
        "Category", null=True, blank=True, on_delete=models.SET_NULL
    )
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    """ Returns the name """

    def __str__(self):
        return self.name
