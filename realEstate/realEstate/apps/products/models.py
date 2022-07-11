from django.db import models
from nanoid import generate
from django.utils.translation import gettext_lazy as _


# 产品库

def nanoid_generate():
    return generate(size=10)


class Test(models.Model):
    id = models.CharField(max_length=10, default=nanoid_generate, primary_key=True)
    name = models.CharField(max_length=25, default='123')


class BuildingProduct(models.Model):
    id = models.CharField(_('系统编码'), max_length=10, default=nanoid_generate, primary_key=True)
    product_code = models.CharField(_('产品编码'), max_length=100)


    class Meta:
        db_table = 'building_product'
