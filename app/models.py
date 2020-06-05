from django.db import models
from django.shortcuts import reverse


class User(models.Model):
    username = models.CharField(max_length=255, null=False)
    email = models.EmailField(max_length=255, null=False)
    password = models.CharField(max_length=50)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,)
    hobby = models.CharField(max_length=255, default="",)
    ifLogged = models.BooleanField(default=False)
    token = models.CharField(max_length=500, null=True, default="")

    def __str__(self):
        return "{} -{}".format(self.username, self.email)


class Item(models.Model):
    I_id = models.IntegerField( null = False)
    title = models.CharField(max_length=225,null = False)
    description = models.CharField(max_length=  1000, null=False)
    discount_price = models.FloatField(blank=True, null=True)
    price = models.FloatField(null=False)
    image = models.ImageField(upload_to='images')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title



    def get_add_to_cart_url(self):
        return reverse("core:add-to-cart", kwargs={
            'slug': self.slug
        })

    def get_remove_from_cart_url(self):
        return reverse("core:remove-from-cart", kwargs={
            'slug': self.slug
        })









