from django.db import models
from accounts.models import UserModel
# Create your models here.


class ProductModel(models.Model):
    class Meta:
        db_table = "products"

    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    product_code = models.CharField(max_length=256)
    product_name = models.CharField(max_length=256)
    product_description = models.CharField(max_length=256)
    product_price = models.IntegerField(default=0)
    sizes = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('F', 'Free'),
    )
    product_size = models.CharField(choices=sizes, max_length=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.code

    # def save(self, *args, **kwargs):
    #     pass
