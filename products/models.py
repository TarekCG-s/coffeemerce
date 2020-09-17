from django.db import models
from django.db.models import Max
from django.db.models.signals import post_save
from django.dispatch import receiver


class ProductsBase(models.Model):
    
    PRODUCT_TYPES_CODES = {}
    product_type = models.IntegerField()
    code = models.CharField(max_length=255, null=True, blank=True)
    price = models.FloatField(null=False, blank=False, default=0.0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self,*args, **kwargs):
        objs = self.__class__.objects.all()
        new_id = objs.aggregate(Max('id'))['id__max'] + 1 if objs else 1
        self.code = self.PRODUCT_TYPES_CODES.get(self.product_type) + '{:03d}'.format(new_id)
        super(ProductsBase, self).save(*args, **kwargs)

    class Meta:
        abstract = True

class CoffeeMachine(ProductsBase):

    class ProductType(models.IntegerChoices):
        COFFEE_MACHINE_SMALL = 0
        COFFEE_MACHINE_LARGE = 1
        ESPRESSO_MACHINE = 2

    class ProductClass(models.IntegerChoices):
        BASE_MODEL = 0
        PREMIUM_MODEL = 1
        DELUXE_MODEL = 2

    PRODUCT_TYPES_CODES = {
        ProductType.COFFEE_MACHINE_LARGE: 'CM',
        ProductType.COFFEE_MACHINE_SMALL: 'CM',
        ProductType.ESPRESSO_MACHINE: 'EM',
    }

    product_type = models.IntegerField(choices=ProductType.choices, default=0)
    product_class = models.IntegerField(choices=ProductClass.choices, default=0)
    water_line_compatible = models.BooleanField(default=False)
    
    def __str__(self):
        return "{code} - {type} - {product_class}".format(
            code=self.code, type=self.get_product_type_display(), product_class=self.get_product_class_display()
        )

class CoffeePod(ProductsBase):

    class ProductType(models.IntegerChoices):
        COFFEE_POD_SMALL = 0
        COFFEE_POD_LARGE = 1
        ESPRESSO_POD = 2

    class CoffeeFlavor(models.IntegerChoices):
        COFFEE_FLAVOR_VANILLA = 0
        COFFEE_FLAVOR_CARAMEL = 1
        COFFEE_FLAVOR_PSL = 2
        COFFEE_FLAVOR_MOCHA = 3
        COFFEE_FLAVOR_HAZELNUT = 4

    class PackSize(models.IntegerChoices):
        ONE_DOZEN = 0, ('1 Dozen (12)')
        THREE_DOZEN = 1, ('3 Dozen (36)')
        FIVE_DOZEN = 2, ('5 Dozen (60)')
        SEVEN_DOZEN = 3, ('7 Dozen (84)')

    PRODUCT_TYPES_CODES = {
        ProductType.COFFEE_POD_LARGE: 'CP',
        ProductType.COFFEE_POD_SMALL: 'CP',
        ProductType.ESPRESSO_POD: 'EP',
    }

    product_type = models.IntegerField(choices=ProductType.choices, default=0)
    coffee_flavor = models.IntegerField(choices=CoffeeFlavor.choices, default=0)
    pack_size = models.IntegerField(choices=PackSize.choices, default=0)

    def __str__(self):
        return "{code} - {type} - {flavor} - {pack}".format(
            code=self.code, type=self.get_product_type_display(), flavor=self.get_coffee_flavor_display(),
            pack=self.get_pack_size_display()
        )
