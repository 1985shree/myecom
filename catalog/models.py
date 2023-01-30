from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):
    title = models.CharField(max_length=200) # name/title of the item
    price = models.DecimalField(max_digits = 1000, decimal_places = 2)
    discount_price = models.DecimalField(max_digits = 1000, decimal_places = 2, blank = True, null = True)
    description = models.CharField(max_length=2000)
    slug = models.SlugField() #A "slug" is a way of generating a valid URL, generally using data already obtained. For instance,
    # a slug uses the title of an article to generate a URL, e.g. if title is black polo necked tshirt, slug makes it black-polo-necked-tshirt,
    # and it's possible to make an url with it: <slug>black-polo-necked-tshirt</slug>

    def __str__(self): # python method which is called when we use print/str to convert object into a string
        return self.title

class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # to delete all related entries to the key from db
    item = models.ForeignKey(Item, on_delete = models.CASCADE) # one key per item
    ordered = models.BooleanField(default = False)
    quantity = models.IntegerField(default = 1)

    def __str__(self): # python method which is called when we use print/str to convert object into a string
        return f"{self.quantity} of {self.item.title}" # see title in Item class


class Order(models.Model): # related to orders and users
    user = models.ForeignKey(User, on_delete=models.CASCADE) # to delete all related entries to the key from db
    ordered = models.BooleanField(default = False)
    items = models.ManyToManyField(OrderItem) # order will have many-to-many relationship with OrderItem
    start_date = models.DateTimeField(auto_now_add =True) #
    ordered_date = models.DateTimeField()

    def __str__(self): # python method which is called when we use print/str to convert object into a string
        return self.user.username
